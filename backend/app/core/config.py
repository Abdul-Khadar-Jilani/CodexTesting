from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DecisionGraph API"
    api_prefix: str = "/api"
    environment: Literal["dev", "test", "prod"] = "dev"

    supabase_url: str | None = None
    supabase_key: str | None = None

    groq_api_key: str | None = None
    gemini_api_key: str | None = None

    planner_model: str = Field(default="groq:llama-3.1-8b-instant")
    research_model: str = Field(default="groq:mixtral-8x7b-32768")
    critic_model: str = Field(default="groq:llama-3.1-70b-versatile")
    synthesis_model: str = Field(default="gemini:gemini-1.5-pro")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
