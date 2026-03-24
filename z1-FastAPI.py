"""
Нужно реализовать endpoint POST /metrics, который принимает событие метрики и сохраняет его. 
Требования:

валидация входных данных;
идемпотентность по event_id;
ответ 201 при новой записи и 200 при повторе.

"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

app = FastAPI()

# В реальности здесь БД
storage = {}

class MetricIn(BaseModel):
    event_id: str = Field(..., min_length=1)
    agent_id: str
    metric_name: Literal["latency_ms", "cost_usd", "error_rate"]
    value: float
    ts: datetime

@app.post("/metrics")
async def ingest_metric(metric: MetricIn):
    if metric.event_id in storage:
        return {
            "status": "duplicate",
            "event_id": metric.event_id
        }

    storage[metric.event_id] = metric.model_dump()
    return {
        "status": "created",
        "event_id": metric.event_id
    }

"""
уникальный индекс в PostgreSQL по event_id;
INSERT ... ON CONFLICT DO NOTHING/UPDATE;
correlation id;
batch ingestion;
асинхронную отправку в Kafka/очередь.
"""