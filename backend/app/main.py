from fastapi import FastAPI

from app.api.routes.runs import router as runs_router
from app.api.routes.tasks import router as tasks_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="DecisionGraph MVP API for orchestrating research workflows.",
)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "app": settings.app_name}


app.include_router(tasks_router, prefix=settings.api_prefix)
app.include_router(runs_router, prefix=settings.api_prefix)
