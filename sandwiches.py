from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from api.models import Sandwich
from api.models.schemas import SandwichCreate, SandwichUpdate

def create_sandwich(db: Session, sandwich: SandwichCreate):
    db_sandwich = Sandwich(**sandwich.dict())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_sandwiches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sandwich).offset(skip).limit(limit).all()

def read_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    return db_sandwich

def update_sandwich(db: Session, sandwich_id: int, sandwich: SandwichUpdate):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    for key, value in sandwich.dict(exclude_unset=True).items():
        setattr(db_sandwich, key, value)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    db.delete(db_sandwich)
    db.commit()
    return {"message": "Sandwich deleted"}
