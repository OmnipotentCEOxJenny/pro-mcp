# Pro MCP

Pro MCP helps your AI assistant use small programs that run on your own computer. Think of it as a friendly adapter: you have a handy little tool (for example, one that reads a sentence and tells you whether it sounds happy, upset or neutral), and Pro MCP shows you, step by step, how to plug that tool into your assistant so it can use it for you. Why would you want this? Your assistant becomes more useful, the work stays on your computer instead of going to someone else's server, and it costs nothing. Pro MCP comes with a ready-made mood checker so you can try it in a few minutes, and it explains every step in everyday words.

![Pro MCP logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-22: v1.0.0 built and pushed to GitHub. Local tests only: manifest valid JSON, skill and rule front matter valid (`tests/check_frontmatter.py`), and `tests/test_sentiment_server.py` started the example mood checker, listed its tool and got a real result through the official MCP Python client on this computer.

**Pending**
- Not tested inside Cursor or Grok yet (no in-app test has been done).
- Not submitted to the marketplace.
- Translated summaries are machine-made and not reviewed by native speakers.

**Uncertain**
- How each AI app shows or loads local tools may differ; the settings file shown here is Cursor's `.cursor/mcp.json`.

## Quick start
1. Install (see Installation) and make sure Python 3.10 or newer is on your computer.
2. Ask: "Help me connect the Pro MCP mood checker."
3. Then ask: "What's the mood of: I love learning for free!"

## Installation
Install from this repository: https://github.com/OmnipotentCEOxJenny/pro-mcp (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`). Free. No API keys, no accounts, no paid services. The example tool needs the free Python packages `gradio[mcp]` and `textblob`.

## Testing
1. `python3 tests/check_frontmatter.py` (needs PyYAML).
2. `python tests/test_sentiment_server.py` (needs `gradio[mcp]`, `textblob`, `mcp`). Expected: the tool `sentiment_analysis` is listed and the test sentence comes back "positive".
3. Compare with `examples/mood-checker.md`.

## Search keywords
ModelContextProtocol, LocalTools, ConnectTools, ToolCalling, gradio, SentimentAnalysis, MoodChecker, AiAssistant, BeginnerFriendly, StepByStep, SetupHelper, automation, RunsLocally, NoApiKey, ProMcp, JennyEcho, OmnipotentCeo, OmnipotentMedia, ToolConnector, McpClient, LocalServer, localhost, textblob, TextMood, SetupGuide, troubleshooting, ConnectionCheck, OpenSource, MitLicense, CursorPlugin, PythonFunctions, SelfHosted, McpSetup, McpJson, FriendlyAdapter, LocalPrograms, ToolTesting, PythonTools, SentimentTool, ExampleServer. The full list with plain-word meanings is in [keywords.md](keywords.md).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Modeled on the Gradio sentiment-analysis MCP server exercise in the free Hugging Face MCP Course (https://huggingface.co/learn/mcp-course). Pro MCP is independent and not endorsed by Hugging Face or Gradio.

## Components
- `skills/pro-mcp-connect`: set up and connect a local tool, step by step.
- `skills/pro-mcp-check`: confirm a tool is connected and fix common problems.
- `rules/scope.mdc`: the scope.
- `scripts/sentiment_server.py`: the example mood checker (local only, 127.0.0.1).
- `tests/`: front-matter check and local end-to-end test.
- `examples/mood-checker.md`: a real local run.
- `keywords.md`: the search keyword list.

## Languages
The AI answers in the user's language and keeps commands, file names and setting names unchanged. Summaries in 23 languages are in [TRANSLATIONS.md](TRANSLATIONS.md). They are machine translations, not yet reviewed by native speakers; the English text is authoritative. Each language section in TRANSLATIONS.md also starts with a one-line machine-translation notice in that language.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
- It has not been tested inside Cursor or Grok yet; only local tests on one computer have been run.
- It does not host tools on the internet; tools run only while your computer and the tool's window are on.
- The example mood checker is simple: it reads English best and can misjudge sarcasm or mixed feelings.
- You need Python and a few free packages; Pro MCP guides you but cannot install them without your permission.
- Marketplace: not submitted; it is not an approved listing.
- Translations are machine-made and not reviewed by native speakers.
- It is not legal or security advice; only connect tools you trust.
- Rules and compliance: it follows all local, county, state and federal laws and every platform's rules, uses no paid services, never bypasses logins or security settings, and never claims a feature it does not have.
