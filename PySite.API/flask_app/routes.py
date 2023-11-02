from flask_app import app
from flask import jsonify, request

# Add initial User
current_id = 0
users = {str(current_id): {"name": "Jonass"}}


@app.route("/api/users", methods=["GET", "POST"])
def handle_users():
    global current_id
    if request.method == "GET":
        return jsonify({"users": users})

    elif request.method == "POST":
        # Recieved new request to add a user
        try:
            data = request.get_json()
            print("printing the data recieved from frontend", data)
            current_id += 1
            users[str(current_id)] = data

            return jsonify({"message": "Users updated successfully"})
        except Exception as e:
            print("Error occured: ", e)
            return jsonify({"message": "could not update users"}), 500


@app.route("/api/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def handle_user(user_id):
    if user_id in users:
        if request.method == "GET":
            return jsonify(users[user_id])

        elif request.method == "PUT":
            data = request.get_json()
            users[user_id] = data
            return jsonify(users[user_id])
        
        elif request.method == "DELETE":
            del users[user_id] 
            return f"delete user with id: {user_id}"
    else:
        return jsonify({"message": "User not found"}), 404
