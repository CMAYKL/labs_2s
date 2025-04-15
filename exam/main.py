# функція на вхід отримує число а на вихід повинна повернути список з кількістю елементів (яка була передана) відповідно цьому числу

def generate_list(a):
    if not isinstance(a, int) or a < 0:
        raise ValueError("Число має бути цілим і невід'ємним")
    return list(range(a))

if __name__ == "__main__":
    number = 5
    result = generate_list(number)
    print(f"Список з {number} елементів: {result}")

