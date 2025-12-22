\# FastAPI User Management API



This is a simple FastAPI application that manages users in memory (no database needed).  



\## Features



\- Home route (`GET /`)  

\- Create users (`POST /users`)  

\- Get all users (`GET /users?limit=optional`)  

\- Get user by ID (`GET /users/{user\_id}`)  

\- Delete user (`DELETE /users/{user\_id}`)  

\- Middleware adds `X-App-Name: User API` header  

\- Pydantic validation for user name and age  

\- Swagger UI and Redoc documentation  



\## Setup



1\. Install dependencies:

```bash

pip install fastapi uvicorn



2.Run the server:

uvicorn main:app --reload



3\. Open in browser:



\- Swagger UI: \[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

\- ReDoc: \[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)



\## API Usage



\- \*\*Create user\*\* (`POST /users`):



```json

{

&nbsp; "name": "John",

&nbsp; "age": 22

}



-Get all users (GET /users)



\- Get user by ID (GET /users/1)



\- Delete user (DELETE /users/1)

