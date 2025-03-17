# Time Entries API

## Endpoints

### Create Time Entry

Create a new time entry.

**URL** : `/time_entries`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `TimeEntryDefault`: Object containing time entry details.

**Request Example:**

```json
{
  "task_id": 1,
  "start_time": "2023-10-01T09:00:00",
  "end_time": "2023-10-01T17:00:00",
  "duration": 480
}
```

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
  "status": 201,
  "data": {
    "id": 1,
    "task_id": 1,
    "start_time": "2023-10-01T09:00:00",
    "end_time": "2023-10-01T17:00:00",
    "duration": 480
  }
}
```

### Get Time Entries

Retrieve a list of all time entries.

**URL** : `/time_entries`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
  {
    "id": 1,
    "task_id": 1,
    "start_time": "2023-10-01T09:00:00",
    "end_time": "2023-10-01T17:00:00",
    "duration": 480
  },
  {
    "id": 2,
    "task_id": 2,
    "start_time": "2023-10-02T09:00:00",
    "end_time": "2023-10-02T17:00:00",
    "duration": 480
  }
]
```

### Get Time Entry

Retrieve a time entry by ID.

**URL** : `/time_entries/{time_entry_id}`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "id": 1,
  "task_id": 1,
  "start_time": "2023-10-01T09:00:00",
  "end_time": "2023-10-01T17:00:00",
  "duration": 480
}
```

### Update Time Entry

Update a time entry by ID.

**URL** : `/time_entries/{time_entry_id}`

**Method** : `PATCH`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `TimeEntryDefault`: Object containing updated time entry details.

**Request Example:**

```json
{
  "task_id": 1,
  "start_time": "2023-10-01T09:00:00",
  "end_time": "2023-10-01T17:00:00",
  "duration": 480
}
```

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "id": 1,
  "task_id": 1,
  "start_time": "2023-10-01T09:00:00",
  "end_time": "2023-10-01T17:00:00",
  "duration": 480
}
```

### Delete Time Entry

Delete a time entry by ID.

**URL** : `/time_entries/{time_entry_id}`

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "ok": true
}
```
