import redis
import sys

cache = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True,
    socket_connect_timeout=2
)

try:
    cache.ping()
    print("Успешно: Redis подключен!")
except redis.ConnectionError:
    print("Ошибка: Redis сервер не отвечает.")
    print("Попробуй в терминале: redis-cli ping")
    sys.exit()


def get_fibonacci(n):
    if n <= 1: return n

    cached_val = cache.get(f"fib:{n}")
    if cached_val:
        return int(cached_val)

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        cache.set(f"fib:{i}", b)
    return b


n = int(input("Введите число: "))
print(f"Результат: {get_fibonacci(n)}")