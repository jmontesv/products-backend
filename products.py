import unicodedata

def normalize(text):
    return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8").lower()

def filter_by_name(name, products):
    name_normalized = normalize(name)
    return [
        product for product in products
        if normalize(product["nombre"]).startswith(name_normalized)
    ]

def filter_by_price_min(price_min, products):
    return list(filter(lambda product: product["precio"] >= price_min, products))

def filter_by_price_max(price_max, products):
    return list(filter(lambda product: product["precio"] <= price_max, products))

def filter_by_page(page, per_page, products):
    total = len(products)
    total_pages = (total + per_page - 1) // per_page  # redondeo hacia arriba

    if page < 1 or page > total_pages:
        return []

    start = (page - 1) * per_page
    end = start + per_page
    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "data": products[start:end]
    }

    
