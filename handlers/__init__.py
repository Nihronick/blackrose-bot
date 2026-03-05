from .content import router as content_router
from .errors import router as errors_router
from .helpers import router as helpers_router
from .menu import router as menu_router

__all__ = ["menu_router", "content_router", "helpers_router", "errors_router"]  # ✅ И это!
