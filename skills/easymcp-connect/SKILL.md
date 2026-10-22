---
name: easymcp-connect
description: Set up a small tool on the user's own computer and connect it to the AI assistant, step by step, in plain language. Use when someone wants their assistant to use a local program, an MCP server, or the example mood-checker (sentiment) tool.
---

# Connect a local tool

Follow `rules/pillars-and-scope.mdc`. Answer in the user's language and in plain words.

1. **Explain first (one or two sentences):** "A connector lets your assistant press a button on a small program that runs on your computer, and read the answer back. Nothing leaves your computer."
2. **Check what is there:** Python 3.10 or newer (`python3 --version`). If missing, point to https://www.python.org/downloads/ (free).
3. **Example tool (mood checker):** from the plugin folder run
   - `python3 -m venv .venv` then `.venv/bin/pip install "gradio[mcp]" textblob` (Windows: `.venv\Scripts\pip`)
   - `.venv/bin/python scripts/sentiment_server.py`
   - It listens only on this computer at `http://127.0.0.1:7861`. The tool address is `http://127.0.0.1:7861/gradio_api/mcp/`.
4. **Connect it:** add this to the project's `.cursor/mcp.json` (create the file if needed), then reload the assistant:
   ```json
   { "mcpServers": { "easymcp-sentiment": { "url": "http://127.0.0.1:7861/gradio_api/mcp/" } } }
   ```
5. **Check it (two ways):** run the `easymcp-check` skill: the tool `sentiment_analysis` must appear in the list, and a test sentence must return a score.
6. **Your own tool:** any Python function with a short docstring can be wrapped the same way (`gr.Interface(fn=...)` and `demo.launch(mcp_server=True, server_name="127.0.0.1")`). Show the user the function's code before running it.
7. **Stop it:** press Ctrl+C in the window that runs the tool. Remove the entry from `.cursor/mcp.json` to disconnect.

Never say "connected" or "working" until step 5 passed in this session.
