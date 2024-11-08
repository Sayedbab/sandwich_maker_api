from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from api.models import OrderDetail
from api.models.schemas import OrderDetailCreate, OrderDetailUpdate

def create_order_detail(db: Session, order_detail: OrderDetailCreate):
    db_order_detail = OrderDetail(**order_detail.dict())
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read_order_details(db: Session, skip: int = 0, limit: int = 10):
    return db.query(OrderDetail).offset(skip).limit(limit).all()

def read_order_detail(db: Session, order_detail_id: int):
    db_order_detail = db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).first()
    if not db_order_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderDetail not found")
    return db_order_detail

def update_order_detail(db: Session, order_detail_id: int, order_detail: OrderDetailUpdate):
    db_order_detail = db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).first()
    if not db_order_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderDetail not found")
    for key, value in order_detail.dict(exclude_unset=True).items():
        setattr(db_order_detail, key, value)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def delete_order_detail(db: Session, order_detail_id: int):
    db_order_detail = db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).first()
    if not db_order_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderDetail not found")
    db.delete(db_order_detail)
    db.commit()
    return {"message": "OrderDetail deleted"}
