# GitHub Profile Cleanup: maadhav-codes

The goal is that a hiring manager who clicks the GitHub link on the Full-Stack resume sees the **same person**: a 4-year full-stack engineer, not a "6-month frontend developer" working through Frontend Mentor levels.

## What's wrong today

| Issue | Seen by a recruiter as |
|---|---|
| Bio: *"Frontend Developer with 6 months of experience."* | Contradicts "4+ years, SDE-2" on the resume. |
| Profile README is a Frontend Mentor tracker that marks **"Full-Stack Architectures: Locked"** | Directly undercuts the Full-Stack resume. |
| No pinned repos | The page shows forks and archived CSS challenges first. |
| 11 forks with no commits (`*-forked`, WinDiskWriter, Beginner-Friendly-Ai-Vtuber) | Padding. |
| 9 archived `fm-*` repos + `DCN` ("learning web development") | Reads as a beginner. |
| `vs-code-extension`, `maadhav-codes`: no description | Looks unfinished. |

## Step 1: run the script (automated)
```bash
gh auth login                    # log in as maadhav-codes
bash github/apply.sh
```
This updates the bio, location, website and hireable flag, replaces the profile README (with a backup at `README.old.md`), and adds descriptions and topics to the featured repos.

## Step 2: pin repos (manual, there is no API)
Profile → **Customize your pins** → select these, in this order:
1. `ollama-vox`
2. `anime-ai-companion`
3. `diff2commit`
4. `mica`
5. `svara-music-player` (Flutter; shows range)
6. `frontend-mentor-solutions` (optional; one tidy repo instead of nine)

## Step 3: reduce noise (your call; these are destructive or hard to reverse)
- **Forks you never committed to** cannot be made private. Either delete them (Settings → Delete), or leave them; once pins exist they matter much less.
- **The 9 archived `fm-*` repos** are already merged into `frontend-mentor-solutions`. Delete them, or make them private (Settings → unarchive → change visibility → re-archive). Their GitHub Pages demos will stop working.
- **`DCN`**: make it private ("learning web development" notes).
- **`vs-code-extension`**: add a one-line description and README, or make it private.

## Step 4: make the featured repos senior-proof (next weekend)
| Repo | Add |
|---|---|
| ollama-vox | 15-second demo GIF at the top of the README · GitHub Actions running `pytest` + badge · v0.1.0 release |
| anime-ai-companion | Deploy to Vercel and set the repo **Website** field · screenshot/GIF · a few Vitest tests + CI |
| diff2commit | pytest tests + CI · publish to PyPI so `pip install diff2commit` works · demo GIF |
| all | Short "Architecture / design decisions" section in each README |

## Step 5: keep it consistent
Whenever the resume changes, update the bio, the profile README "What I've worked on" section, Wellfound and LinkedIn in the same sitting.
