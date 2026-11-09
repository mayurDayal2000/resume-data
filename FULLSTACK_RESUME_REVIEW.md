# Full-Stack Resume Review: Mayur Dayal

**Reviewed:** `resumes/Mayur_Dayal_Fullstack_Resume.pdf` (source: `resumes/src/build.py` → `"Fullstack"`)
**Cross-checked against:** Wellfound profile (`wellfound.com/u/mayur_dayal_15`, public part only) and GitHub (`github.com/maadhav-codes`)
**Lens:** how a hiring manager or senior engineer screens a 4-year full-stack candidate in about 30 seconds, and then digs in.

> Rule for every edit below: **only claim what you can defend in an interview.** Wherever you see `[X]`, put in a real number. If you don't have one, drop the metric rather than invent it.

---

## 0. TL;DR: top 7 fixes, by impact

| # | Problem | Why a reviewer cares | Fix |
|---|---|---|---|
| 1 | **Your profiles disagree with each other.** The resume says *Full-Stack, 4+ yrs, SDE-2*. Wellfound says *"Frontend-Focused SDE-1, 2+ Years"*. The GitHub bio says *"Frontend Developer with 6 months of experience."* | This is the #1 credibility killer. Recruiters open Wellfound and GitHub next to the resume, and three different seniority stories looks like inflation. | Make all three match today (§1). |
| 2 | **No numbers anywhere.** None of the 13 experience bullets has a metric. | Without scale or impact, the bullets read like a task list. A senior dev can't tell whether you handled 10 users or 100k. | Add 1 metric to at least 60% of bullets (§3). |
| 3 | **Neither project is full-stack.** Both are local Python tools (CLI + Qt desktop app). | On a *full-stack* resume, the projects should prove the stack in the headline: web UI + API + DB + auth + deploy + tests. | Replace or add one deployed full-stack project (§5). |
| 4 | **About 11-month gap** since Dec 2025 (BLACKBOX contract ended), and nothing explains it. | Gaps are fine, *unexplained* gaps are not. | Add a line such as "Independent / Open Source, Jan 2026 – Present" (§3). |
| 5 | **The skills list claims tools no bullet backs up**: Redux Toolkit, Zustand, TanStack Query, PostgreSQL, Redis, Prisma, Alembic, Supabase, Docker, GitHub Actions, JWT, Gemini. | Interviewers pick one tool from your skills and drill into it. If no bullet uses it, it looks like keyword stuffing. | Keep a tool only if a bullet or project uses it, or if you'd be happy to be grilled on it (§2). |
| 6 | **The BLACKBOX contract (2 months) overclaims**: "Built an AI application-generation platform." | No one builds a whole platform in 8 weeks on a contract. Seniors spot this immediately and start doubting everything else. | Scope it honestly: "Built the X and Y for BLACKBOX's app-generation product" (§3). |
| 7 | **"30+ responsive web interfaces"** under freelance. Your GitHub is mostly **Frontend Mentor practice solutions**. | If any of the 30 are practice challenges, that's a misrepresentation, and the GitHub profile makes it easy to suspect. | Count only paid client work. Name 1–2 clients or domains (§3). |

---

## 1. Fix consistency first (Wellfound, GitHub, LinkedIn)

**Wellfound headline: current version (outdated):**
> Frontend-Focused SDE-1 | 2+ Years Experience in React, JavaScript/TypeScript, HTML5 & CSS3 | Skilled in Responsive Design, UI/UX, & Web Performance Optimization

**Replace with:**
> Full-Stack Engineer (SDE-2) · 4+ yrs · React/TypeScript + Python/FastAPI · Payments, GitHub Apps, LLM tooling

Also on Wellfound:
- Role sought: **Full-Stack Engineer** as the primary role, with Frontend and Backend as secondary.
- Paste the new summary from §3 into the bio.
- Experience: same companies, titles and dates as the resume. Show Penify as **two titles** (SDE-1, then SDE-2) so the promotion is visible.
- Add the GitHub link and the resume PDF.

