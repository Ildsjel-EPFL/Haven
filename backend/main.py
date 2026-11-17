from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_core.messages import HumanMessage

from utils.graph import graph
from utils.classes import ChatRequest, ChatResponse

app = FastAPI()

SUPPORTED_LANGUAGES = {
    "fr": "français",
    "de": "allemand",
    "it": "italien",
    "en": "anglais",
    "es": "espagnol",
    "pt": "portugais",
    "sq": "albanais",
    "tr": "turc",
    "ar": "arabe",
    "bs": "bosnien",
    "hr": "croate",
    "sr-Latn": "serbe en alphabet latin",
    "sr-Cyrl": "serbe en alphabet cyrillique",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    language = request.language if request.language in SUPPORTED_LANGUAGES else "fr"
    result = graph.invoke(
        {
            "messages": [HumanMessage(content=request.message)],
            "language": SUPPORTED_LANGUAGES[language],
        },
        config={
            "configurable": {
                "thread_id": request.session_id,
            }
        },
    )
    
    print(f'Situation: {result.get("situation")}\n')
    print(f'Conditions: {result.get("conditions")}')
    print(f"User ID: {request.session_id}")
    return ChatResponse(
        response=result.get("response", "Aucune réponse générée.")
    )