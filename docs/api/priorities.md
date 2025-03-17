# Priorities API

## Endpoints

### Create Priority

Create a new priority.

**URL** : `/priorities`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `PriorityDefault`: Object containing priority details.

**Request Example:**

```json
{
  "name": "High"
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
    "name": "High"
  }
}
```

### Get Priorities

Retrieve a list of all priorities.

**URL** : `/priorities`

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
    "name": "High"
  },
  {
    "id": 2,
    "name": "Medium"
  }
]
```

### Get Priority

Retrieve a priority by ID.

**URL** : `/priorities/{priority_id}`

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
  "name": "High"
}
```

### Update Priority

Update a priority by ID.

**URL** : `/priorities/{priority_id}`

**Method** : `PATCH`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `PriorityDefault`: Object containing updated priority details.

**Request Example:**

```json
{
  "name": "High Updated"
}
```

#### Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "id": 1,
  "name": "High Updated"
}
```

### Delete Priority

Delete a priority by ID.

**URL** : `/priorities/{priority_id}`

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
