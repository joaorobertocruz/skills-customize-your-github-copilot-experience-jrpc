# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API that manages a collection of items using FastAPI. In this assignment, students will practice routing, request validation, JSON responses, and CRUD operations while creating a functional web service.

## 📝 Tasks

### 🛠️ Create the API

#### Description

Set up a FastAPI application that exposes a simple endpoint for managing a list of items. Use an in-memory data store and define a model for each item.

#### Requirements

The completed program must:

- Create a FastAPI app with a root endpoint that returns a welcome message.
- Define a Pydantic model for an item with fields such as `id`, `title`, `description`, and `completed`.
- Implement a `GET /items` endpoint that returns all items in JSON format.
- Implement a `POST /items` endpoint that creates a new item.
- Return `201 Created` when a new item is successfully added.
- Validate incoming data to prevent invalid item records.

### 🛠️ Add CRUD functionality

#### Description

Extend the API so each item can be retrieved, updated, and deleted by its unique identifier.

#### Requirements

The completed program must:

- Implement `GET /items/{item_id}` to fetch a single item.
- Implement `PUT /items/{item_id}` to update an existing item.
- Implement `DELETE /items/{item_id}` to remove an item from the collection.
- Return `404 Not Found` when an item does not exist.
- Use appropriate HTTP status codes for each action.
- Ensure responses are returned in a consistent JSON format.
- Verify that the API documentation is available at `/docs`.
