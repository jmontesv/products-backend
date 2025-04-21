# 🛍️ Products App

Aplicación web que muestra una tabla de productos con filtros por nombre, precio y paginación.  
Desarrollada con **Flask** para el backend y **React** para el frontend.

---

## 🧩 Funcionalidades

- 🔍 Filtro por nombre con **debounce**
- 💰 Filtro por precio (slider)
- 📄 Paginación dinámica
- 🎯 CORS configurado
- ⚡ Backend en Flask
- 🎨 Frontend con React + Vite + TypeScript

## 🌐 Backend Flask(Python)

Instala las dependencias:
```bash
pip install flask flask-cors
```

Corre la aplicación:
```bash
python app.py
```

Abre en tu navegador: http://localhost:5000

## 📋 Endpoints de la API
GET /products
Parámetros de consulta (query params):
- name → filtra por nombre (string)
- page → número de página (int)
- per_page → productos por página (int)
- max_price → precio máximo (float)
- min_price → precio máximo (float)

Ejemplo: GET /products?name=lap&page=1&per_page=5&max_price=1000