from fastapi import APIRouter
from .processing.router import router as processing_router


router = APIRouter()
router.include_router(processing_router, prefix="/processing", tags=["Processing"])
