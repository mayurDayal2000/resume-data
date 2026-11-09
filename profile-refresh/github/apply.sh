#!/usr/bin/env bash
# Apply the GitHub profile changes to github.com/maadhav-codes.
# Prerequisite: gh logged in AS maadhav-codes:
#   gh auth login            (choose github.com, log in as maadhav-codes)
#   gh auth switch -u maadhav-codes   (if you have several accounts)
set -euo pipefail
cd "$(dirname "$0")"

OWNER=maadhav-codes
me=$(gh api user --jq .login)
if [[ "$me" != "$OWNER" ]]; then
  echo "gh is logged in as '$me', not '$OWNER'. Run: gh auth login  (or gh auth switch -u $OWNER)"; exit 1
fi

echo "1) Profile bio, location, website, hireable"
gh api -X PATCH user \
  -f bio="Full-stack engineer · React/TypeScript + Python/FastAPI · Building local-first AI tools" \
  -f location="Bengaluru, India" \
  -f blog="https://linkedin.com/in/mayur-dayal" \
  -F hireable=true >/dev/null

echo "2) Replace profile README (old copy saved to README.old.md)"
gh api "repos/$OWNER/$OWNER/contents/README.md" --jq .content | base64 -d > README.old.md
sha=$(gh api "repos/$OWNER/$OWNER/contents/README.md" --jq .sha)
gh api -X PUT "repos/$OWNER/$OWNER/contents/README.md" \
  -f message="Update profile README for full-stack role" \
  -f content="$(base64 < PROFILE_README.md | tr -d '\n')" \
  -f sha="$sha" >/dev/null

echo "3) Sharpen descriptions and topics on featured repos"
gh repo edit "$OWNER/ollama-vox" \
  --description "Privacy-first macOS menubar voice assistant: on-device speech recognition → local LLM → TTS on a cancellable three-worker pipeline." \
  --add-topic python,macos,voice-assistant,local-llm
gh repo edit "$OWNER/anime-ai-companion" \
  --description "Browser AI companion with token-streamed LLM chat, sentence-level TTS, Live2D expressions, and Gemini/Groq/Ollama providers. React 19 + TypeScript." \
  --add-topic react,typescript,vite,tailwindcss,llm,streaming,live2d,tts,ollama
gh repo edit "$OWNER/diff2commit" \
  --add-topic python,cli,git,conventional-commits,llm,ollama,developer-tools

echo "Done. Now do the manual steps in CHECKLIST.md (pinning has no API)."
