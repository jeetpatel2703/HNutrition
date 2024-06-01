import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="food_nutrition"
)

def get_food_categories():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("""
        SELECT fc.id AS category_id, fc.name AS category_name, fi.id AS item_id, fi.name AS item_name,
               ni.calories, ni.protein, ni.fat, ni.carbohydrates
        FROM food_categories fc
        LEFT JOIN food_items fi ON fc.id = fi.category_id
        LEFT JOIN nutritional_info ni ON fi.id = ni.item_id
    """)
    categories = {}
    for row in cursor.fetchall():
        category_id = row['category_id']
        if category_id not in categories:
            categories[category_id] = {
                'id': category_id,
                'name': row['category_name'],
                'items': []
            }
        if row['item_id']:
            categories[category_id]['items'].append({
                'id': row['item_id'],
                'name': row['item_name'],
                'calories': row['calories'],
                'protein': row['protein'],
                'fat': row['fat'],
                'carbohydrates': row['carbohydrates']
            })
    cursor.close()
    return list(categories.values())

def get_nutritional_info(item_id):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("""
        SELECT calories, protein, fat, carbohydrates
        FROM nutritional_info
        WHERE item_id = %s
    """, (item_id,))
    info = cursor.fetchone()
    cursor.close()
    return info

def get_food_items(category_id):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("""
        SELECT fi.*, ni.calories, ni.protein, ni.fat, ni.carbohydrates
        FROM food_items fi
        LEFT JOIN nutritional_info ni ON fi.id = ni.item_id
        WHERE fi.category_id = %s
    """, (category_id,))
    items = cursor.fetchall()
    cursor.close()
    return items

