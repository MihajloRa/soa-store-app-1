from fastapi import FastAPI,status,HTTPException
from typing import Optional, List
from db.database import SessionLocal
from db.models import  ProductDTO, Product


db=SessionLocal()

#Items 
@app.get('/productss', response_model=List[Product], status_code=200)
def get_all_items():
    items=db.query(Product).all()
    return items

@app.get('/products/{product_id}',response_model=ProductDTO,status_code=status.HTTP_200_OK)
def get_an_iem(product_id:int):
    item=db.query(Product).filter(Product.id==product.name).first()
    return item

@app.post('/products',response_model=ProductDTO, status_code=status.HTTP_201_CREATED)
def create_an_item(product:ProductDTO):
    db_item=db.query(Product).filter(Product.name==item.name).first()
    if db_item is not None :
        raise HTTPException(status_code=400,detail="ProductDTO already exists")

    new_item=Product(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )
    db.add(new_item)
    db.commit()

    return new_item

@app.delete('/products/{product_id}')
def delete_item(product_id:int):
    item_to_delete=db.query(Product).filter(Product.id==product_id).first()
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource not found")
    db.delete(item_to_delete)
    db.commit()
    return item_to_delete

@app.put('/products/{product_name}',response_model=ProductDTO,status_code=status.HTTP_200_OK)
def update_item(product_name:,product:ProductDTO):
    item_to_update=db.query(Product).filter(Product.name==product.name).first()
    item_to_update.name=product.name
    item_to_update.price=product.price
    item_to_update.description=product.description
    item_to_update.on_offer=product.on_offer

    db.commit()
    return item_to_update
 