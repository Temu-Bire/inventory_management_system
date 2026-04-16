from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.Stock import Stock

class StockRepository:
    async def create(self, db: AsyncSession, data):
        stock = Stock(**data.dict())
        db.add(stock)
        await db.commit()
        await db.refresh(stock)
        return stock

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(Stock))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, stock_id: int):
        result = await db.execute(
            select(Stock).where(Stock.id == stock_id)
        )
        return result.scalar_one_or_none()

    async def delete(self, db: AsyncSession, stock):
        await db.delete(stock)
        await db.commit()