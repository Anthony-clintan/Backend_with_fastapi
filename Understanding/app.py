from typing import Annotated, Union

from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: Annotated[Union[str,None], Query(
    alias="item_query",
    min_length=4,
    max_length=10,
    deprecated=True)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
