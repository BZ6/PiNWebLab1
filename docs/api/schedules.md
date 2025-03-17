# Schedules API

## Endpoints

### Create Schedule

Create a new schedule.

**URL** : `/schedules`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `ScheduleDefault`: Object containing schedule details.

**Request Example:**

```json
{
  "user_id": 1,
  "date": "2023-10-01T00:00:00"
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
    "user_id": 1,
    "date": "2023-10-01T00:00:00"
  }
}
```

### Get Schedules

Retrieve a list of all schedules.

**URL** : `/schedules`

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
    "user_id": 1,
    "date": "2023-10-01T00:00:00"
  },
  {
    "id": 2,
    "user_id": 2,
    "date": "2023-10-02T00:00:00"
  }
]
```

### Get Schedule

Retrieve a schedule by ID.

**URL** : `/schedules/{schedule_id}`

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
  "user_id": 1,
  "date": "2023-10-01T00:00:00"
}
```

### Update Schedule

Update a schedule by ID.

**URL** : `/schedules/{schedule_id}`

**Method** : `PATCH`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `ScheduleDefault`: Object containing updated schedule details.

**Request Example:**

```json
{
  "user_id": 1,
  "date": "2023-10-01T00:00:00"
}
```

#### Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "id": 1,
  "user_id": 1,
  "date": "2023-10-01T00:00:00"
}
```

### Delete Schedule

Delete a schedule by ID.

**URL** : `/schedules/{schedule_id}`

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
