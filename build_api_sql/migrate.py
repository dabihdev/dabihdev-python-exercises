# ================================================
# SCRIPT TO MIGRATE DATA FROM BOOK.JSON TO BOOK.DB
# ================================================

import json
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. SETUP DATABASE CONNECTION
# This must match the URL used in your revised main.py
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. DEFINE THE TABLE SCHEMA
# This needs to be identical to your backend model so the data lands in the right place
class BookTable(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)

def migrate_data():
    # Create the database and the 'books' table if they don't exist yet
    Base.metadata.create_all(bind=engine)
    
    # Check if the JSON file exists before trying to read it
    if not os.path.exists("books.json"):
        print("Error: books.json not found. Nothing to migrate.")
        return

    # 3. READ JSON DATA
    with open("books.json", "r") as f:
        books_data = json.load(f)

    # 4. INSERT INTO SQL DATABASE
    db = SessionLocal()
    try:
        print(f"Starting migration of {len(books_data)} books...")
        
        for item in books_data:
            # Create an instance of the SQL Model for each JSON entry
            new_book = BookTable(
                id=item["id"],
                title=item["title"],
                author=item["author"]
            )
            
            # Check if the ID already exists to avoid unique constraint errors
            existing = db.query(BookTable).filter(BookTable.id == item["id"]).first()
            if not existing:
                db.add(new_book)
                print(f"Added: {item['title']}")
            else:
                print(f"Skipped: ID {item['id']} already exists in database.")

        # Save all changes to the .db file
        db.commit()
        print("\nMigration complete! Your 'books.db' is ready.")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    migrate_data()