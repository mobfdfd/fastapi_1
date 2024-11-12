from app.celery.celery_app import celery
import pytesseract
from PIL import Image
from app.database.database import SessionLocal
from app.database.model import Documents, Documents_text


@celery.task
def analyze_doc(doc_id: int):
    global text
    db = SessionLocal()

    db_doc = db.query(Documents).filter(Documents.id == doc_id).first()

    if db_doc:
        text = pytesseract.image_to_string(Image.open(db_doc.path))

        db_text = Documents_text(id_doc=db_doc.id, text=text)
        db.add(db_text)

        db.commit()

    db.close()
    return f'{text}'
