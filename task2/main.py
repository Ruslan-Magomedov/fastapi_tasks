from fastapi import FastAPI
import uvicorn

import booksDB
from models.book import Book


app = FastAPI()


@app.get("/books", summary="Получить все книги")
def get_books() -> list[dict]:
    return booksDB.data


@app.get("/books/{book_id}", summary="Получить книгу по id")
def get_book_byid(book_id: int) -> dict:
    for book in booksDB.data:
        if book["id"] == book_id:
            return book
    return {"status": 404, "message": "Not Found"}


@app.post("/books", summary="Добавить новую книгу")
def create_book(book_data: Book) -> dict:
    if book_data.title and book_data.text and book_data.author:
        temp = {
            "id": len(booksDB.data) + 1,
            "title": book_data.title,
            "text": book_data.text,
            "author": book_data.author
            }
        booksDB.data.append(temp)
        return temp
    return {"status": 400, "message": "Bad Request"}


@app.put("/books/{book_id}", summary="Изменить книгу по id")
def edit_book_byid(book_id: int, book_data: Book) -> dict:
    if book_data.title or book_data.text or book_data.author:
        for index, book in enumerate(booksDB.data):
            if book["id"] == book_id:
                if book_data.title:
                    booksDB.data[index]["title"] = book_data.title
                if book_data.text:
                    booksDB.data[index]["text"] = book_data.text
                if book_data.author:
                    booksDB.data[index]["author"] = book_data.author
                return book
        return {"status": 404, "message": "Not Found"}
    return {"status": 400, "message": "Bad Request"}


@app.delete("/books/{book_id}", summary="Удалить книгу по id")
def delete_book_byid(book_id: int) -> dict:
    for index, book in enumerate(booksDB.data):
        if book["id"] == book_id:
            booksDB.data.pop(index)
            return {"message": "Book deleted successfully"}
    return {"status": 404, "message": "Not Found"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
