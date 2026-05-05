from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Book(BaseModel):
    name: str
    seller: str
    price: int

class BookResponse(BaseModel):
    name: str
    price: int

inventory = {
    "Book1": {
        "name" : "The Pyschology of Money",
        "seller" : "Nostalgica",
        "price" : 200
    },
    "Book2": {
        "name" : "The Wave Rider",
        "seller" : "Satyam Wholesales",
        "price" : 450
    },
}

app = FastAPI()

@app.get('/get-books/{BookId}', response_model = BookResponse)
def get_books(BookId: str):
    for i in inventory.keys():
        if BookId == i:
            return inventory[BookId]
    raise HTTPException(
        status_code= 404,
        detail = "Not Found"
    )

@app.post('/store-book/{BookId}', response_model=BookResponse)
def create_book(book: Book, BookId: str):
    if BookId not in inventory:
        inventory[BookId] = book
        return inventory[BookId]
    else:
        raise HTTPException(
            status_code= 409,
            detail= "Resource already exists."
        )