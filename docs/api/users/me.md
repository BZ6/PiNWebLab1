# Me API

## Endpoints

### Register User

Register a new user.

**URL** : `/users/me/register`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `UserCreate`: Object containing user creation details.

**Request Example:**

```json
{
  "first_name": "john",
  "last_name": "doe",
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
  "status": 201,
  "data": {
    "id": 1,
    "first_name": "john",
    "last_name": "doe",
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword",
    "access_token": null
  }
}
```

### Login User

Login user.

**URL** : `/users/me/login`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `UserLogin`: Object containing user login details.

**Request Example:**

```json
{
  "username": "john_doe",
  "password": "securepassword"
}
```

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
  "status": 201,
  "data": {
    "id": 1,
    "first_name": "john",
    "last_name": "doe",
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhYm9iYSIsImV4cCI6MTc0MzI0ODU5MSwicmVmcmVzaCI6ZmFsc2V9.WuvI0wNefcyGajtcXAkBvKoUQdfipg4QYNmyYI4ax88"
  }
}
```

### Password User

Reset password for user.

**URL** : `/users/me/password`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `UserLogin`: Object containing user login details.

**Request Example:**

```json
{
  "username": "john_doe",
  "password": "newsecurepassword"
}
```

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
  "status": 201,
  "data": {
    "id": 1,
    "first_name": "john",
    "last_name": "doe",
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword",
    "access_token": null
  }
}
```

### Current User

Reset password for user.

**URL** : `/users/me/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

#### Success Responses

**Code** : `200 Ok`

**Content** : `{}`

```json
{
  "status": 200,
  "data": {
    "id": 1,
    "first_name": "john",
    "last_name": "doe",
    "username": "john_doe",
    "email": "john@example.com"
  }
}
```
