from typing import Annotated
from memes_api.crud import mem_crud
from memes_api.models import Mem
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi import UploadFile
from memes_api._minio import obj_img


class Memes(BaseModel):
    id: int
    description: str


app = FastAPI()


@app.get('/')
def main():
    return HTTPException(status_code=200, detail='OK')


@app.get('/memes')
def get_all_memes(memes_list: Annotated[Mem, Depends(mem_crud.get_all_mem)], page: int, per_page: int):
    total = len(memes_list)
    start = (page-1) * per_page
    end = start + per_page if start + per_page < total else total
    return memes_list[start:end]


@app.get('/memes/{id}')
def get_mem(current_mem: Annotated[Mem, Depends(mem_crud.get_mem)]):
    if not current_mem:
        raise HTTPException(status_code=404, detail="Mem not found")

    return {'current_mem': current_mem}


async def upload_file(photo: UploadFile):
    content = photo.file.read()
    with open('my_file.txt', 'wb') as binary_file:
        binary_file.write(content)

    return photo.size


@app.post('/memes')
async def set_mem(bytes: Annotated[int, Depends(upload_file)], mem: Annotated[Mem, Depends(mem_crud.set_mem)]):
    if not bytes:
        raise HTTPException(status_code=404, detail="Incorrect image")
    obj_img.set_image(mem.id)
    return {'id': mem.id,
            'description': mem.description,
            'bytes': bytes}


@app.put('/memes/{id}')
def update_mem(bytes: Annotated[int, Depends(upload_file)], mem_id: Annotated[int, Depends(mem_crud.update_mem)]):
    if not mem_crud.get_mem(mem_id):
        raise HTTPException(status_code=404, detail="Mem not found")
    obj_img.set_image(mem_id)
    return {'mem_id': mem_id, 'bytes': bytes}


@app.delete('/memes/{id}')
def delete_mem(mem_id: Annotated[int, Depends(mem_crud.delete_mem)]):
    obj_img.delete_image(mem_id)
    return mem_id

