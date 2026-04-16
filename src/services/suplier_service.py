from src.repositories.suplier_repository import SupplierRepository
from fastapi import HTTPException

class SupplierService:

    def __init__(self):
        self.repo = SupplierRepository()

    async def create_supplier(self, db, data):
        return await self.repo.create(db, data)

    async def get_suppliers(self, db):
        return await self.repo.get_all(db)

    async def get_supplier(self, db, supplier_id):
        supplier = await self.repo.get_by_id(db, supplier_id)

        if not supplier:
            raise HTTPException(404, "Supplier not found")

        return supplier

    async def delete_supplier(self, db, supplier_id):
        supplier = await self.repo.get_by_id(db, supplier_id)

        if not supplier:
            raise HTTPException(404, "Supplier not found")

        # Business rule example
        # if some_condition:
        #     raise HTTPException(400, "Cannot delete this supplier due to ...")

        await self.repo.delete(db, supplier)
        return {"message": "Deleted successfully"}