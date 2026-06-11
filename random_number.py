import random

def get_random_number():
    """Возвращает случайное число от 1 до 100."""
    return random.randint(1, 100)

if __name__ == "__main__":
    num = get_random_number()
    print(f"Случайное число от 1 до 100: {num}")
