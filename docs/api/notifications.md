# Notifications API

## Endpoints

### Create Notification

Create a new notification.

**URL** : `/notifications`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `NotificationDefault`: Object containing notification details.

**Request Example:**

```json
{
  "task_id": 1,
  "message": "Task reminder",
  "sent_at": "2023-10-01T12:00:00Z"
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
    "task_id": 1,
    "message": "Task reminder",
    "sent_at": "2023-10-01T12:00:00Z"
  }
}
```

### Get Notifications

Retrieve a list of all notifications.

**URL** : `/notifications`

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
    "task_id": 1,
    "message": "Task reminder",
    "sent_at": "2023-10-01T12:00:00Z"
  },
  {
    "id": 2,
    "task_id": 2,
    "message": "Meeting reminder",
    "sent_at": "2023-10-02T12:00:00Z"
  }
]
```

### Get Notification

Retrieve a notification by ID.

**URL** : `/notifications/{notification_id}`

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
  "task_id": 1,
  "message": "Task reminder",
  "sent_at": "2023-10-01T12:00:00Z"
}
```

### Update Notification

Update a notification by ID.

**URL** : `/notifications/{notification_id}`

**Method** : `PATCH`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

**Request Body:**

- `NotificationDefault`: Object containing updated notification details.

**Request Example:**

```json
{
  "message": "Updated task reminder",
  "sent_at": "2023-10-01T13:00:00Z"
}
```

#### Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
  "id": 1,
  "task_id": 1,
  "message": "Updated task reminder",
  "sent_at": "2023-10-01T13:00:00Z"
}
```

### Delete Notification

Delete a notification by ID.

**URL** : `/notifications/{notification_id}`

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
