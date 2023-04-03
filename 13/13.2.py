import sqlite3
from flask import Flask, jsonify

app = Flask(name)

def get_airport_info(icao_code):
    conn = sqlite3.connect('lentokentatietokanta.db')
    c = conn.cursor()
    c.execute("SELECT * FROM airports WHERE ident = ?", (icao_code,))
    result = c.fetchone()
    conn.close()

    if result:
        icao, name, city = result[1], result[3], result[10]
        return {"ICAO": icao, "Name": name, "Municipality": city}
    else:
        return {"error": "Airport not found"}

@app.route('/kenttä/<string:icao_code>')
def get_airport_route(icao_code):
    result = get_airport_info(icao_code)
    return jsonify(result)

if name == 'main':
    app.run(debug=True)