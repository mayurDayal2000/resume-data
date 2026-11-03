"""Build role-tailored resumes (HTML -> PDF via headless Chrome).

Usage: python3 build.py
Edit the content dicts below, then re-run. Output PDFs land in ../
"""
import html
import pathlib
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

NAME = "Mayur Dayal"
CONTACT = [
    ("mayurdayal.engineer@gmail.com", "mailto:mayurdayal.engineer@gmail.com"),
    ("+91-9263912330", "tel:+919263912330"),
    ("Bengaluru, India (Open to Remote)", None),
]
LINKS = [
    ("linkedin.com/in/mayur-dayal", "https://linkedin.com/in/mayur-dayal/"),
    ("github.com/maadhav-codes", "https://github.com/maadhav-codes"),
]
EDUCATION = {
    "school": "Bengal College of Engineering & Technology",
    "dates": "Aug 2017 – Jul 2021",
    "degree": "B.Tech, Information Technology · CGPA 8.2/10",
}

# Shared role/date metadata ------------------------------------------------
BLACKBOX = ("BLACKBOX AI", "Full-Stack Engineer (Contract)", "Nov 2025 – Dec 2025")
PENIFY = ("Penify.dev", "Software Engineer (SDE-1 → SDE-2, promoted Feb 2025)", "Jul 2023 – Oct 2025")
FREELANCE = ("Independent Web Development (Remote Clients)", "Front-End / Full-Stack Developer", "Mar 2022 – Jun 2023")
ZINEDU = ("ZinEdu Classes Pvt. Ltd.", "Front-End Developer", "Aug 2021 – Feb 2022")

VOX = ("Ollama Vox — Local macOS Voice Assistant", "Apr 2026 – May 2026",
       "github.com/maadhav-codes/ollama-vox", "https://github.com/maadhav-codes/ollama-vox",
       "Python, PySide6/Qt, Ollama, MLX Whisper, Kokoro TTS, pytest")
D2C = ("diff2commit — AI-Powered Git Commit CLI", "Oct 2025 – Nov 2025",
       "github.com/maadhav-codes/diff2commit", "https://github.com/maadhav-codes/diff2commit",
       "Python, Git, Rich, Ollama, OpenAI-compatible APIs")

