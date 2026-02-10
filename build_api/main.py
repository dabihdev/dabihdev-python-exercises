import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
DB_FILE = "books.json"

# This is the 'Template' for a book
class Book(BaseModel):
    id: int
    title: str
    author: str

# --- Helper Functions (The 'Waiters' fetching from the kitchen) ---

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- API Endpoints (The 'Menu' items) ---

@app.get("/books")
def get_all_books():
    """Returns every book in our JSON file"""
    return read_db()

@app.post("/books")
def add_book(book: Book):
    """Adds a new book to the JSON file"""
    books = read_db()
    books.append(book.__dict__) # Convert Python object to dictionary
    write_db(books)
    return {"message": "Book saved to JSON!", "data": book}

@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    """Finds one specific book by its ID"""
    books = read_db()
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Removes a book from the JSON file by its ID"""
    books = read_db()
    
    # Check if the book actually exists before trying to delete
    book_exists = any(book["id"] == book_id for book in books)
    
    if not book_exists:
        # This sends a clear 404 error back to the user
        raise HTTPException(status_code=404, detail="Book not found")

    # Create a new list that excludes the book with the matching ID
    updated_books = [book for book in books if book["id"] != book_id]
    
    # Save the new list back to the JSON file
    write_db(updated_books)
    
    return {"message": f"Book with ID {book_id} has been deleted."}