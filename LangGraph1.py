from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


# Общее состояние графа
class State(TypedDict):
    text: str
    result: str


# Узел 1: нормализуем строку
def normalize_text(state: State):
    print(11)

    return {
        "text": state["text"].strip().lower()
    }


# Узел 2: формируем итог
def build_result(state: State):
    print(12)
    return {
        "result": f"Готово: {state['text']}"
    }


print(1)
# Собираем граф
builder = StateGraph(State)

builder.add_node("normalize", normalize_text)
builder.add_node("finish", build_result)

builder.add_edge(START, "normalize")
builder.add_edge("normalize", "finish")
builder.add_edge("finish", END)

print(2)

graph = builder.compile()
print(3)

# Запуск
output = graph.invoke({
    "text": "   PRIVET, LANGGRAPH!   ",
    "result": ""
})
print(4)


print(output)
print(output["result"])