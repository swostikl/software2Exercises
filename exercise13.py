#Question No 1
#Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not. Use the
# prior prime number exercise as a starting point. For example, a GET request for number 31 is given as:
# http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.

import math
from flask import Flask, request, jsonify
app=Flask(__name__)

@app.route("/primeNumber")
def prime_number():
    args = request.args
    try:
        number = int(args.get('number', 0))
        if number <= 1:
            response = {
                'number': number,
                'isprime': False
            }
            return jsonify(response)
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break
        response = {
            "Number": number,
            "isprime": is_prime
        }
        return jsonify(response)
    except ValueError:
        return jsonify({"error": "Invalid input, please provide an integer."}), 400
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


#question2
# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport
#in JSON format. The information is fetched from the airport database used on this course. For example, the GET request
# for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK",
# "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

from flask import Flask, request, jsonify
