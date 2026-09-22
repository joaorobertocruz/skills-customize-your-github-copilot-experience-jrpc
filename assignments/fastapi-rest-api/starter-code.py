from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Item(BaseModel):
    id: int
    title: str
    description: str = ""
    completed: bool = False


items = [
    Item(id=1, title="Learn FastAPI", description="Build a REST API", completed=False),
    Item(id=2, title="Write tests", description="Verify endpoints", completed=True),
]


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: Implement GET /items
# TODO: Implement POST /items
# TODO: Implement GET /items/{item_id}
# TODO: Implement PUT /items/{item_id}
# TODO: Implement DELETE /items/{item_id}
