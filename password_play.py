import secrets
import string
import requests
import hashlib


def generate_password(pass_size):
    safe_symbols = "@#*!$%^&"
    characters = string.ascii_letters + string.digits + safe_symbols
    while True:
        password = "".join(secrets.choice(characters) for _ in range(pass_size))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 2
            and sum(c in safe_symbols for c in password) >= 2
        ):
            if check_password_leak(password) == 0:
                return password


def check_password_leak(password):
    # 1. Создаем SHA-1 хеш пароля и переводим в верхний регистр
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    # 2. Берем первые 5 символов (префикс) и остальную часть (суффикс)
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    # 3. Делаем запрос к API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Ошибка при запросе к API"
    # 4. Ищем наш суффикс в ответе (ответ — список строк вида "СУФФИКС:КОЛИЧЕСТВО")
    for h, count in (line.split(":") for line in response.text.splitlines()):
        if h == suffix:
            return 1
    return 0
