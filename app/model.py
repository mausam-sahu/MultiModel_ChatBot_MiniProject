import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from app.schemas import AIResponse
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

parser = PydanticOutputParser(pydantic_object=AIResponse)

def build_llm(model_name:str) -> ChatGroq:
    return ChatGroq(
        model=model_name,
        temperature=0.1
    )

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system","{system_prompt}"),
        ("human","{human_prompt}"),
    ]
)

def generate_response(user_message:str,model_name:str):
    llm = build_llm(model_name)
    chain = PROMPT | llm | parser

    result = chain.invoke(
        {
            "system_prompt":("you are a helpful assistant who gives conscise and accurate answers.""Return a concise JSON response with summary, sentiment, and response."),
            "human_prompt":user_message + "\n" + parser.get_format_instructions(),
        }
    )

    return result.model_dump()