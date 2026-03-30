import hashlib
import requests
import time


def check_password_leak(password):
    # 1. Создаем SHA-1 хеш пароля и переводим в верхний регистр
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    print(sha1_password)
    time.sleep(0)
    # 2. Берем первые 5 символов (префикс) и остальную часть (суффикс)
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    # 3. Делаем запрос к API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Ошибка при запросе к API"

    # 4. Ищем наш суффикс в ответе (ответ — список строк вида "СУФФИКС:КОЛИЧЕСТВО")
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return 1

    return 0


# Пример проверки
print(check_password_leak("password123"))
