from domain.product import Product
from domain.shoppingcart import ShoppingCart, CartItem


def test_add_item():
    cart = ShoppingCart()
    cart.add(Product("IPad Pro"))
    cart.add(Product("Hero ink Pen"))


def test_get_all_items():
    cart = ShoppingCart()
    cart.add(Product("IPad Pro"))
    cart.add(Product("Hero ink Pen"))
    cart.add(Product("Reebok Cricket bat"))
    cart.add(Product("Reebok Cricket bat"))

    assert cart.get_all() == \
           [CartItem(product=Product("IPad Pro"), quantity=1),
            CartItem(product=Product("Hero ink Pen"), quantity=1),
            CartItem(product=Product("Reebok Cricket bat"), quantity=2)]


def test_remove_an_existing_product():
    cart = ShoppingCart()
    cart.add(Product("Reebok Cricket bat"))
    cart.add(Product("Reebok Cricket bat"))

    assert cart.get_all() == \
           [CartItem(product=Product("Reebok Cricket bat"), quantity=2)]

    cart.remove("Reebok Cricket bat")

    assert cart.get_all() == []


def test_remove_an_non_existing_product():
    cart = ShoppingCart()
    cart.add(Product("Reebok Cricket bat"))
    cart.add(Product("Reebok Cricket bat"))

    assert cart.get_all() == \
           [CartItem(product=Product("Reebok Cricket bat"), quantity=2)]

    cart.remove("IPad Pro")

    assert cart.get_all() == \
           [CartItem(product=Product("Reebok Cricket bat"), quantity=2)]


def test_audit_remove_an_existing_product():
    cart = ShoppingCart()
    cart.add(Product("Reebok Cricket bat"))
    cart.add(Product("Reebok Cricket bat"))

    assert cart.get_all() == \
           [CartItem(product=Product("Reebok Cricket bat"), quantity=2)]

    cart.remove("Reebok Cricket bat")

    assert cart.get_all() == []
    assert cart.was_removed("Reebok Cricket bat") == True

