from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, UUID
from sqlalchemy.sql import func
from .connection import Base
import uuid

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID, primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Questionnaire(Base):
    __tablename__ = "questionnaires"

    questionnaire_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False) # e.g., 'phq-9'
    title = Column(String(255), nullable=False) # e.g., 'Patient Health Questionnaire-9'
    description = Column(Text)

class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, index=True)
    questionnaire_id = Column(Integer, ForeignKey("questionnaires.questionnaire_id"))
    question_text = Column(Text, nullable=False)
    question_order = Column(Integer, nullable=False)

class Response(Base):
    __tablename__ = "responses"

    response_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("users.user_id"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    session_id = Column(UUID, nullable=False, default=uuid.uuid4)
    answer_value = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Prediction(Base):
    __tablename__ = "predictions"

    prediction_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("users.user_id"))
    session_id = Column(UUID, nullable=False)
    questionnaire_id = Column(Integer, ForeignKey("questionnaires.questionnaire_id"))
    severity_label = Column(String(50), nullable=False)
    severity_score = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("users.user_id"))
    entry_text = Column(Text, nullable=False)
    sentiment_label = Column(String(50))
    sentiment_score = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Recommendation(Base):
    __tablename__ = "recommendations"

    recommendation_id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer, ForeignKey("predictions.prediction_id"))
    recommended_strategy = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())