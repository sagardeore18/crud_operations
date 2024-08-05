from flask import Flask, jsonify, request
import subject_crud_recored as crud

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Sagar!'

@app.route('/get-subject/<subject_id>')
def get_subject(subject_id):
    return crud.display_record(subject_id)

@app.route('/insert-subject', methods=['POST'])
def insert_subject():
    subject = request.json
    print(f"subject : {subject}")
    crud.insert_into_mysql(subject.get("subject_id"),subject.get("subject_name"),subject.get("teacher_id"))
    return f"subject with id {subject.get("subject_id")} inserted successfully!"

@app.route('/update-subject', methods=['PUT'])
def update_subject():
    subject = request.json
    print(f"subject : {subject}")
    crud.update_record(subject_name = subject.get("subject_name"), subject_id = subject.get("subject_id"))
    return f"subject with id {subject.get("subject_id")} updated successfully!"

@app.route('/update-teacher', methods=['PUT'])
def update_teacher():
    teacher = request.json
    print(f"teacher : {teacher}")
    crud.update_teacher(subject_id = teacher.get("subject_id"), teacher_id = teacher.get("teacher_id"))
    return f"subject with id {teacher.get("teacher_id")} updated successfully!"


@app.route('/delete-subject', methods=['POST'])
def delete_subject():
    subject = request.json
    print(f"subject : {subject}")
    crud.delete_record(subject.get("subject_id"))
    return f"subject with id {subject.get("subject_id")} deleted successfully!"


@app.route('/delete-subject/<subject_id>', methods=['DELETE'])
def delete_subject_1(subject_id):
    print(f"subject_id : {subject_id}")
    crud.delete_record(subject_id)
    return f"subject with id {subject_id} deleted successfully!"



if __name__ == "__main__":
    app.run(debug=True)