from models.product import Product
from models.order import Order, OrderItem

# Create product
p1 = Product(
    product_id=1, name="Laptop", category="Electronics", price=1200.0, stock_quantity=10
)

# Create order
order = Order(
    order_id=1,
    customer_name="John",
    items=[OrderItem(product_id=1, quantity=2, price=1200.0)],
    total_amount=2400.0,
)

print(p1)
print(order)
