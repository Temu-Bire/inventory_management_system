# repositories/product_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.Products import Product

class ProductRepository:

    async def create(self, db: AsyncSession, data):
        product = Product(**data.dict())
        db.add(product)
        await db.commit()
        await db.refresh(product)
        return product

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(Product))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, product_id: int):
        result = await db.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()

    async def update(self, db: AsyncSession, product, data):
        for key, value in data.dict(exclude_unset=True).items():
            setattr(product, key, value)

        await db.commit()
        await db.refresh(product)
        return product

    async def delete(self, db: AsyncSession, product):
        await db.delete(product)
        await db.commit()