from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from api.models import Recipe
from api.models.schemas import RecipeCreate, RecipeUpdate

def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Recipe).offset(skip).limit(limit).all()

def read_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return db_recipe

def update_recipe(db: Session, recipe_id: int, recipe: RecipeUpdate):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    for key, value in recipe.dict(exclude_unset=True).items():
        setattr(db_recipe, key, value)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    db.delete(db_recipe)
    db.commit()
    return {"message": "Recipe deleted"}
