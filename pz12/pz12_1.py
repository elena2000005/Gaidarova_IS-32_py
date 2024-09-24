# Функция для создания новой последовательности
def generate_sequence(nums):
    return [((nums[i-1] + nums[i+1]) ** 2) for i in range(1, len(nums) - 1)]

# Пример использования
n = [2, 5, 8, 3, 9]  # пример исходной последовательности
new_sequence = generate_sequence(n)
print("Новая последовательность:", new_sequence)
