"""Password hashing helpers."""

import hashlib
import secrets


ALGORITHM = "pbkdf2_sha256"
ITERATIONS = 120_000


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        ITERATIONS,
    ).hex()
    return f"{ALGORITHM}${ITERATIONS}${salt}${password_hash}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        algorithm, iterations, salt, password_hash = stored_hash.split("$", 3)
        if algorithm != ALGORITHM:
            return False

        check_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            int(iterations),
        ).hex()
        return secrets.compare_digest(check_hash, password_hash)
    except (ValueError, TypeError):
        return False

