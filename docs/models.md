# Database Models

## ScheduleTaskDefault

- `schedule_id`: Foreign key to Schedule
- `task_id`: Foreign key to Task

## UserDefault

- `first_name`: String
- `last_name`: String
- `username`: String
- `email`: String

## PriorityDefault

- `name`: String

## TaskDefault

- `description`: String
- `deadline`: DateTime
- `priority_id`: Foreign key to Priority
- `user_id`: Foreign key to User

## TimeEntryDefault

- `task_id`: Foreign key to Task
- `start_time`: DateTime
- `end_time`: DateTime
- `duration`: Integer

## ScheduleDefault

- `user_id`: Foreign key to User
- `date`: DateTime

## NotificationDefault

- `task_id`: Foreign key to Task
- `message`: String
- `sent_at`: DateTime

## User

- `id`: Primary key
- `first_name`: String
- `last_name`: String
- `username`: String
- `password_hash`: String
- `email`: String
- `tasks`: Relationship with Task
- `schedules`: Relationship with Schedule

## UserInner

- `username`: String
- `email`: String
- `tasks`: List of Task
- `schedules`: List of Schedule

## UserCreate

- `first_name`: String
- `last_name`: String
- `username`: String
- `email`: String
- `password`: String

## UserLogin

- `username`: String
- `password`: String

## UserJWTResponse

- `first_name`: String
- `last_name`: String
- `username`: String
- `email`: String
- `password`: String
- `access_token`: String

## UserResponse

- `first_name`: String
- `last_name`: String
- `username`: String
- `email`: String

## Priority

- `id`: Primary key
- `name`: String
- `tasks`: Relationship with Task

## PriorityInner

- `name`: String
- `tasks`: List of Task

## Task

- `id`: Primary key
- `description`: String
- `deadline`: DateTime
- `priority_id`: Foreign key to Priority
- `user_id`: Foreign key to User
- `priority`: Relationship with Priority
- `user`: Relationship with User
- `time_entries`: Relationship with TimeEntry
- `notifications`: Relationship with Notification
- `schedules`: Relationship with Schedule through ScheduleTask

## TaskInner

- `description`: String
- `deadline`: DateTime
- `priority_id`: Foreign key to Priority
- `user_id`: Foreign key to User
- `priority`: Priority
- `user`: List of User
- `time_entries`: List of TimeEntry
- `notifications`: List of Notification
- `schedules`: List of Schedule

## TimeEntry

- `id`: Primary key
- `task_id`: Foreign key to Task
- `start_time`: DateTime
- `end_time`: DateTime
- `duration`: Integer
- `task`: Relationship with Task

## TimeEntryInner

- `task_id`: Foreign key to Task
- `start_time`: DateTime
- `end_time`: DateTime
- `duration`: Integer
- `task`: Task

## Schedule

- `id`: Primary key
- `user_id`: Foreign key to User
- `date`: DateTime
- `user`: Relationship with User
- `tasks`: Relationship with Task through ScheduleTask

## ScheduleInner

- `user_id`: Foreign key to User
- `date`: DateTime
- `user`: User
- `tasks`: List of Task

## Notification

- `id`: Primary key
- `task_id`: Foreign key to Task
- `message`: String
- `sent_at`: DateTime
- `task`: Relationship with Task

## NotificationInner

- `task_id`: Foreign key to Task
- `message`: String
- `sent_at`: DateTime
- `task`: Task

## ScheduleTask

- `schedule_id`: Foreign key to Schedule
- `task_id`: Foreign key to Task
- `added_at`: DateTime