**GitHub (`maadhav-codes`):**
- Bio: change *"Frontend Developer with 6 months of experience."* to **"Full-stack engineer: React/TS + Python/FastAPI. Building local-first AI tools."**
- **Pin 4–6 repos**: the new full-stack project (§5), `ollama-vox`, `diff2commit`, `anime-ai-companion`. Right now nothing is pinned, so visitors land on forks and archived CSS challenges.
- Move the 9 archived `fm-*` repos into the existing `frontend-mentor-solutions` repo, or make them private. Unstar or hide the forks you never contributed to (`*-forked`). They add noise and suggest the profile is padded.
- Add a profile README (`maadhav-codes/maadhav-codes` already exists and is empty) with a 3-line intro, your stack, and links to the pinned projects.
- Give `vs-code-extension` a description or make it private.

---

## 2. Header, headline, skills

**Headline:** good. Keep: `Full-Stack Engineer | React, TypeScript, Python/FastAPI | AI Developer Tools`

**Contact:** add the Wellfound or portfolio link. Write `linkedin.com/in/mayur-dayal` without the trailing slash, consistent with the base resume.

**Skills: current vs. proposed.** Trim to what the bullets prove. A shorter, credible list beats a long one.

```
Languages:        TypeScript, JavaScript, Python, SQL
Frontend:         React, Next.js, TanStack Query, Tailwind CSS, shadcn/ui
Backend:          FastAPI, Pydantic, Node.js, REST, Webhooks, OAuth 2.0 / JWT
Data:             PostgreSQL, MongoDB, Redis            ← only if a bullet below uses them
AI / LLM:         OpenAI API, Ollama, streaming responses, agent/tool workflows
Testing & Ops:    pytest, Docker, GitHub Actions, Vercel
```

Removed or held back until a bullet backs them up: **Redux Toolkit, Zustand** (pick the one you actually used at Penify), **Prisma, Alembic, Supabase** (which job used them?), **Gemini API**, **HTML/CSS** (implied for any frontend engineer), **"Vercel Sandboxes"** (keep it in the BLACKBOX bullet, not in skills).

> Tip: for every skill left in the list, you should be able to say *"I used it at ___ to ___."*

---

## 3. Rewritten Full-Stack resume (ready to drop into `build.py`)

### Summary
**Current:** generic, and it says "end to end" twice across the resume.

**Proposed:**
> Full-Stack Engineer with 4+ years shipping SaaS products in React/TypeScript and Python/FastAPI. At Penify.dev (promoted SDE-1 → SDE-2), owned billing, GitHub App integrations, and the customer dashboard used by [X] developers / [X] orgs. Most recently built LLM agent tooling at BLACKBOX AI that turns a prompt into a deployed app. Comfortable owning a feature from schema to UI to production.

### Experience

**Independent / Open Source**, *Full-Stack Engineer*, **Jan 2026 – Present** ← *new; closes the gap*
- Building local-first AI developer tools in Python and TypeScript (Ollama Vox, diff2commit, Anime Companion); [X] commits across [X] repos.
- *(If you interviewed, freelanced, or upskilled in this period, say so here, e.g. "Delivered [X] for a client".)*

---

**BLACKBOX AI**, *Full-Stack Engineer (Contract)*, **Nov 2025 – Dec 2025**
- Built the **agent execution layer** for BLACKBOX's prompt-to-app product: LLM-generated files written and run in isolated **Vercel Sandboxes**, with live status streamed to the UI.
- Shipped the workspace UI (chat, file explorer, terminal logs, live preview) in React/TypeScript, streaming LLM output token by token.
- Automated one-click **GitHub repo creation + Vercel production deploy**; persisted project, conversation and deployment state in MongoDB. *Add: "cut prompt-to-live-URL to ~[X] min" if you know it.*

> Why: "Built *the agent execution layer for*" is honest for 2 months and still impressive. "Built a platform" is not believable.

---

