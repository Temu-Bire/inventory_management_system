from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.Categories import  Category

class CategoryRepository:
    async def create(self, db: AsyncSession, data):
        category = Category(**data.dict())
        db.add(category)
        await db.commit()
        await db.refresh(category)
        return category

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(Category))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, category_id: int):
        result = await db.execute(
            select(Category).where(Category.id == category_id)
        )
        return result.scalar_one_or_none()



    async def delete(self, db: AsyncSession, category):
        await db.delete(category)
        await db.commit()