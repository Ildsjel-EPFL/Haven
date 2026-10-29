from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_core.messages import HumanMessage

from utils.graph import graph
from utils.classes import ChatRequest, ChatResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest) -> ChatResponse:
#     result = graph.invoke(
#         {
#             "messages": [HumanMessage(content=request.message)],
#         }
#     )

#     return ChatResponse(
#         response=str(result.get("response", "Aucune réponse générée."))
#     )
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    result = graph.invoke(
        {
            "messages": [HumanMessage(content=request.message)],
        },
        config={
            "configurable": {
                "thread_id": "default-chat",
            }
        },
    )

    return ChatResponse(
        response=result.get("response", "Aucune réponse générée.")
    )