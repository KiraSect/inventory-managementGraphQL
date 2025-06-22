from ariadne import QueryType, MutationType
from server.models import Product, StockChange
from server.storage import read_data, write_data

query = QueryType()
mutation = MutationType()


@query.field("getProduct")
def resolve_get_product(_, info, id):
    data = read_data()
    id = int(id)  # убедиться, что id сравнивается как число
    return next((p for p in data["products"] if p["id"] == id), None)


@query.field("listProducts")
def resolve_list_products(_, info, limit=None, offset=0):
    products = read_data()["products"]
    return products[offset:offset + limit] if limit else products[offset:]


@mutation.field("addProduct")
def resolve_add_product(_, info, input):
    data = read_data()

    # Генерация нового ID
    new_id = data.get("next_product_id", 1)
    product = {
        "id": new_id,
        "name": input["name"],
        "quantity": input["quantity"]
    }

    data["products"].append(product)
    data["next_product_id"] = new_id + 1
    write_data(data)

    return product


@mutation.field("updateStock")
def resolve_update_stock(_, info, productId, delta):
    data = read_data()
    productId = int(productId)

    product = next((p for p in data["products"] if p["id"] == productId), None)
    if not product:
        raise Exception("Product not found")

    # Сохраняем новое количество
    new_quantity = product["quantity"] + delta
    product["quantity"] = new_quantity

    # Запись в историю изменений (без изменений)
    change_id = data.get("next_change_id", 1)
    stock_change = {
        "id": change_id,
        "productId": productId,
        "delta": delta,
        "timestamp": StockChange.get_timestamp()
    }
    data["stock_changes"].append(stock_change)
    data["next_change_id"] = change_id + 1
    write_data(data)

    return product

@mutation.field("removeProduct")
def resolve_remove_product(_, info, id):
    data = read_data()
    id = int(id)
    original_len = len(data["products"])
    data["products"] = [p for p in data["products"] if p["id"] != id]
    write_data(data)
    return len(data["products"]) < original_len
