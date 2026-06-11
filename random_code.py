import random

def generate_code(length=6):
    """Генерирует случайный цифровой код заданной длины."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

if __name__ == "__main__":
    code = generate_code()
    print(f"Случайный 6-значный код: {code}")
    
    # Пример: сгенерировать 5 уникальных кодов
    codes = set()
    while len(codes) < 5:
        codes.add(generate_code())
    print("Уникальные коды:", sorted(codes))
