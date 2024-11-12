from fastapi import APIRouter, HTTPException, UploadFile
from app.celery.tasks import analyze_doc
from app.database.database import SessionLocal
from app.database.model import Documents, Documents_text
from app.schemas.document_schemas import DocumentAnalyseResponse, DocumentTextResponse, DocumentUploadResponse, DocumentDeleteResponse
import os


router = APIRouter()
UPLOAD_FOLDER = "documents"


@router.post("/upload_doc", response_model=DocumentUploadResponse)
async def upload_doc(file: UploadFile):

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_content = await file.read()
    filename = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(filename, "wb") as f:
        f.write(file_content)

    db = SessionLocal()
    db_doc = Documents(path=filename)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    db.close()

    return DocumentUploadResponse(id=db_doc.id)


@router.delete("/doc_delete/{doc_id}", response_model=DocumentDeleteResponse)
def delete_doc(doc_id: int):
    db = SessionLocal()

    db_text = db.query(Documents_text).filter(Documents_text.id_doc == doc_id).first()
    if db_text:
        db.delete(db_text)

    db_doc = db.query(Documents).filter(Documents.id == doc_id).first()
    if not db_doc:
        raise HTTPException(status_code=404, detail="Document not found")

    os.remove(db_doc.path)
    db.delete(db_doc)
    db.commit()

    return DocumentDeleteResponse(message="Document deleted successfully")

