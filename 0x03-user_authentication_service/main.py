#!/usr/bin/env python3
"""End-to-end integration tests for the authentication service"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Test user registration"""
    response = requests.post(f"{BASE_URL}/users",
                             data={"email": email, "password": password})
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}")
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with wrong password"""
    response = requests.post(f"{BASE_URL}/sessions",
                             data={"email": email, "password": password})
    assert response.status_code == 401, (
        f"Expected status code 401, got {response.status_code}")


def log_in(email: str, password: str) -> str:
    """Test login with correct credentials"""
    response = requests.post(f"{BASE_URL}/sessions",
                             data={"email": email, "password": password})
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}")
    assert "session_id" in response.cookies
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """Test profile access without logging in"""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403, (
        f"Expected status code 403, got {response.status_code}")


def profile_logged(session_id: str) -> None:
    """Test profile access when logged in"""
    response = requests.get(f"{BASE_URL}/profile",
                            cookies={"session_id": session_id})
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}")
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """Test logout"""
    response = requests.delete(f"{BASE_URL}/sessions",
                               cookies={"session_id": session_id})
    assert response.status_code == 302, (
        f"Expected status code 302, got {response.status_code}")


def reset_password_token(email: str) -> str:
    """Test password reset token generation"""
    response = requests.post(f"{BASE_URL}/reset_password",
                             data={"email": email})
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}")
    assert "email" in response.json() and "reset_token" in response.json()
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test password update"""
    response = requests.put(
        f"{BASE_URL}/reset_password",
        data={"email": email,
              "reset_token": reset_token,
              "new_password": new_password}
    )
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}")
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)

# print("All tests passed successfully!")
