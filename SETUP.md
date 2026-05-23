# 🚀 Profile README — Setup Guide

## What this is
A "rice'd out" GitHub **profile README**. GitHub shows the README of a special
repo named **exactly your username** at the top of your profile page.

## Steps to go live

1. **Create the magic repo**
   - On GitHub, create a new **public** repo named exactly **`SRock44`**.
   - GitHub will show a "✨ You found a secret!" hint when the name matches — that confirms it.
   - Leave it empty (don't add a README — we already have one).

2. **Push these files**
   ```bash
   cd C:\Users\winst\githubprof
   git init
   git add .
   git commit -m "✨ rice out my profile"
   git branch -M main
   git remote add origin https://github.com/SRock44/SRock44.git
   git push -u origin main
   ```

3. **Turn on the snake animation**
   - Repo → **Settings → Actions → General → Workflow permissions**
   - Select **"Read and write permissions"** → Save.
   - Repo → **Actions** tab → run **"Generate Contribution Snake"** once (Run workflow).
   - This creates the `output` branch the README pulls the snake SVG from.
     (After the first run it auto-refreshes every 12 hours.)

4. **Check it** — visit `https://github.com/SRock44` 🎉

## ⚠️ Two things to personalize before you push
- **Email**: the "Reach me" badge currently points to `drwelter7@gmail.com`.
  Edit it in `README.md` (or remove that line) if you'd rather not make it public.
- **LinkedIn**: a commented-out LinkedIn badge is in the "Let's Connect" section.
  Add your handle and uncomment it — recruiters love a LinkedIn link.

## Notes
- All stat cards (stats, top-langs, streak, profile views) auto-update — no maintenance.
- Want a light/different theme? The cards use `theme=tokyonight`; other options:
  `radical`, `dracula`, `synthwave`, `github_dark`, `nightowl`.
- Don't worry if the snake/stat images look broken locally — they only render
  once the repo is pushed and the Action has run.
