from fastapi import APIRouter
from .auth.router import router as auth_router
from .perfil.router import router as perfil_router


router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(perfil_router, prefix="/perfil", tags=["Auth"])