from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)

    def with_discount(self, percent: float) -> float:
        return self.price * (1 - percent / 100)


# Создание объекта
product = Product(name="Ноутбук", price=1200.0, tags=["electronics", "portable"])

print(product)  # Product(name='Ноутбук', price=1200.0, tags=['electronics', 'portable'])
print(product.name)  # Ноутбук
print(product.with_discount(10))  # 1080.0