# ---------------------------------------------------------------------------
RESUMES = {
    "Frontend": {
        "headline": "Frontend Engineer | React, TypeScript, Next.js | SaaS Dashboards & AI Developer Tools",
        "summary": (
            "Frontend Engineer with 4+ years of experience building production React and TypeScript "
            "applications for SaaS and EdTech products. Built the customer dashboard, authentication flows, "
            "payment interfaces, and Next.js marketing site for a developer-tools SaaS (Penify.dev), and a "
            "real-time AI workspace with streaming chat, a code explorer, terminal logs, and live previews "
            "(BLACKBOX AI). Comfortable working into FastAPI and Node.js backends to ship complete features."
        ),
        "skills": [
            ("Languages", "TypeScript, JavaScript, HTML, CSS, Python, SQL"),
            ("Frontend", "React, Next.js, TanStack Query (React Query), Redux Toolkit, Zustand, Tailwind CSS, shadcn/ui"),
            ("UI Engineering", "Reusable components, responsive & mobile-first layouts, protected routing, streaming UIs"),
            ("APIs & Auth", "REST APIs, OAuth 2.0, JWT, Webhooks, Node.js, FastAPI"),
            ("Tools & Delivery", "Git, GitHub Actions (CI/CD), Vercel, Docker, Supabase"),
        ],
        "jobs": [
            (BLACKBOX, [
                "Built the workspace interface for an AI application-generation platform that streamed LLM responses and turned natural-language prompts into project files.",
                "Connected chat, a code explorer, terminal logs, and live application previews in one workspace, with real-time status for agent file generation and command execution.",
                "Wired one-step GitHub repository creation and Vercel production deployment into the workspace.",
            ]),
            (PENIFY, [
                "Developed the React/TypeScript dashboard and reusable components for repository management, documentation generation, job tracking, profiles, and API-key management.",
                "Implemented sign-up, password recovery, protected routes, and Google/GitHub OAuth authentication flows.",
                "Delivered payment-history, plan-upgrade, and coupon-redemption interfaces, plus Cashfree and PayPal checkout flows integrated with billing APIs.",
                "Built and maintained the responsive marketing website and product-tour pages with Next.js, TypeScript, and Tailwind CSS.",
                "As SDE-2, also built the FastAPI endpoints and GitHub App integrations behind dashboard features such as repository discovery, organization filtering, and usage analytics.",
            ]),
            (FREELANCE, [
                "Built 30+ responsive web interfaces from design specifications using semantic HTML, CSS, and JavaScript, with mobile-first layouts and cross-browser testing.",
                "Developed React applications with reusable components, routing, state management, and API integrations; owned requirements, feedback iterations, and deployment for each client.",
            ]),
            (ZINEDU, [
                "Developed React interfaces for an EdTech platform: role-based dashboards, access-controlled routes, and learning workflows for classes, assignments, exams, and performance analytics.",
                "Built admin interfaces for user management, attendance, and fee collection, with REST API integration and Excel/CSV/PDF reporting.",
            ]),
        ],
        "projects": [
            (VOX, ["Built a native Qt menu-bar app showing model health, responses, and per-stage latency, kept responsive by a three-worker background pipeline for on-device speech recognition, LLM inference, and text-to-speech."]),
            (D2C, ["Built an interactive CLI that generates Conventional Commit messages from staged diffs, with review, editing, and regeneration before committing."]),
        ],
    },

    "Backend": {
        "headline": "Backend Engineer | Python, FastAPI, PostgreSQL | APIs, Payments & LLM Integrations",
        "summary": (
            "Software Engineer with 4+ years of experience, focused on Python/FastAPI services for a "
            "developer-tools SaaS. Built payment and subscription logic (Cashfree, PayPal), GitHub App "
            "integrations, OAuth authentication, and documentation-generation workflows at Penify.dev, and "
            "LLM agent workflows that generate and run code in isolated sandboxes at BLACKBOX AI. Writes "
            "tested, concurrent Python and has full-stack depth in React and TypeScript."
        ),
        "skills": [
            ("Languages", "Python, TypeScript, JavaScript, SQL"),
            ("Backend & APIs", "FastAPI, Pydantic, Node.js, REST APIs, Webhooks, OAuth 2.0, JWT"),
            ("Data", "PostgreSQL, MongoDB, Redis, Supabase, Prisma ORM, Alembic"),
            ("AI & LLM", "OpenAI API, Gemini API, Ollama, agent workflows, streaming responses"),
            ("Testing & Delivery", "pytest, Docker, GitHub Actions (CI/CD), Git, Vercel, Vercel Sandboxes"),
            ("Frontend", "React, Next.js, Tailwind CSS"),
        ],
        "jobs": [
            (BLACKBOX, [
                "Built agent workflows for file generation, command execution, and status tracking, running LLM-generated projects inside isolated Vercel Sandboxes.",
                "Streamed LLM responses to clients and converted natural-language prompts into project files.",
                "Automated GitHub repository creation, sandbox-file synchronization, and Vercel production deployments; persisted project, conversation, execution, and deployment state in MongoDB.",
            ]),
            (PENIFY, [
                "Built and maintained FastAPI endpoints and service-layer logic for repository workflows, user accounts, analytics, and Git-provider integrations.",
                "Implemented Cashfree and PayPal checkout flows, transaction validation, and repository-based subscription eligibility, integrated with the billing dashboard.",
                "Built GitHub App integrations for repository discovery, organization filtering, usage analytics, and documentation-generation requests.",
                "Extended documentation-generation workflows with TypeDoc integration, changelog generation, multi-language support, and architecture documentation.",
                "As SDE-1, built the React/TypeScript dashboard and Google/GitHub OAuth authentication flows before taking on backend API ownership as SDE-2.",
            ]),
            (FREELANCE, [
                "Delivered custom web applications for remote clients, connecting React front ends to backend services and third-party APIs; owned requirements, testing, and deployment support.",
            ]),
            (ZINEDU, [
                "Built admin tools for an EdTech platform covering user management, attendance, and fee collection, with REST API, payment-workflow, and Excel/CSV/PDF reporting integrations.",
            ]),
        ],
        "projects": [
            (VOX, [
                "Designed a three-worker pipeline (speech recognition → LLM inference → text-to-speech) with bounded queues, cancellation, and configurable overflow handling, all running on-device.",
                "Wrote pytest suites covering audio, transcription, inference, speech synthesis, and pipeline behavior.",
            ]),
            (D2C, [
                "Built and packaged a Python CLI that generates Conventional Commit messages from staged diffs via local Ollama models or OpenAI-compatible endpoints.",
                "Added commit-message validation, diff-size limits, and staged-tree/HEAD consistency checks that block commits if repository state changes after review.",
            ]),
        ],
    },

    "Fullstack": {
        "headline": "Full-Stack Engineer | React, TypeScript, Python/FastAPI | AI Developer Tools",
        "summary": (
            "Full-Stack Engineer with 4+ years of experience building SaaS products end to end with React, "
            "TypeScript, and Python/FastAPI. At Penify.dev, owned features from dashboard UI to API, including "
            "payments, GitHub App integrations, OAuth, and documentation generation. At BLACKBOX AI, built an "
            "AI application-generation platform that takes a prompt all the way to a deployed app."
        ),
        "skills": [
            ("Languages", "TypeScript, JavaScript, Python, SQL, HTML, CSS"),
            ("Frontend", "React, Next.js, TanStack Query (React Query), Redux Toolkit, Zustand, Tailwind CSS, shadcn/ui"),
            ("Backend & APIs", "FastAPI, Node.js, Pydantic, REST APIs, OAuth 2.0, JWT, Webhooks, Prisma ORM, Alembic"),
            ("Databases", "PostgreSQL, MongoDB, Redis, Supabase"),
            ("AI & LLM", "OpenAI API, Gemini API, Ollama, agent workflows"),
            ("Testing & Delivery", "pytest, Docker, Git, GitHub Actions (CI/CD), Vercel, Vercel Sandboxes"),
        ],
        "jobs": [
            (BLACKBOX, [
                "Built an AI application-generation platform that streamed LLM responses and converted natural-language prompts into project files inside isolated Vercel Sandboxes.",
                "Implemented agent workflows for file generation, command execution, and status tracking, and connected chat, a code explorer, terminal logs, and live previews in one workspace.",
                "Automated GitHub repository creation, sandbox-file synchronization, and Vercel production deployments; persisted project, conversation, execution, and deployment state in MongoDB.",
            ]),
            (PENIFY, [
                "Built FastAPI endpoints and service-layer logic for repository workflows, user accounts, analytics, and Git-provider integrations.",
                "Implemented Cashfree and PayPal checkout, transaction validation, and repository-based subscription eligibility, plus the payment-history, plan-upgrade, and coupon-redemption UIs.",
                "Built GitHub App integrations for repository discovery, organization filtering, usage analytics, and documentation-generation requests.",
                "Developed the React/TypeScript dashboard and reusable components for repository management, documentation jobs, profiles, and API-key management, with Google/GitHub OAuth and protected routes.",
                "Extended documentation workflows with TypeDoc integration, changelog generation, and multi-language support; built the Next.js/Tailwind marketing site.",
            ]),
            (FREELANCE, [
                "Delivered custom websites and web apps for remote clients, from requirements through testing, feedback iterations, and deployment support.",
                "Built 30+ responsive interfaces from design specs, and React applications integrated with backend services and third-party APIs.",
            ]),
            (ZINEDU, [
                "Developed React interfaces for an EdTech platform, including role-based dashboards and admin tools for users, attendance, and fees, with REST API, payment, and Excel/CSV/PDF reporting integrations.",
            ]),
        ],
        "projects": [
            (VOX, [
                "Built a macOS menu-bar voice assistant with on-device speech recognition, LLM inference, and text-to-speech, using a three-worker pipeline with bounded queues and cancellation to keep the Qt UI responsive.",
            ]),
            (D2C, [
                "Built and packaged a Python CLI that writes Conventional Commit messages from staged diffs using local or remote LLMs, with validation and repository-state consistency checks.",
            ]),
        ],
    },

    "Forward_Deployed": {
        "headline": "Forward Deployed Engineer | LLM Applications, Integrations & End-to-End Delivery",
        "summary": (
            "Engineer with 4+ years of experience shipping production software end to end, including LLM "
            "applications, agent workflows, and third-party integrations (GitHub Apps, Vercel, payment "
            "gateways, OAuth). Spent 15 months as an independent developer working directly with clients, "
            "from scoping requirements through feedback iterations to deployment. Moves between React "
            "front ends, Python/FastAPI backends, and LLM APIs to get working systems into users' hands quickly."
        ),
        "skills": [
            ("AI & LLM", "OpenAI API, Gemini API, Ollama, agent workflows, streaming responses, on-device inference (MLX Whisper, Kokoro TTS)"),
            ("Integrations", "GitHub Apps, Vercel, OAuth 2.0, JWT, Webhooks, Cashfree, PayPal, REST APIs"),
            ("Backend & Data", "Python, FastAPI, Pydantic, Node.js, PostgreSQL, MongoDB, Redis, Supabase"),
            ("Frontend", "TypeScript, React, Next.js, Tailwind CSS"),
            ("Delivery", "Docker, GitHub Actions (CI/CD), Vercel Sandboxes, pytest, Git"),
        ],
        "jobs": [
            (BLACKBOX, [
                "Built an AI application-generation platform that turned natural-language prompts into running apps: streamed LLM output, generated project files, and executed commands in isolated Vercel Sandboxes.",
                "Implemented agent workflows with status tracking, surfaced through a unified workspace of chat, code explorer, terminal logs, and live previews.",
                "Automated the path to production: GitHub repository creation, sandbox-file sync, and Vercel deployments, with state persisted in MongoDB.",
            ]),
            (PENIFY, [
                "Integrated external platforms into the product: GitHub App integrations for repository discovery, organization filtering, usage analytics, and documentation-generation requests.",
                "Implemented Cashfree and PayPal checkout, transaction validation, and repository-based subscription eligibility across FastAPI services and the billing dashboard.",
                "Built FastAPI endpoints and service-layer logic for repository workflows, user accounts, analytics, and Git-provider integrations.",
                "Extended developer-documentation workflows with TypeDoc integration, changelog generation, multi-language support, and architecture documentation.",
                "Developed the React/TypeScript dashboard and Google/GitHub OAuth flows (SDE-1) before expanding into backend ownership (SDE-2).",
            ]),
            (FREELANCE, [
                "Worked directly with remote clients to scope requirements, build custom web applications, run feedback iterations, and support deployment.",
                "Integrated client applications with backend services and third-party APIs; delivered 30+ responsive interfaces from design specifications.",
            ]),
            (ZINEDU, [
                "Built role-based dashboards and admin tools for an EdTech platform, integrating REST APIs, payment workflows, and Excel/CSV/PDF reporting.",
            ]),
        ],
        "projects": [
            (VOX, [
                "Built a fully local voice assistant (speech recognition → LLM → text-to-speech) that keeps all voice processing on-device, with per-stage latency monitoring and pytest coverage across the pipeline.",
            ]),
            (D2C, [
                "Shipped a packaged CLI that works with local Ollama models or any OpenAI-compatible endpoint, with safety checks that block commits if repository state changes after review.",
            ]),
        ],
    },
}

