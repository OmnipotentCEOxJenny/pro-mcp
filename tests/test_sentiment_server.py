#!/usr/bin/env python3
"""Local end-to-end check: start scripts/sentiment_server.py, connect with the
official MCP Python client, list tools, call sentiment_analysis, stop the server.
Needs: gradio[mcp], textblob, mcp. Exit 0 = pass. This is a local test only;
it is NOT an in-app (Cursor/Grok) test."""
import asyncio, os, pathlib, subprocess, sys, time, urllib.request
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

root = pathlib.Path(__file__).resolve().parent.parent
port = os.environ.get("EASYMCP_PORT", "7871")
url = f"http://127.0.0.1:{port}/gradio_api/mcp/"
proc = subprocess.Popen([sys.executable, str(root / "scripts/sentiment_server.py")],
                        env={**os.environ, "EASYMCP_PORT": port},
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

async def run():
    async with streamablehttp_client(url) as (r, w, _):
        async with ClientSession(r, w) as s:
            await s.initialize()
            names = [t.name for t in (await s.list_tools()).tools]
            print("tools:", names)
            assert "sentiment_analysis" in names, "tool not listed"
            res = await s.call_tool("sentiment_analysis", {"text": "I love learning for free!"})
            out = " ".join(getattr(c, "text", "") for c in res.content)
            print("call result:", out)
            assert "positive" in out, "unexpected result"
try:
    for _ in range(60):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=1); break
        except Exception:
            time.sleep(1)
    asyncio.run(run())
    print("PASS: listed and called sentiment_analysis locally")
    rc = 0
except Exception as e:
    print("FAIL:", e); rc = 1
finally:
    proc.terminate(); proc.wait(timeout=10)
sys.exit(rc)
