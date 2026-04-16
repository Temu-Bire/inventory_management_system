# services/product_service.py
from src.repositories.product_repository import ProductRepository
from fastapi import HTTPException

class ProductService:

    def __init__(self):
        self.repo = ProductRepository()

    async def create_product(self, db, data):
        # Example rule
        if data.price <= 0:
            raise HTTPException(400, "Price must be greater than 0")

        return await self.repo.create(db, data)

    async def get_products(self, db):
        return await self.repo.get_all(db)

    async def get_product(self, db, product_id):
        product = await self.repo.get_by_id(db, product_id)

        if not product:
            raise HTTPException(404, "Product not found")

        return product

    async def update_product(self, db, product_id, data):
        product = await self.repo.get_by_id(db, product_id)

        if not product:
            raise HTTPException(404, "Product not found")

        return await self.repo.update(db, product, data)

    async def delete_product(self, db, product_id):
        product = await self.repo.get_by_id(db, product_id)

        if not product:
            raise HTTPException(404, "Product not found")

        # Business rule example
        if product.quantity > 0:
            raise HTTPException(400, "Cannot delete product with stock")

        await self.repo.delete(db, product)
        return {"message": "Deleted successfully"}