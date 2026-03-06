# 🚀 Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework to practice designing endpoints, handling JSON request/response bodies, and running a local development server.

## 📝 Tasks

### 🛠️ Create a basic REST API

#### Description
Implement a small web API that allows clients to list, create, and retrieve simple `Item` objects. Use FastAPI to declare routes and Pydantic models for request/response validation.

#### Requirements
Completed project should:

- Provide a GET `/items/` endpoint returning a list of items
- Provide a GET `/items/{item_id}` endpoint returning a single item or 404
- Provide a POST `/items/` endpoint to create a new item from JSON payload
- Use Pydantic models for request validation and response serialization
- Include clear instructions to run the server locally with `uvicorn`

## ⏱ Estimated time

60–90 minutes

## ⚙️ Difficulty

Medium

## 💡 Hints

- Install dependencies with `pip install fastapi uvicorn`
- Define request/response schemas using `pydantic.BaseModel`
- Return proper HTTP status codes (201 for created, 404 when not found)
- Use an in-memory list or dict to store items for this assignment (persistence not required)

## 📦 Starter code

See `starter-code.py` for a minimal FastAPI app with example endpoints.

## ✅ Example requests

Create an item:

```
POST /items/
Content-Type: application/json

{
  "name": "Sample Widget",
  "description": "A small widget",
  "price": 9.99
}
```

List items:

```
GET /items/
```

Get item by id:

```
GET /items/1
```

---

If you want, I can add automated tests, a `requirements.txt`, or GitHub Actions to run tests.
