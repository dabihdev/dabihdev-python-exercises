import json
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str

book = Book(id=5, title="hey", author="JR")
print(book.__dict__)

with open("books2.json", 'r') as file:
    data = json.load(file)

with open("books2.json", 'w') as file:
    json.dump(book.__dict__, file)

