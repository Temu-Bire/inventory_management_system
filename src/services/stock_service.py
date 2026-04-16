from src.repositories.stock_repository import StockRepository
from fastapi import HTTPException

class StockService:

    def __init__(self):
        self.repo = StockRepository()

    async def create_stock(self, db, data):
        return await self.repo.create(db, data)

    async def get_stock(self, db):
        return await self.repo.get_all(db)

    async def get_stock_by_id(self, db, stock_id):
        stock = await self.repo.get_by_id(db, stock_id)

        if not stock:
            raise HTTPException(404, "Stock not found")

        return stock

    async def delete_stock(self, db, stock_id):
        stock = await self.repo.get_by_id(db, stock_id)

        if not stock:
            raise HTTPException(404, "Stock not found")

        # Business rule example
        # if some_condition:
        #     raise HTTPException(400, "Cannot delete this stock due to ...")

        await self.repo.delete(db, stock)
        return {"message": "Deleted successfully"}