from app.core.config import get_settings


class SupabaseClient:
    def __init__(self) -> None:
        settings = get_settings()
        self.url = settings.supabase_url
        self.key = settings.supabase_key

    @property
    def configured(self) -> bool:
        return bool(self.url and self.key)
