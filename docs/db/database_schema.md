# Database Schema

## User

- `id`: Integer, Primary Key
- `first_name`: String
- `last_name`: String
- `username`: String
- `email`: String
- `password_hash`: String

## Priority

- `id`: Integer, Primary Key
- `name`: String

## Task

- `id`: Integer, Primary Key
- `description`: String
- `deadline`: DateTime
- `priority_id`: Integer, Foreign Key
- `user_id`: Integer, Foreign Key

## Schedule

- `id`: Integer, Primary Key
- `user_id`: Integer, Foreign Key
- `date`: DateTime

## ScheduleTask

- `schedule_id`: Integer, Foreign Key, Primary Key
- `task_id`: Integer, Foreign Key, Primary Key
- `added_at`: DateTime

## TimeEntry

- `id`: Integer, Primary Key
- `task_id`: Integer, Foreign Key
- `start_time`: DateTime
- `end_time`: DateTime
- `duration`: Integer

## Notification

- `id`: Integer, Primary Key
- `task_id`: Integer, Foreign Key
- `message`: String
- `sent_at`: DateTime
