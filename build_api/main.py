import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field # Add Field here
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# without this, the computer will not allow the front-end to communicate
# with the back-end. It regards it as a different server and thinks it wants
# to attack you.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (fine for local dev)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],
)

DB_FILE = "books.json"

# This is the 'Template' for a book
""" class Book(BaseModel):
    id: int
    title: str
    author: str """

class Book(BaseModel):
    # ID must be greater than 0
    id: int = Field(gt=0, msg="The ID must be a positive integer")

    # Title must be between 1 and 100 characters
    title: str = Field(min_length=1, max_length=100)

    # Author cannot be empty
    author: str #= Field(min_length=2, max_length=50)

# --- Helper Functions (The 'Waiters' fetching from the kitchen) ---

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- API Endpoints (The 'Menu' items) ---

@app.get("/books")
def get_all_books(author: Optional[str] = None):
    """Returns every book in our JSON file"""
    # read db books
    books = read_db()

    # if optional parameter author is given,
    # filter results
    if author:
        filtered_books = [book for book in books if book['author'].lower() == author.lower()]
        return filtered_books
    
    # otherwise return all the books
    return books


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

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    """Updates an existing book in the JSON file"""
    books = read_db()

    # Look for the book index (its position in the list)
    for index, book in enumerate(books):
        if book["id"] == book_id:
            # We found it! Now we replace the old data with the new data
            # .dict() converts the Pydantic object into a JSON-friendly dictionary
            books[index] = updated_book.__dict__
            write_db(books)
            return {"message": "Book updated!", "data": updated_book}

    # If the loop finishes without finding the ID
    raise HTTPException(status_code=404, detail="Book not found to update")
