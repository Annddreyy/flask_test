import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/users", methods=['GET'])
def main():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM test')

    data = cur.fetchall()

    data_json = []
    for d in data:
        data_json.append(
            {
                'id': d[0],
                'surname': d[1]
            }
        )

    cur.close()
    conn.close()

    return jsonify(data_json)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)

