from models import Question
from sqlalchemy.orm import Session

def get_question_list(db: Session):
    qestion_list = db.query(Question)\
    .order_by(Question.create_date.desc())\
    .all()
    return qestion_list


