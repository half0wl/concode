# Concode API

## Project Setup

To get a local dev environment running,

1. Clone this repo and `cd server/`

2. Create a virtualenv and activate it:

```
$ virtualenv .venv && source .venv/bin/activate
```

3. Install dependencies:

```
$ pip install -r requirements.txt
```

4. Set up environment variables:

```
$ export DJANGO_SETTINGS_MODULE='concode.settings.dev'
$ export GITHUB_CLIENT_SECRET=client_secret
```

5. Migrate DB and run:

```
$ python manage.py makemigrations core
$ python manage.py migrate
$ python manage.py runserver
```

(Maybe I should dockerize this.)

## Authentication

Step 1. Direct user to https://github.com/login/oauth/authorize?client_id=f011549ce875a82ec3a1&redirect_uri=http://127.0.0.1:8000/authorization to start the OAuth flow.

Step 2. If the user accepts, they will be redirected to `/authorization` with a `code` in the parameter (e.g. `http://127.0.0.1:8000/authorization?code=supersecretcode`).

Step 3. Exchange the `code` for a JWT token by `POST`ing it to `/auth/social/jwt/`.

**POST `/auth/social/jwt/`** should return a JWT token, which should be included in all subsequent requests as a header in the format: `Authorization: JWT <token>`.

## Current Endpoints

Note: Currently, all endpoints do not require authentication or permissions.

**GET `/users/`**

List all users.

```
$ curl -X GET http://127.0.0.1:8000/users/

[
  {
    "id": 1,
    "first_name": "Test",
    "last_name": "User",
    "username": "test_user",
    "bio": "Lorem Ipsum."
  },
  {
    "id": 2,
    "first_name": "Test",
    "last_name": "User2",
    "username": "test_user2",
    "bio": "Hello!"
  },
  ...
]
```


**GET `/users/<username>/`**

Retrieve a single user by username.

```
$ curl -X GET http://127.0.0.1:8000/users/test_user/

{
    "id": 1,
    "first_name": "Test",
    "last_name": "User",
    "username": "test_user",
    "bio": "Lorem Ipsum."
}
```

**PATCH `/users/<username>/`**

Update a user's profile details. (A profile is automatically for each new user
using placeholder values, so we only have to update it.) Note: It's possible to
`PATCH` user details such as `first_name`, `username`, etc., but the backend
will only save the profile details and discard the rest.

```
curl -X PATCH http://127.0.0.1:8000/users/test_user/ --data 'bio=Hello, world!'

{
    "id": 1,
    "first_name": "Test",
    "last_name": "User",
    "username": "test_user",
    "bio": "Hello, world!"
}
```