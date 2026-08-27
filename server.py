from flask import Flask, jsonify

app = Flask(__name__) # Instance of Flask

@app.get("/")
def index():
    return jsonify("Welcome to Flask Framework")


@app.get("/cohort-69")
def Hello_World():
    return jsonify({"message": "Hello cohort 69"})


# http://127.0.0.1:5000/students-ch-69
@app.get("/students-ch-69")
def get_students():
    return jsonify(["Edwin", "Jey", "Austin", "Chante", "Leo"])


app.run(debug=True) # Execute the instance
