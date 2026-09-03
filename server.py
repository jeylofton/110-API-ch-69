from flask import Flask, jsonify, request

app = Flask(__name__) # Instance of Flask


# ---- Coupons ---- 
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]


products = [
    {
        "id": 1,
        "name": "Cake",
        "price": 10.99
    },
    {
        "id": 2,
        "name": "Cookies",
        "price": 4.99
    },
    {
        "id": 3,
        "name": "Chips",
        "price": 2.99
    }
]

@app.get("/api/coupons")
def get_coupons():
    return jsonify(coupons)


@app.get("/api/coupons/count")
def get_coupons_count():
    return jsonify(len(coupons))


# POST http://127.0.0.1:5000/api/coupons
@app.post("/api/coupons")
def create_coupon():
    new_coupon = request.get_json(silent=True)
    if not new_coupon:
        return jsonify({"error": "Request body must be JSON"}), 400
    if "code" not in new_coupon or "discount" not in new_coupon:
        return jsonify({"error": "Missing required field: code and discount"}), 400
    new_coupon["_id"] = len(coupons) + 1
    coupons.append(new_coupon)
    return jsonify(new_coupon), 201

# PUT http://127.0.0.1:5000/api/products/ -> Update a product by id
@app.put("/api/products/<int:product_id>")
def update_product_by_id(product_id):
    updated_data = request.get_json(silent=True)
    if not updated_data:
        return jsonify({"error": "Request body must be JSON"}), 400

    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_data["name"]
            product["price"] = updated_data["price"]
            return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404

# DELETE http://127.0.0.1/api/products -> Remove product by id
@app.delete("/api/products/<int:product_id>")
def remove_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"error": "Product not found"}), 404


# GET http://127.0.0.1:5000/api/coupons/
@app.get("/api/coupons/<int:id>")
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify(coupon), 200
    return jsonify({"error": "Coupon not found"}), 404

# DELETE http://127.0.0.1:5000/api/coupons/ -> Remove a coupon by id
@app.delete("/api/coupons/<int:id>")
def remove_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            coupons.remove(coupon)
            return jsonify({"message": "Coupon deleted successfully"}), 200
    return jsonify({"error": "Coupon not found"}), 404


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
        "title": "Introduction Web API with Flask",
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
