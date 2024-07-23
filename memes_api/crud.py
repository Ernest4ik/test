from memes_api.database import Session, engine
from memes_api.models import Mem
from sqlalchemy import update, delete


class Memcrud:

    def __init__(self, db: Session):
        self.db = db

    def get_all_mem(self):
        list_mem = self.db.query(Mem).all()
        return list_mem

    def get_mem(self, id: int):
        current_mem = self.db.query(Mem).filter(Mem.id == id).first()
        return current_mem

    def set_mem(self, mem: str):
        current_mem = Mem(description=mem)
        self.db.add(current_mem)
        self.db.commit()
        return current_mem

    def update_mem(self, id: int, description: str):
        self.db.execute(update(Mem).where(id == Mem.id).values(description=description))
        self.db.commit()
        return id

    def delete_mem(self, id: int):
        self.db.execute(delete(Mem).where(id == Mem.id))
        self.db.commit()
        return id


mem_crud = Memcrud(Session(engine))
