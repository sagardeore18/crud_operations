from flask import Flask, jsonify, request
import crud_student_record as crud

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Sagar!'

@app.route('/get-user/<roll_no>')
def get_user(roll_no):
    return crud.display_record(roll_no)

@app.route('/insert-user', methods=['POST'])
def insert_user():
    user = request.json
    print(f"user : {user}")
    crud.insert_into_mysql(user.get("roll_no"),user.get("name"),user.get("marks"))
    return f"user with id {user.get("roll_no")} inserted successfully!"

@app.route('/update-user', methods=['PUT'])
def update_user():
    user = request.json
    print(f"user : {user}")
    crud.update_record(roll_no = user.get("roll_no"), name = user.get("name"))
    return f"user with id {user.get("roll_no")} updated successfully!"

@app.route('/delete-user', methods=['POST'])
def delete_user():
    user = request.json
    print(f"user : {user}")
    crud.delete_record(user.get("roll_no"))
    return f"user with id {user.get("roll_no")} deleted successfully!"


@app.route('/delete-user/<roll_no>', methods=['DELETE'])
def delete_user_1(roll_no):
    print(f"roll_no : {roll_no}")
    crud.delete_record(roll_no)
    return f"user with id {roll_no} deleted successfully!"



if __name__ == "__main__":
    app.run(debug=True)