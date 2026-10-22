# Example: the ToolPal mood checker (real local run, 2026-10-22)

Run: `python tests/test_sentiment_server.py` on the builder's computer (local only, not in-app).

```
tools: ['sentiment_analysis']
call result: {'polarity': 0.5, 'subjectivity': 0.7, 'assessment': 'positive'}
PASS: listed and called sentiment_analysis locally
```

Plain-words reading: the sentence "I love learning for free!" sounds **moderately positive** (0.5 on a scale from -1 to 1) and is mostly opinion (0.7 on a scale from 0 to 1).
