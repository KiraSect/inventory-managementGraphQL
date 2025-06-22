import requests

URL = "http://localhost:8000"

def gql(query, variables=None):
    response = requests.post(URL, json={"query": query, "variables": variables})
    print(response.json())

# Пример: Добавление продукта
gql("""
mutation($input: AddProductInput!) {
  addProduct(input: $input) {
    id
    name
    quantity
  }
}
""", {"input": {"name": "SSD Kingston", "quantity": 10}})

# Пример: Обновление стока
gql("""
mutation {
  updateStock(productId: "ID_ПРОДУКТА", delta: -8) {
    name
    quantity
  }
}
""")