**Penify.dev**, *Software Engineer II (SDE-2)*, **Feb 2025 – Oct 2025**
- Owned **billing end to end**: Cashfree + PayPal checkout, webhook-based transaction validation, and repo-based subscription eligibility in FastAPI, processing [X] payments / ₹[X] per month.
- Built **GitHub App** integrations (repo discovery, org filtering, usage analytics, doc-generation triggers) used by [X] installations / [X] repos.
- Designed FastAPI endpoints and the service layer for repositories, accounts and analytics on **PostgreSQL** *(or whatever the DB actually was; name it)*; reduced [endpoint] p95 latency from [X] ms to [X] ms *(only if true)*.
- Extended the documentation engine with TypeDoc, changelog generation and multi-language support, adding [X] languages.

**Penify.dev**, *Software Engineer I (SDE-1)*, **Jul 2023 – Jan 2025**
- Built the **React/TypeScript customer dashboard** (repo management, doc jobs, API keys, billing history, plan upgrades, coupons) using [TanStack Query / Redux], shipping [X] features.
- Implemented auth: email sign-up, password reset, protected routes, and **Google/GitHub OAuth**.
- Built the Next.js + Tailwind marketing site and product tour; improved Lighthouse performance from [X] to [X] *(fits the "web performance" claim on Wellfound)*.

> Why split SDE-1 and SDE-2: a promotion inside 19 months is one of the strongest signals on this resume. The base resume shows it, but the current Full-Stack version buries it in a single line.

---

**Freelance Web Developer (Remote Clients)**, **Mar 2022 – Jun 2023**
- Delivered [X] client projects (e.g. [domain: e-commerce / clinic booking / agency site]) from requirements through deployment.
- Built React apps integrated with [specific APIs: Razorpay, Firebase, CMS…]; *name at least one real thing.*

> Remove "30+ interfaces" unless every one was paid client work.

---

**ZinEdu Classes Pvt. Ltd.**, *Front-End Developer*, **Aug 2021 – Feb 2022**
- Built role-based React dashboards (student / teacher / admin) for classes, assignments, exams and analytics, serving [X] students.
- Built admin tools for attendance and fee collection with CSV/PDF reporting.

### Education
Unchanged. Add "West Bengal" only if space allows.

---

## 4. Review of the current projects

| Project | What a senior dev sees on GitHub | Verdict |
|---|---|---|
| **ollama-vox** | 35 commits, pytest suite, MIT, clear README. No demo GIF, no releases, no CI badge. | **Good. Keep.** Add a 15-second demo GIF, a GitHub Actions workflow running pytest, and a v0.1.0 release. |
| **diff2commit** | **4 commits, no tests** (the README says so), not on PyPI. The resume says "built and packaged" and dates it Oct–Nov 2025. | **Weak as it stands.** "Packaged" is a stretch without a PyPI release. Either publish it (`pip install diff2commit`), add tests and CI, and add a demo, or drop it from the resume. |
| **anime-ai-companion** | React 19 + TS + Vite, Live2D, streaming LLM chat, TTS, 21 commits. No tests, no live demo, no backend. | **Not on the resume, but it's your only TypeScript project.** With a live Vercel demo, it shows frontend craft better than the other two. |

**Main issue:** the resume says **Full-Stack**, but both listed projects are **Python-only local tools**. There is no web backend, no database, no auth, and no deployed URL. Nothing in the project section proves the "full-stack" claim independently of employer work. Hiring managers can't see your Penify code, so **the projects are the only code they can verify.**

Also check the date mismatch: diff2commit is listed as Oct–Nov 2025, but the repo's activity is in Oct 2026. Make the dates match the commit history.

---

## 5. Project suggestions (what would actually move the needle)

Build **one** of these properly rather than three half-done ones. Each is deliberately close to what you already did at Penify and BLACKBOX, so in interviews it reads as depth rather than a toy.

