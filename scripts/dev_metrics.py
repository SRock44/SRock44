"""Update the README commit-time section. Stdlib only, owned non-fork repos, last 365 days."""
import json, os, re, sys, urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

TOKEN = os.environ["GH_TOKEN"]
USER = os.environ.get("GH_USER", "SRock44")
TZ = ZoneInfo(os.environ.get("METRICS_TZ", "America/New_York"))
SINCE = (datetime.now(timezone.utc) - timedelta(days=365)).strftime("%Y-%m-%dT%H:%M:%SZ")


def get(url):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def paged(url):
    page = 1
    while True:
        data = get(f"{url}{'&' if '?' in url else '?'}per_page=100&page={page}")
        if not data:
            return
        yield from data
        if len(data) < 100:
            return
        page += 1


repos = [r for r in paged("https://api.github.com/user/repos?affiliation=owner")
         if not r["fork"] and not r["archived"] and r["owner"]["login"] == USER]

seen, times = set(), []
for r in repos:
    try:
        for c in paged(f"https://api.github.com/repos/{r['full_name']}/commits?author={USER}&since={SINCE}"):
            if c["sha"] in seen:
                continue
            seen.add(c["sha"])
            ts = c["commit"]["author"]["date"]
            times.append(datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(TZ))
    except Exception as e:  # empty repos return 409
        print(f"skip {r['full_name']}: {e}", file=sys.stderr)

total = len(times) or 1
BARS = 25


def bar(n):
    filled = round(n / total * BARS)
    return "█" * filled + "░" * (BARS - filled)


def row(label, n):
    return f"{label:<24} {f'{n} commits':<19} {bar(n)}   {n / total * 100:05.2f} %"


parts = Counter(("Night", "Morning", "Daytime", "Evening")[t.hour // 6] for t in times)
days = Counter(t.strftime("%A") for t in times)
icons = [("🌞 Morning", "Morning"), ("🌆 Daytime", "Daytime"), ("🌃 Evening", "Evening"), ("🌙 Night", "Night")]
names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
best = max(names, key=lambda d: days[d])

body = "\n".join([
    f"**{len(times)} commits in the last 365 days across {len(repos)} owned repos**",
    "", "```text", *[row(i, parts[k]) for i, k in icons], "```",
    f"📅 **I'm Most Productive on {best}**", "", "```text", *[row(d, days[d]) for d in names], "```",
    "", f" Last Updated on {datetime.now(timezone.utc):%m/%d/%Y} UTC", ""])

text = open("README.md", encoding="utf-8").read()
new = re.sub(r"(<!--START_SECTION:waka-->).*?(<!--END_SECTION:waka-->)",
             lambda m: f"{m[1]}\n{body}{m[2]}", text, flags=re.S)
open("README.md", "w", encoding="utf-8").write(new)
print(f"{len(times)} commits, {len(repos)} repos")
