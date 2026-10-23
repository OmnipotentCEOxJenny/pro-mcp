# Changelog

## 1.0.2 (2026-10-23)
- Translations: each language section in TRANSLATIONS.md now starts with a one-line notice in that language saying it is a machine translation, not reviewed by a native speaker, and that the English version is authoritative. README Languages section notes this. No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.1 (2026-10-23)
- Search keywords: 32 to 40 (added McpSetup, McpJson, FriendlyAdapter, LocalPrograms, ToolTesting, PythonTools, SentimentTool, ExampleServer); plugin-name keyword ProMCP written as ProMcp (PascalCase). `keywords.md` and the README keyword line were out of date (old hyphenated list of 38) and now match the manifest exactly.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.0 (2026-10-22)
- Name history: first built as "ToolPal" (an early copy was pushed by accident to github.com/OmnipotentCEOxJenny/toolpal, which is not this plugin's home), then "Easy MCP", final name "Pro MCP" chosen by Rob. Repository github.com/OmnipotentCEOxJenny/pro-mcp created and pushed 2026-10-22. 38 search keywords. Logo: plug and toolbox.
- First version: skills `pro-mcp-connect` and `pro-mcp-check`, rule `pillars-and-scope.mdc`, example local mood checker `scripts/sentiment_server.py` (modeled on the Hugging Face MCP Course Gradio exercise), plain-language README, 38 search keywords in the manifest plus `keywords.md`, 23 machine-translated summaries.
- Tests: `tests/check_frontmatter.py` and local end-to-end `tests/test_sentiment_server.py`. Local only; not tested in-app. Not submitted to the marketplace.
