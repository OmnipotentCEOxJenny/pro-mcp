---
name: pro-mcp-check
description: Check that a local tool is really connected and working, and fix common problems in plain language. Use when a user asks whether their tool or MCP server is connected, why the assistant cannot see it, or why a call fails.
---

# Check a local tool

Follow `rules/scope.mdc`. Answer in the user's language.

1. **Is it running?** Open `http://127.0.0.1:7861/` in a browser (or the address the user chose). No page means the program is not running: start it again.
2. **Can the assistant see it?** List the tools. Expected: `sentiment_analysis` (or the user's tool names).
3. **Does it answer?** Call it with a test sentence, for example "I love learning for free!". Expected: a polarity above 0 and the assessment "positive". Report the numbers exactly.
4. **Quick self-test without the assistant:** `.venv/bin/python tests/test_sentiment_server.py` starts the example tool, lists it, calls it and stops it.
5. **Common fixes:**
   - Wrong address: current Gradio uses `/gradio_api/mcp/` (older guides show `/gradio_api/mcp/sse`).
   - Port busy: change `server_port` in `scripts/sentiment_server.py` and in `.cursor/mcp.json`.
   - Tool missing after editing settings: reload the assistant window.
   - Tool called over and over: ask the assistant to stop after one result.
6. Report: what you checked, what passed, what failed, and the next step. Anything not checked is UNVERIFIED.
