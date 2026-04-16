from src.repositories.catagory_repository import CategoryRepository
from fastapi import HTTPException

class CategoryService:

    def __init__(self):
        self.repo = CategoryRepository()

    async def create_category(self, db, data):
        return await self.repo.create(db, data)

    async def get_categories(self, db):
        return await self.repo.get_all(db)

    async def get_category(self, db, category_id):
        category = await self.repo.get_by_id(db, category_id)

        if not category:
            raise HTTPException(404, "Category not found")

        return category

    async def delete_category(self, db, category_id):
        category = await self.repo.get_by_id(db, category_id)

        if not category:
            raise HTTPException(404, "Category not found")

        # Business rule example
        # if some_condition:
        #     raise HTTPException(400, "Cannot delete this category due to ...")

        await self.repo.delete(db, category)
        return {"message": "Deleted successfully"}