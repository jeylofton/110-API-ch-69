# 110-API-ch-69

## The 5 Steps for Creating an API Endpoint

Every endpoint in Flask is built from these five pieces, in this order:

```python
@app.get("/course")              # 1. Decorator   2. HTTP Method   3. Path (URL)
def get_course_information():    # 4. Function
    course_info = {
        "title": "Introductory Web API with Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }
    return jsonify(course_info)  # 5. Return (jsonify)
```

1. **Decorator** — `@app` attaches the function below it to the Flask app. Without it, the function is just a normal function and Flask never knows it exists.
2. **HTTP Method** — `.get` says this endpoint answers GET requests. Other options are `.post`, `.put`, and `.delete`.
3. **Path (URL)** — `"/course"` is the address the client types after the host. It must match **exactly** — `/course` and `/course_info` are different endpoints.
4. **Function** — the code that runs when a request comes in. Its name must be **unique** across the whole file, because Flask registers routes by function name.
5. **Return (jsonify)** — `jsonify()` converts a Python dict or list into JSON and sets the `Content-Type: application/json` header so the client knows what it's receiving.

### Gotchas

- Define every route **above** `app.run(...)` — that line blocks, so anything below it never registers.
- Use `http://`, not `https://`. The Flask dev server has no certificate.
- Python booleans are `True` / `False`; `jsonify` lowercases them to `true` / `false` in the JSON.
