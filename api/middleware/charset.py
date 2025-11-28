from fastapi import Request

async def add_charset_header(request: Request, call_next):
    """Middleware для добавления charset в заголовки"""
    response = await call_next(request)
    if response.headers.get("content-type", "").startswith("application/json"):
        response.headers["content-type"] = "application/json; charset=utf-8"

    return response