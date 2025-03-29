# Authentication Module

This module provides functions for password hashing, token creation, and token decoding.

## Functions

### `get_password_hash`

Hashes a plaintext password using bcrypt.

- **Parameters:**
  - `password` (str): The plaintext password to hash.
- **Returns:**
  - `str`: The hashed password.

### `verify_password`

Verifies a plaintext password against a hashed password.

- **Parameters:**
  - `plain_password` (str): The plaintext password to verify.
  - `hashed_password` (str): The hashed password to verify against.
- **Returns:**
  - `bool`: `True` if the passwords match, `False` otherwise.

### `create_access_token`

Creates a JWT access token.

- **Parameters:**
  - `data` (str): The data to include in the token payload.
  - `expiry` (timedelta, optional): The token expiry time. Defaults to 60 minutes.
  - `refresh` (bool, optional): Whether the token is a refresh token. Defaults to `False`.
- **Returns:**
  - `str`: The encoded JWT token.

### `decode_token`

Decodes a JWT token and returns its payload.

- **Parameters:**
  - `token` (str): The JWT token to decode.
- **Returns:**
  - `dict`: The token payload.
- **Raises:**
  - `HTTPException`: If the token is expired, invalid, or not yet valid.

## Dependencies

The `dependencies.py` file provides classes for token validation and verification.

### `TokenBearer`

A base class for token validation.

- **Methods:**
  - `__call__`: Validates the token from the request header.
  - `token_valid`: Checks if the token is valid.
  - `verify_token_data`: Abstract method to be overridden in child classes.

### `AccessTokenBearer`

A class for access token validation.

- **Methods:**
  - `verify_token_data`: Verifies the token data.