CSS = """
@page { size: A4; margin: 10mm 13mm; }
* { box-sizing: border-box; }
body { font-family: Charter, Georgia, serif; font-size: 9.4pt; line-height: 1.3; color: #111; margin: 0; }
a { color: #1f3a68; text-decoration: none; }
h1 { font-size: 21pt; margin: 0; letter-spacing: .2px; }
.headline { font-size: 10.4pt; margin: 1px 0 2px; }
.contact { font-size: 9.2pt; }
.contact span + span::before { content: " | "; color: #555; }
h2 { font-size: 10.8pt; color: #1f3a68; border-bottom: 1px solid #1f3a68; margin: 8px 0 4px; padding-bottom: 1px; }
p { margin: 0; }
.skills div { margin: 0 0 1px; }
.row { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; }
.org { font-weight: bold; margin-top: 5px; }
.role { font-style: italic; font-weight: normal; }
.org .date { font-weight: normal; }
.date { white-space: nowrap; }
ul { margin: 1px 0 0; padding-left: 15px; }
li { margin: 0 0 1px; }
.tech { font-size: 9pt; }
"""


def e(s):
    return html.escape(s, quote=True)


def link(text, href):
    return f'<a href="{e(href)}">{e(text)}</a>' if href else e(text)


def bullets(items):
    return "<ul>" + "".join(f"<li>{e(b)}</li>" for b in items) + "</ul>"


