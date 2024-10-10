# test_get_secret.py
from utils import get_secret

SECRET_ID = 'e6q4gb0idnb5p6kmk77m'  # Убедитесь, что вы используете правильный идентификатор секрета

try:
    secret_key = get_secret(SECRET_ID)
    print(f"Секретный ключ успешно получен: {secret_key}")
except Exception as e:
    print(f"Ошибка при получении секрета: {e}")
