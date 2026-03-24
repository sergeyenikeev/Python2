"""
Нужно прочитать сообщения из Kafka, обработать, записать в БД и только после этого закоммитить offset.
"""

import json

class FakeConsumer:
    def __iter__(self):
        yield {"offset": 1, "value": json.dumps({"event_id": "e1", "value": 42})}
        yield {"offset": 2, "value": json.dumps({"event_id": "e2", "value": 43})}

    def commit(self):
        print("offset committed")

processed = set()

def save_to_db(event: dict):
    if event["event_id"] in processed:
        return
    processed.add(event["event_id"])

consumer = FakeConsumer()

for msg in consumer:
    event = json.loads(msg["value"])
    try:
        save_to_db(event)
        consumer.commit()
    except Exception as e:
        print(f"processing failed: {e}")

