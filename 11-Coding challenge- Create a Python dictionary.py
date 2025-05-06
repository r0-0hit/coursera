product_catalog = {
    "SKU123": {"name": "Widget A", "price": 19.99, "quantity": 50},
    "SKU456": {"name": "Gadget B", "price": 34.95, "quantity": 25},
    "SKU789": {"name": "Gizmo C", "price": 9.99, "quantity": 100},
}

sku_to_retrieve = "SKU123"

if sku_to_retrieve in product_catalog:
    product = product_catalog[sku_to_retrieve]
    print(f"The price of {product['name']} is ${product['price']:.2f}")
    # * OR this is also okkk... print(f"The price of {product_catalog[sku_to_retrieve]['name']} is ${product_catalog[sku_to_retrieve]['price']:.2f}")
else:
    print("Product not found.")
