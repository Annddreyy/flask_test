from flask import Flask, jsonify

from db import get_connection

app = Flask(__name__)


@app.route("/api/v1/recipes", methods=['GET'])
def get_recipes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM recipe')

    recipes = cur.fetchall()

    recipes_json = []
    for recipe in recipes:
        recipes_json.append(
            {
                'id': recipe[0],
                'title': recipe[1],
                'callories': recipe[2],
                'cooking_time': recipe[3],
                'image_path': recipe[4]
            }
        )

    cur.close()
    conn.close()

    return jsonify(recipes_json)

@app.route('/api/v1/recipe_types')
def get_types():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM recipe_type')

    recipe_types = cur.fetchall()

    recipe_types_json = []
    for recipe in recipe_types:
        recipe_types_json.append(
            {
                'id': recipe[0],
                'title': recipe[1],
                'image_path': recipe[2]
            }
        )

    return jsonify(recipe_types_json)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)

