from fastapi import FastAPI
from fastapi import Form
from src import item_list
import asyncio

app = FastAPI()


@app.get("/items/{item_id}")
async def foo(item_id):
    try:
        item = item_list.item_names[int(item_id)]
        return {"item": item}

    except:
        return {"item": "item doesn't exits"}


@app.post("/items/create")
async def bar(item_name: str = Form()):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, item_list.add_item, item_name)
    return {"status": f"added {item_name}"}


@app.put("/items/create")
async def foobar(item_name: str = Form()):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, item_list.add_item, item_name)
    return {"status": f"added {item_name}"}


@app.delete("/items/{item_id}")
async def baz(item_id):
    try:
        item_list.delete_item(int(item_id))
        return {"message": f"succefull deleted {item_id}"}
    except Exception as e:
        return {
            "message": f"failed to delete {item_id}",
            "exeption": str(e)
                }
