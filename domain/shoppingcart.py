import dataclasses

from domain.product import Product


@dataclasses.dataclass
class CartItem:
    quantity: int
    product: Product


@dataclasses.dataclass
class ProductWasRemoved:
    cart_item: CartItem
    

class ShoppingCart:
    def __init__(self):
        self.elements = {}
        self.domain_events = {}

    def add(self, product):
        current_item = self.elements.get(product.name)

        if current_item:
            current_item.quantity = current_item.quantity + 1
        else:
            self.elements[product.name] = CartItem(product=product, quantity=1)

    def get_all(self):
        return list(self.elements.values())
    
    def remove(self, product_name):
        if self.elements.get(product_name):
            cart_item = self.elements.pop(product_name)
            self._record_domain_event(ProductWasRemoved(cart_item))

    def _record_domain_event(self, domain_event):
        self.domain_events[domain_event.cart_item.product.name] = domain_event

    def was_removed(self, param):
        if self.domain_events.get(param):
            return True
        else:
            return False
