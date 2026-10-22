"""Pro MCP example tool: a free, local mood checker (sentiment analysis).
Modeled on the Gradio MCP server exercise in the Hugging Face MCP course.
Runs only on this computer (127.0.0.1). Requires: pip install "gradio[mcp]" textblob"""
import gradio as gr
from textblob import TextBlob


def sentiment_analysis(text: str) -> dict:
    """Analyze the sentiment (mood) of the given text.

    Args:
        text: The text to analyze

    Returns:
        dict with polarity (-1 negative to 1 positive), subjectivity (0 factual to 1 opinion) and assessment
    """
    s = TextBlob(text).sentiment
    return {
        "polarity": round(s.polarity, 2),
        "subjectivity": round(s.subjectivity, 2),
        "assessment": "positive" if s.polarity > 0 else "negative" if s.polarity < 0 else "neutral",
    }


demo = gr.Interface(fn=sentiment_analysis, inputs=gr.Textbox(), outputs=gr.JSON(),
                    title="Pro MCP mood checker (local)")

if __name__ == "__main__":
    import os
    demo.launch(mcp_server=True, server_name="127.0.0.1", server_port=int(os.environ.get("PRO_MCP_PORT", "7861")))