### Option A (recommended): "PR Pilot", a GitHub App that reviews and documents PRs
- **Stack:** Next.js dashboard + FastAPI + PostgreSQL + Redis (job queue) + GitHub App webhooks + an LLM (Ollama/OpenAI) + Stripe **test mode** billing.
- **Flow:** install the app on a repo → a PR opens → a webhook enqueues a job → a worker generates a review summary or changelog → it posts a PR comment → the dashboard shows job history and usage.
- **Why it wins:** it shows webhooks, queues/async workers, idempotency, auth, a DB schema, billing, and LLM integration, which is every keyword on your resume, now verifiable.
- **Must-haves for credibility:** live URL, installable on a real repo, pytest + Playwright tests, GitHub Actions CI, Docker Compose for local dev, an architecture diagram in the README, and a "Design decisions" section (retries, rate limits, webhook signature verification).

### Option B: real-time collaborative app
e.g. a multiplayer kanban or whiteboard. Next.js + FastAPI WebSockets + Postgres + Redis pub/sub. Shows real-time systems, optimistic UI, conflict handling and auth.

### Option C: upgrade what you already have (lowest effort)
- **anime-ai-companion:** add a small FastAPI backend (auth, per-user chat history in Postgres, server-side API keys so they aren't stored in localStorage), deploy it, and add tests. That turns it into a genuine full-stack project.
- **diff2commit:** publish to PyPI, add pytest + CI, a demo GIF, and a Homebrew tap. Then "packaged" is true.

**Final Projects section for the Full-Stack resume (2 entries max):**
1. The new full-stack project (A, B, or the upgraded anime-ai-companion), with a **live link**.
2. Ollama Vox, which shows systems thinking (concurrency, queues, cancellation, tests).

Drop diff2commit from the Full-Stack version unless it's upgraded. It can stay on the Backend resume.

---

## 6. Smaller polish items

- **Experience math:** Aug 2021 – Dec 2025 ≈ 4.3 yrs including 15 months of freelancing. "4+ years" is defensible; just be ready to break it down.
- **Title consistency:** the base PDF says "Full Stack Engineer" and build.py says "Full-Stack Engineer". Pick **Full-Stack** everywhere.
- **Verbs:** many bullets start with "Built". Vary them: *Owned, Designed, Shipped, Migrated, Cut, Automated, Led*.
- **One page:** the Full-Stack version should stay one page. With the trimmed skills and two projects, it will.
- **ATS:** the layout is single-column with standard headings, which is fine. Keep the PDF text-selectable, which it is.
- **File naming:** `Mayur_Dayal_Fullstack_Resume.pdf` → `Mayur_Dayal_FullStack_Engineer.pdf` (minor).

---

## 7. Checklist

- [ ] Wellfound headline, bio and role updated to match the resume
- [ ] GitHub bio fixed, repos pinned, FM/forks cleaned up, profile README added
- [ ] Real numbers filled into every `[X]` (or the clause removed)
- [ ] Penify split into SDE-1 / SDE-2 in the Full-Stack resume
- [ ] BLACKBOX bullets re-scoped
- [ ] "30+ interfaces" verified or removed
- [ ] Jan 2026 – Present entry added to close the gap
- [ ] Skills trimmed to those backed by bullets
- [ ] One deployed full-stack project with tests, CI and a live link
- [ ] diff2commit upgraded or removed from the Full-Stack version
- [ ] Rebuild: `cd resumes/src && python3 build.py`

---

## 8. Applied (2026-11-09)

Applied to `resumes/src/build.py` → `"Fullstack"`, and rebuilt `resumes/Mayur_Dayal_Fullstack_Resume.pdf` (1 page):
- New headline and summary (promotion and ownership up front).
- Skills trimmed to tools that the bullets back up.
- Added "Independent AI Tooling Projects, Jan 2026 – Present" to close the gap.
- BLACKBOX re-scoped to the "agent execution layer + workspace UI".
- Penify split into SDE-2 and SDE-1 (the renderer now shows a promotion under one company heading).
- Removed "30+ interfaces". Condensed freelance and ZinEdu.
- Projects: Ollama Vox + Anime Companion (the TypeScript/React project). diff2commit dropped from this version (4 commits, no tests).
- **No metrics were invented.** Still TODO: add real numbers (users, payments, repos, latency) where you have them, and the GitHub/Wellfound cleanup in §1.
