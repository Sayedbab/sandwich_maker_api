from fastapi import FastAPI, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from api.dependencies.database import engine, get_db
from api.models import Base
from api.models.schemas import (
    SandwichCreate, SandwichUpdate, Sandwich,
    ResourceCreate, ResourceUpdate, Resource,
    RecipeCreate, RecipeUpdate, Recipe,
    OrderCreate, OrderUpdate, Order, OrderDetailCreate, OrderDetail, OrderDetailUpdate
)
from api.controllers.sandwiches import sandwiches
from api.controllers.resources import resources
from api.controllers.recipes import recipes
from api.controllers.orders import orders
from api.controllers.order_details import order_details
# Create the FastAPI app instance
app = FastAPI()

# Create the database tables if they do not exist
Base.metadata.create_all(bind=engine)

# Sandwiches Endpoints
@app.post("/sandwiches/", response_model=Sandwich, tags=["sandwiches"])
def create_sandwich(sandwich: SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)

@app.get("/sandwiches/", response_model=list[Sandwich], tags=["sandwiches"])
def read_sandwiches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return sandwiches.read_all(db=db, skip=skip, limit=limit)

@app.get("/sandwiches/{sandwich_id}", response_model=Sandwich, tags=["sandwiches"])
def read_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwiches.read_one(db=db, sandwich_id=sandwich_id)

@app.put("/sandwiches/{sandwich_id}", response_model=Sandwich, tags=["sandwiches"])
def update_sandwich(sandwich_id: int, sandwich: SandwichUpdate, db: Session = Depends(get_db)):
    return sandwiches.update(db=db, sandwich_id=sandwich_id, sandwich=sandwich)

@app.delete("/sandwiches/{sandwich_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["sandwiches"])
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)

# Resources Endpoints
@app.post("/resources/", response_model=Resource, tags=["resources"])
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)

@app.get("/resources/", response_model=list[Resource], tags=["resources"])
def read_resources(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return resources.read_all(db=db, skip=skip, limit=limit)

@app.get("/resources/{resource_id}", response_model=Resource, tags=["resources"])
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.read_one(db=db, resource_id=resource_id)

@app.put("/resources/{resource_id}", response_model=Resource, tags=["resources"])
def update_resource(resource_id: int, resource: ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update(db=db, resource_id=resource_id, resource=resource)

@app.delete("/resources/{resource_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["resources"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.delete(db=db, resource_id=resource_id)

# Recipes Endpoints
@app.post("/recipes/", response_model=Recipe, tags=["recipes"])
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipe=recipe)

@app.get("/recipes/", response_model=list[Recipe], tags=["recipes"])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return recipes.read_all(db=db, skip=skip, limit=limit)

@app.get("/recipes/{recipe_id}", response_model=Recipe, tags=["recipes"])
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipes.read_one(db=db, recipe_id=recipe_id)

@app.put("/recipes/{recipe_id}", response_model=Recipe, tags=["recipes"])
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):
    return recipes.update(db=db, recipe_id=recipe_id, recipe=recipe)

@app.delete("/recipes/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["recipes"])
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipes.delete(db=db, recipe_id=recipe_id)

# Orders Endpoints
@app.post("/orders/", response_model=Order, tags=["orders"])
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)

@app.get("/orders/", response_model=list[Order], tags=["orders"])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return orders.read_all(db=db, skip=skip, limit=limit)

@app.get("/orders/{order_id}", response_model=Order, tags=["orders"])
def read_order(order_id: int, db: Session = Depends(get_db)):
    return orders.read_one(db=db, order_id=order_id)

@app.put("/orders/{order_id}", response_model=Order, tags=["orders"])
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    return orders.update(db=db, order_id=order_id, order=order)

@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["orders"])
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return orders.delete(db=db, order_id=order_id)

# Order Details Endpoints
@app.post("/order_details/", response_model=OrderDetail, tags=["order_details"])
def create_order_detail(order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_detail=order_detail)

@app.get("/order_details/", response_model=list[OrderDetail], tags=["order_details"])
def read_order_details(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return order_details.read_all(db=db, skip=skip, limit=limit)

@app.get("/order_details/{order_detail_id}", response_model=OrderDetail, tags=["order_details"])
def read_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return order_details.read_one(db=db, order_detail_id=order_detail_id)

@app.put("/order_details/{order_detail_id}", response_model=OrderDetail, tags=["order_details"])
def update_order_detail(order_detail_id: int, order_detail: OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details.update(db=db, order_detail_id=order_detail_id, order_detail=order_detail)

@app.delete("/order_details/{order_detail_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["order_details"])
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return order_details.delete(db=db, order_detail_id=order_detail_id)
