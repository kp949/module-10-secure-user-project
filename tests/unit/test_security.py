from app.security import hash_password, verify_password


def test_hash_password_does_not_store_plain_text():
    password = "MyPassword123"

    password_hash = hash_password(password)

    assert password_hash != password
    assert password not in password_hash


def test_verify_password_accepts_correct_password():
    password_hash = hash_password("MyPassword123")

    assert verify_password("MyPassword123", password_hash) is True


def test_verify_password_rejects_wrong_password():
    password_hash = hash_password("MyPassword123")

    assert verify_password("WrongPassword123", password_hash) is False


def test_verify_password_rejects_bad_hash_format():
    assert verify_password("MyPassword123", "not-a-valid-hash") is False

