from flask import Flask, jsonify

app = Flask(__name__) # Instance of Flask


# ---- Coupons ---- 
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

@app.get("/api/coupons")
def get_coupons():
    return jsonify(coupons)


@app.get("/api/coupons/count")
def get_coupons_count():
    return jsonify(len(coupons))

# ----- COUPONS END -------

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

# GET http://127.0.0.1:5000/contact
@app.get("/contact")
def get_contact_information():
    contact_info = {
        "email": "loftonjamar8@gmail.com",
        "phone": "689-867-4277"
    }
    return jsonify(contact_info)


# GET http://127.0.0.1:5000/course
@app.get("/course")
def get_course_information():
    course_info = {
        "title": "Introduction Web API with Flash",
        "duration": "4 Sessions",
        "level": "Beginner"
    }
    return jsonify(course_info)


# GET http://127.0.0.1:5000/user-information
@app.get("/user-information")
def get_user_information():
    user_info = {
        "name": "Jey",
        "role": "Student",
        "is_active": True,
        "favorite_technologies": ["React", "Nextjs"]
    }
    return jsonify(user_info)

app.run(debug=True) # Execute the instance
