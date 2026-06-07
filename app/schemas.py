from pydantic import BaseModel, Field


class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user's message")
    sentiment: int = Field(description="Sentiment score from 0 to 100")
    response: str = Field(description="Suggested response to the user")