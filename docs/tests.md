# Tests Documentation

This document provides an overview of the test cases for the application. Each test case is
designed to verify the functionality of various endpoints and ensure that the application
behaves as expected.

## Test Files

### `conftest.py`

This file contains fixtures and configurations for the test environment.

- **pytest_sessionstart**: Hook to check database connectivity before running tests.
- **test_db_engine**: Fixture to create and drop the test database schema.
- **test_db_session**: Fixture to provide a database session for each test.
- **test_client**: Fixture to provide a test client for making HTTP requests.

### `test_task.py`

This file contains tests for the task-related endpoints.

- **test_create_task**: Tests the creation of a new task.
- **test_get_tasks**: Tests retrieving all tasks.
- **test_get_task**: Tests retrieving a single task by ID.
- **test_update_task**: Tests updating an existing task.
- **test_delete_task**: Tests deleting a task.

### `test_schedule_task.py`

This file contains tests for the schedule task-related endpoints.

- **test_create_schedule_task**: Tests the creation of a new schedule task.
- **test_get_schedule_tasks**: Tests retrieving all schedule tasks.
- **test_get_schedule_task**: Tests retrieving a single schedule task by schedule ID and task ID.
- **test_delete_schedule_task**: Tests deleting a schedule task.

### `test_auth.py`

This file contains tests for the authentication-related endpoints.

- **test_register_user**: Tests user registration.
- **test_login_user**: Tests user login.
- **test_get_info_current_user**: Tests retrieving information about the current user.
- **test_reset_password_user**: Tests resetting a user's password.

### `test_notification.py`

This file contains tests for the notification-related endpoints.

- **test_create_notification**: Tests the creation of a new notification.
- **test_get_notifications**: Tests retrieving all notifications.
- **test_get_notification**: Tests retrieving a single notification by ID.
- **test_update_notification**: Tests updating an existing notification.
- **test_delete_notification**: Tests deleting a notification.

### `test_priority.py`

This file contains tests for the priority-related endpoints.

- **test_create_priority**: Tests the creation of a new priority.
- **test_get_priorities**: Tests retrieving all priorities.
- **test_get_priority**: Tests retrieving a single priority by ID.
- **test_update_priority**: Tests updating an existing priority.
- **test_delete_priority**: Tests deleting a priority.

### `test_schedule.py`

This file contains tests for the schedule-related endpoints.

- **test_create_schedule**: Tests the creation of a new schedule.
- **test_get_schedules**: Tests retrieving all schedules.
- **test_get_schedule**: Tests retrieving a single schedule by ID.
- **test_update_schedule**: Tests updating an existing schedule.
- **test_delete_schedule**: Tests deleting a schedule.

### `test_user.py`

This file contains tests for the user-related endpoints.

- **test_create_user**: Tests the creation of a new user.
- **test_get_users**: Tests retrieving all users.
- **test_get_user**: Tests retrieving a single user by ID.
- **test_update_user**: Tests updating an existing user.
- **test_delete_user**: Tests deleting a user.

### `test_time_entry.py`

This file contains tests for the time entry-related endpoints.

- **test_create_time_entry**: Tests the creation of a new time entry.
- **test_get_time_entries**: Tests retrieving all time entries.
- **test_get_time_entry**: Tests retrieving a single time entry by ID.
- **test_update_time_entry**: Tests updating an existing time entry.
- **test_delete_time_entry**: Tests deleting a time entry.
