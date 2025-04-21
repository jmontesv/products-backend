# 📋 Endpoints de la API
GET /products
Parámetros de consulta (query params):
- name → filtra por nombre (string)
- page → número de página (int)
- per_page → productos por página (int)
- max_price → precio máximo (float)
- min_price → precio máximo (float)

Ejemplo: GET /products?name=lap&page=1&per_page=5&max_price=1000