from flask import Flask, render_template, request
from db import get_food_categories, get_food_items, get_nutritional_info , mydb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def food_categories():
    categories = get_food_categories()
    return render_template('food_categories.html', categories=categories)

@app.route('/items/<category_id>')
def food_items(category_id):
    items = get_food_items(category_id)
    return render_template('food_items.html', items=items)

@app.route('/nutritional_info/<item_id>')
def nutritional_info(item_id):
    info = get_nutritional_info(item_id)
    return render_template('nutritional_info.html', info=info)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search']
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("""
            SELECT fi.id AS item_id, fi.name AS item_name, ni.calories, ni.protein, ni.fat, ni.carbohydrates
            FROM food_items fi
            LEFT JOIN nutritional_info ni ON fi.id = ni.item_id
            WHERE fi.name LIKE %s
        """, ('%' + search_query + '%',))
        search_results = cursor.fetchall()
        cursor.close()
        return render_template('search_results.html', search_query=search_query, search_results=search_results) 
    else:
        return render_template('search.html')


app.run(debug=True)