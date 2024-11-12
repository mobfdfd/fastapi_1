from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base


class Documents(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    date = Column(DateTime, default=datetime.now)

    text = relationship("Documents_text", back_populates="document", uselist=False)  # Один к одному


class Documents_text(Base):
    __tablename__ = 'documents_text'

    id = Column(Integer, primary_key=True)
    id_doc = Column(Integer, ForeignKey("documents.id"))
    text = Column(String)

    # Связь обратно с документом
    document = relationship("Documents", back_populates="text")


