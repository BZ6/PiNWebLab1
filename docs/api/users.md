# Users API

## Endpoints

- [Me API](users/me.md)

### Create User

Create a new user.

**URL** : `/users`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `UserDefault`: Object containing user details.

**Request Example:**

```json
{
  "username": "john_doe",
  "email": "john@example.com"
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
    "username": "john_doe",
    "email": "john@example.com"
  }
}
```

### Get Users

Retrieve a list of all users.

**URL** : `/users`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

#### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  },
  {
    "id": 2,
    "username": "jane_doe",
    "email": "jane@example.com"
  }
]
```

### Get User

Retrieve a user by ID.

**URL** : `/users/{user_id}`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

#### Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
```

### Update User

Update a user by ID.

**URL** : `/users/{user_id}`

**Method** : `PATCH`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `UserDefault`: Object containing updated user details.

**Request Example:**

```json
{
  "username": "john_doe_updated",
  "email": "john_updated@example.com"
}
```

#### Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "id": 1,
  "username": "john_doe_updated",
  "email": "john_updated@example.com"
}
```

### Delete User

Delete a user by ID.

**URL** : `/users/{user_id}`

**Method** : `DELETE`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

#### Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "ok": true
}
```
