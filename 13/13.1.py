from flask import Flask, jsonify
from math import sqrt

app = Flask(name)

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        limit = int(sqrt(n)) + 1
        for i in range(3, limit, 2):
            if n % i == 0:
                return False
        return True

@app.route('/alkuluku/<int:n>')
def is_prime_route(n):
    result = {"Number": n, "isPrime": is_prime(n)}
    return jsonify(result)

if name == 'main':
    app.run(debug=True)