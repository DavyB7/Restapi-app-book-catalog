from fastapi import FastAPI
from .database import Base, engine
from app.routers import users, authors, books, business

Base.metadata.create_all(bind=engine)
app = FastAPI(
    #lifespan=lifespan,  # Uncomment if you need to create tables on app start
    title="Моя библиотека",
    description="Простейшая библиотека, основанная на "
                "фреймворке FastAPI.",
    version="0.0.1",
    contact={
        "name": "Деви Боджона",
        "email": "devibodjona@yandex.ru",
    }

)

app.include_router(users.router)
app.include_router(authors.router)
app.include_router(books.router)
app.include_router(business.router)

@app.get("/")
def root():
    return {"message": "Book Catalog API"}