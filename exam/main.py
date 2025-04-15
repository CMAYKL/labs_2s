# Функція приймає число і повертає список з цією кількістю елементів (наприклад, список чисел від 0 до a-1)

def generate_list(a):
    if not isinstance(a, int) or a < 0:
        raise ValueError("Число має бути цілим і невід'ємним")
    return list(range(a))

# Приклад запуску функції
if __name__ == "__main__":
    number = 5
    result = generate_list(number)
    print(f"Список з {number} елементів: {result}")

