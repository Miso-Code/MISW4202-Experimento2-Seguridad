import jwt
from flask import Flask, request
from flask_api import status

app = Flask(__name__)


@app.route("/api/v1/endpoint1")
def endpoint1():
    return "Endpoint público"


@app.route("/api/v1/endpoint2")
def endpoint2():
    return "Endpoint protegido por OAuth2.0"


@app.route("/api/v1/endpoint3")
def endpoint3():
    return "Endpoint protegido por JWT"


@app.route("/api/v1/endpoint4")
def endpoint4():
    return "Endpoint protegido por OAuth2.0 y Rate Limiting"

@app.route("/api/v1/clients")
def clients():
    try:
        bearer_token = request.headers.get('Authorization').split()[1]
        decoded_data = jwt.decode(bearer_token, algorithms=['HS256'], options={"verify_signature": False})
        username = decoded_data["preferred_username"]
        user_roles = decoded_data["realm_access"]["roles"]
        if "seller" in user_roles:
            if username == "vendedor1":
                clients_data = [
                    {'id': 1, 'username': 'john_smith', 'name': 'John Smith', 'address': '123 Main St'},
                    {'id': 2, 'username': 'jane_doe', 'name': 'Jane Doe', 'address': '456 Oak Ave'},
                    {'id': 3, 'username': 'bob_johnson', 'name': 'Bob Johnson', 'address': '789 Elm Blvd'},
                    {'id': 4, 'username': 'sara_jackson', 'name': 'Sara Jackson', 'address': '246 Pine Dr'},
                    {'id': 5, 'username': 'tim_wilson', 'name': 'Tim Wilson', 'address': '135 Maple Ln'}
                ]
            elif username == "vendedor2":
                clients_data = [
                    {'id': 6, 'username': 'amy_adams', 'name': 'Amy Adams', 'address': '567 Oak St'},
                    {'id': 7, 'username': 'chris_brown', 'name': 'Chris Brown', 'address': '890 Elm Ave'},
                    {'id': 8, 'username': 'jessica_hall', 'name': 'Jessica Hall', 'address': '345 Pine Blvd'},
                    {'id': 9, 'username': 'peter_jones', 'name': 'Peter Jones', 'address': '678 Maple Dr'},
                    {'id': 10, 'username': 'kate_smith', 'name': 'Kate Smith', 'address': '901 Main Ln'}
                ]
            else:
                clients_data = []
        else:
            raise Exception()
        response = {
                "vendedor": username,
                "data": clients_data
            }
        return response, status.HTTP_200_OK
    except:
        return {
            "error": "Un-authorized to get this data."
        }, status.HTTP_401_UNAUTHORIZED


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
