from collections import defaultdict
from datetime import datetime

events = [
    {"agent_id": "a1", "model": "gpt-x", "tokens": 1000, "cost_usd": 0.02, "ts": "2026-03-24T10:00:00"},
    {"agent_id": "a1", "model": "gpt-x", "tokens": 500, "cost_usd": 0.01, "ts": "2026-03-24T12:00:00"},
    {"agent_id": "a2", "model": "gpt-y", "tokens": 800, "cost_usd": 0.03, "ts": "2026-03-24T13:00:00"},
]

agg = defaultdict(float)

for event in events:
    day = datetime.fromisoformat(event["ts"]).date().isoformat()
    key = (event["agent_id"], day)
    agg[key] += event["cost_usd"]

result = [
    {"agent_id": agent_id, "day": day, "total_cost_usd": total}
    for (agent_id, day), total in agg.items()
]

print(result)