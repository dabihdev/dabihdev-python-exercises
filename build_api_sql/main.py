from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# --- SQLALCHEMY SETUP ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- SQL DATABASE MODEL ---
# This defines how the table looks in the actual .db file
class BookTable(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)

# Create the database file and tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (Unchanged)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- PYDANTIC MODEL ---
# This defines how the data looks in the API (JSON)
class BookSchema(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=100)
    author: str

    class Config:
        from_attributes = True

# --- DEPENDENCY ---
# This opens a connection to the DB for each request and closes it after
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API ENDPOINTS ---

@app.get("/books") # get all
def get_all_books(author: str = None, db: Session = Depends(get_db)):
    query = db.query(BookTable)
    if author:
        # SQL-style filtering
        return query.filter(BookTable.author.ilike(f"%{author}%")).all()
    return query.all()

@app.post("/books")
def add_book(book: BookSchema, db: Session = Depends(get_db)):
    # Check if ID exists (SQL databases usually handle auto-incrementing, 
    # but we will keep your custom ID logic for now)
    db_book = BookTable(id=book.id, title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book) # SQLAlchemy often "expires" the data held in your local Python object (db_book) because it assumes the database might have changed things during the save process.
    # db.expire(db_book)
    # print(db_book.__dict__)
    return db_book

@app.get("/books/{book_id}")
def get_single_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookTable).filter(BookTable.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookTable).filter(BookTable.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": f"Book {book_id} deleted"}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: BookSchema, db: Session = Depends(get_db)):
    db_book = db.query(BookTable).filter(BookTable.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db_book.title = updated_book.title
    db_book.author = updated_book.author
    db.commit()
    db.refresh(db_book)
    return db_book