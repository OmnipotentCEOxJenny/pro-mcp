# Easy MCP

Easy MCP helps your AI assistant use small programs that run on your own computer. Think of it as a friendly adapter: you have a handy little tool (for example, one that reads a sentence and tells you whether it sounds happy, upset or neutral), and Easy MCP shows you, step by step, how to plug that tool into your assistant so it can use it for you. Why would you want this? Your assistant becomes more useful, the work stays on your computer instead of going to someone else's server, and it costs nothing. Easy MCP comes with a ready-made mood checker so you can try it in a few minutes, and it explains every step in everyday words.

![Easy MCP logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-22: v1.0.0 built. Local tests only: manifest valid JSON, skill and rule front matter valid (`tests/check_frontmatter.py`), and `tests/test_sentiment_server.py` started the example mood checker, listed its tool and got a real result through the official MCP Python client on this computer.

**Pending**
- Not tested inside Cursor or Grok yet (no in-app test has been done).
- Not submitted to the marketplace.
- Translated summaries are machine-made and not reviewed by native speakers.

**Uncertain**
- How each AI app shows or loads local tools may differ; the settings file shown here is Cursor's `.cursor/mcp.json`.

## Quick start
1. Install (see Installation) and make sure Python 3.10 or newer is on your computer.
2. Ask: "Help me connect the Easy MCP mood checker."
3. Then ask: "What's the mood of: I love learning for free!"

## Installation
Install from this repository: https://github.com/OmnipotentCEOxJenny/easymcp (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`). Free. No API keys, no accounts, no paid services. The example tool needs the free Python packages `gradio[mcp]` and `textblob`.

## Testing
1. `python3 tests/check_frontmatter.py` (needs PyYAML).
2. `python tests/test_sentiment_server.py` (needs `gradio[mcp]`, `textblob`, `mcp`). Expected: the tool `sentiment_analysis` is listed and the test sentence comes back "positive".
3. Compare with `examples/mood-checker.md`.

## Search keywords
mcp, mcp-server, model-context-protocol, local-tools, connect-tools, tool-calling, gradio, sentiment-analysis, mood-checker, ai-assistant, beginner-friendly, step-by-step, setup-helper, automation, python, privacy, runs-locally, free, no-api-key, multilingual. The full list with plain-word meanings is in [keywords.md](keywords.md).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Modeled on the Gradio sentiment-analysis MCP server exercise in the free Hugging Face MCP Course (https://huggingface.co/learn/mcp-course). Easy MCP is independent and not endorsed by Hugging Face or Gradio.

## Rob Domaine's four pillars
1. Trustworthy, honest, real data, truthful: never claim a tool works until it has been seen working; report results exactly.
2. Use only legitimate means: only tools you own or trust, free and local by default.
3. Double-check everything: every connection is confirmed two ways (tool listed, test call answered).
4. Stay within the law and rules always: local, county, state, federal and platform rules.

## Components
- `skills/easymcp-connect`: set up and connect a local tool, step by step.
- `skills/easymcp-check`: confirm a tool is connected and fix common problems.
- `rules/pillars-and-scope.mdc`: the pillars and scope.
- `scripts/sentiment_server.py`: the example mood checker (local only, 127.0.0.1).
- `tests/`: front-matter check and local end-to-end test.
- `examples/mood-checker.md`: a real local run.
- `keywords.md`: the search keyword list.

## Languages
The AI answers in the user's language and keeps commands, file names and setting names unchanged. Summaries in 23 languages are in [TRANSLATIONS.md](TRANSLATIONS.md). They are machine translations, not yet reviewed by native speakers; the English text is authoritative.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
- It has not been tested inside Cursor or Grok yet; only local tests on one computer have been run.
- It does not host tools on the internet; tools run only while your computer and the tool's window are on.
- The example mood checker is simple: it reads English best and can misjudge sarcasm or mixed feelings.
- You need Python and a few free packages; Easy MCP guides you but cannot install them without your permission.
- Marketplace: not submitted; it is not an approved listing.
- Translations are machine-made and not reviewed by native speakers.
- It is not legal or security advice; only connect tools you trust.
- Rules and compliance: it follows all local, county, state and federal laws and every platform's rules, uses no paid services, never bypasses logins or security settings, and never claims a feature it does not have.
