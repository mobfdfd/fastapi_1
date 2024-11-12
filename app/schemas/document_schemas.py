from pydantic import BaseModel
from typing import Optional


class DocumentUploadResponse(BaseModel):
    id: int


class DocumentDeleteResponse(BaseModel):
    message: str


class DocumentAnalyseResponse(BaseModel):
    message: str


class DocumentTextResponse(BaseModel):
    text: Optional[str] = None
