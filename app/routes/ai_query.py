import sqlite3
from fastapi import APIRouter, HTTPException
from langchain_ollama import ChatOllama
from pydantic import BaseModel

app = APIRouter(prefix="/ai", tags=["AI Query"])
llm = ChatOllama(model="llama3.2", temperature=0)

class Ask_query(BaseModel):
    que: str

@app.post("/query")
def ai_query(query: Ask_query):
    conn = None
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        col_name = [
            description[0]
            for description in cursor.description
        ]

        context = (f"Column names: {', '.join(col_name)}\n"f"Data: {data}\n"
        )

        prompt = f"""
You are a school assistant.
Use the following students table data to answer the question.
If the answer is not available in the data, say so.
{context}
User question: {query.que}
"""
        response = llm.invoke(prompt)
        return {"question": query.que,"answer": response.content}

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    finally:
        if conn is not None:
            conn.close()
