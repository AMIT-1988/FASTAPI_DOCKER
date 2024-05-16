from typing import Union
from fastapi import APIRouter
router=APIRouter()


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = 'amit'):
    return {"item_id": item_id, "q": q}

@router.get("/mainuser")
async def read_user():
    return{"mainuser_name":"pierre",}
