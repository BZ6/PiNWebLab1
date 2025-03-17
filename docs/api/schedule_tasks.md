# Schedule Tasks API

## Endpoints

### Create Schedule Task

Create a new schedule task.

**URL** : `/schedule_tasks/{schedule_id}/{task_id}`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

#### Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
  "status": 201,
  "data": {
    "schedule_id": 1,
    "task_id": 1,
    "added_at": "2023-10-01T12:00:00Z"
  }
}
```

### Get Schedule Tasks

Retrieve a list of all schedule tasks.

**URL** : `/schedule_tasks`

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
    "schedule_id": 1,
    "task_id": 1,
    "added_at": "2023-10-01T12:00:00Z"
  },
  {
    "schedule_id": 2,
    "task_id": 2,
    "added_at": "2023-10-02T12:00:00Z"
  }
]
```

### Get Schedule Task

Retrieve a schedule task by schedule ID and task ID.

**URL** : `/schedule_tasks/{schedule_id}/{task_id}`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

#### Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "schedule_id": 1,
  "task_id": 1,
  "added_at": "2023-10-01T12:00:00Z"
}
```

### Delete Schedule Task

Delete a schedule task by schedule ID and task ID.

**URL** : `/schedule_tasks/{schedule_id}/{task_id}`

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
