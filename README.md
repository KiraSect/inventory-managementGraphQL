# Служба управления складскими запасами Inventory-management

## Обзор
Проект реализует систему управления складскими остатками. Поддерживается:
- добавление и удаление товаров;

- обновление остатков;

- просмотр списка всех товаров;

- получение информации о конкретной позиции по ID.

Реализованы все запросы мутации и сущности (кроме подписки) описанные в задании №14

![image](https://github.com/user-attachments/assets/edd7d8b7-ef19-4b81-a155-eef71e2aafe2)

## Стек технологий

- **Язык:** Python 3, на Pycharm 
- **GraphQL-библиотека:** [Ariadne](https://ariadnegraphql.org)  
- **Хранилище:** JSON-файл (`data.json`)  


## Установка

1. Клонируйте репозиторий

   ```bash
   git clone https://github.com/KiraSect/inventory-managementGraphQL
   cd inventory-managementGraphQL
   ```

2. Установите зависимости
   Откройте терминал pycharm и выполните:
   
   ```bash
    pip install ariadne uvicorn python-dotenv aiofiles
   ```
   
3. Проверьте структуру проекта
   
![image](https://github.com/user-attachments/assets/bb3755e8-00f4-49f1-aadf-66be824d6d6e)

##  Запуск сервера
  Откройте терминал pycharm и выполните:
     ```
    uvicorn server.main:app --reload
    ```
    
Сервер поднимется по адресу: 
**http://localhost:8000/graphql**.


## Примеры GraphQL-запросов

1. Query: Получить товар по ID

```graphql
query {
  getProduct(id: 2) {
    id
    name
    quantity
  }
}
```
Ожидаемый ответ:

![image](https://github.com/user-attachments/assets/3959a12c-dfc1-4459-8d77-0a8c1e81f6cc)


2. Mutation: Добавить товар

```graphql
mutation {
  addProduct(input: { name: "Apple", quantity: 100 }) {
    id
    name
    quantity
  }
}
```
Ожидаемый ответ:

![image](https://github.com/user-attachments/assets/bfc9c5fb-f747-4814-8df4-b54a4304bc1b)


3. Mutation: Обновить количество на складе

```graphql
mutation {
  updateStock(productId: 2, delta: -7) {
    id
    name
    quantity
  }
}
```
Ожидаемый ответ:

![image](https://github.com/user-attachments/assets/fa913863-51ef-4414-a5b2-82e92b4908d7)


4. Query: Получить список продуктов
   
```graphql
query {
  listProducts {
    id
    name
    quantity
  }
}
```
Ожидаемый ответ:

![image](https://github.com/user-attachments/assets/bb3a1329-4dbb-4187-9048-cab7c9f9bbbe)

5.  Mutation: Удалить продукт по ID
```graphql
mutation {
  removeProduct(id: 3)
}
```
Ожидаемый ответ:

![image](https://github.com/user-attachments/assets/b4880989-c7bd-473c-8b38-abccb9e2b64f)

---

## Формат сохранения данных

```
{
  "products": [...],
  "stock_changes": [...],
  "next_product_id": <int>,
  "next_change_id": <int>
}
```
В файле data.json происходит сохранение продуктов, логов изменений продуктов, id для добавления следующего продукта и id для следующего изменения в системе.

![image](https://github.com/user-attachments/assets/af8bd2d8-3aaf-444f-80de-7b07ab9c3b77)


