from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from api.models import Resource
from api.models.schemas import ResourceCreate, ResourceUpdate

def create_resource(db: Session, resource: ResourceCreate):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def read_resources(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Resource).offset(skip).limit(limit).all()

def read_resource(db: Session, resource_id: int):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    return db_resource

def update_resource(db: Session, resource_id: int, resource: ResourceUpdate):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    for key, value in resource.dict(exclude_unset=True).items():
        setattr(db_resource, key, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def delete_resource(db: Session, resource_id: int):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return {"message": "Resource deleted"}
