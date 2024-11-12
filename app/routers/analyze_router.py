from fastapi import APIRouter, HTTPException, UploadFile
from app.celery.tasks import analyze_doc
from app.database.database import SessionLocal
from app.database.model import Documents, Documents_text
from app.schemas.document_schemas import DocumentAnalyseResponse, DocumentTextResponse, DocumentUploadResponse, \
    DocumentDeleteResponse
import os

router = APIRouter()
UPLOAD_FOLDER = "documents"


@router.post("/doc_analyse/{doc_id}", response_model=DocumentAnalyseResponse)
async def doc_analyse(doc_id: int):
    db = SessionLocal()
    db_doc = db.query(Documents).filter(Documents.id == doc_id).first()
    if not db_doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return DocumentAnalyseResponse(message=f'{analyze_doc.delay(doc_id)}')


@router.get("/get_text/{doc_id}", response_model=DocumentTextResponse)
async def get_text(doc_id: int):
    db = SessionLocal()
    db_text = db.query(Documents_text).filter(Documents_text.id_doc == doc_id).first()
    if not db_text:
        raise HTTPException(status_code=404, detail="Text for the document not found")

    return DocumentTextResponse(text=db_text.text)
