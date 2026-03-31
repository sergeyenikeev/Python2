import os
from getpass import getpass

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# 1) API key
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass("OpenAI API key: ")

# 2) Модель
llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.2,
)

# 3) Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Ты полезный Python-ассистент. Отвечай кратко и по делу."),
    ("human", "Объясни простыми словами: {topic}")
])

# 4) Цепочка: prompt -> model -> text
chain = prompt | llm | StrOutputParser()


# 5) Вызов
result = chain.invoke({"topic": "что такое декоратор в Python"})

print(result)