def render(role, r):
    parts = [f"<h1>{e(NAME)}</h1>", f'<div class="headline">{e(r["headline"])}</div>']
    parts.append('<div class="contact">' + "".join(f"<span>{link(t, h)}</span>" for t, h in CONTACT) + "</div>")
    parts.append('<div class="contact">' + "".join(f"<span>{link(t, h)}</span>" for t, h in LINKS) + "</div>")
    parts.append(f"<h2>Summary</h2><p>{e(r['summary'])}</p>")
    parts.append("<h2>Skills</h2><div class='skills'>" + "".join(
        f"<div><b>{e(k)}:</b> {e(v)}</div>" for k, v in r["skills"]) + "</div>")
    parts.append("<h2>Experience</h2>")
    for (org, title, dates), items in r["jobs"]:
        parts.append(f'<div class="row org"><span>{e(org)} <span class="role">— {e(title)}</span></span>'
                     f'<span class="date">{e(dates)}</span></div>' + bullets(items))
    parts.append("<h2>Projects</h2>")
    for (name, dates, ltxt, lhref, tech), items in r["projects"]:
        parts.append(f'<div class="row org"><span>{e(name)} · {link(ltxt, lhref)}</span><span class="date" style="font-weight:normal">{e(dates)}</span></div>'
                     f'<div class="tech"><b>Tech:</b> {e(tech)}</div>' + bullets(items))
    ed = EDUCATION
    parts.append(f'<h2>Education</h2><div class="row"><span><b>{e(ed["school"])}</b> — {e(ed["degree"])}</span><span class="date">{e(ed["dates"])}</span></div>')
    title = f"{NAME} – {role.replace('_', ' ')} Resume"
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{e(title)}</title>'
            f"<style>{CSS}</style></head><body>{''.join(parts)}</body></html>")


def main():
    for role, r in RESUMES.items():
        stem = f"Mayur_Dayal_{role}_Resume"
        src = HERE / f"{stem}.html"
        src.write_text(render(role, r), encoding="utf-8")
        pdf = OUT / f"{stem}.pdf"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", src.as_uri()],
                       check=True, capture_output=True)
        pages = pdf.read_bytes().count(b"/Type /Page") - pdf.read_bytes().count(b"/Type /Pages")
        print(f"{pdf.name}: {pages} page(s)")


if __name__ == "__main__":
    main()
