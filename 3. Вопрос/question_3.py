def max_sum(nums):
    # Проверяем, что список содержит хотя бы два числа
    if len(nums) < 2:
        return None

    # Инициализируем две переменные для хранения двух наибольших чисел
    max1 = max(nums[0], nums[1])
    max2 = min(nums[0], nums[1])

    # Проходим по остальным числам в списке
    for i in range(2, len(nums)):
        # Если текущее число больше max1, обновляем значения max1 и max2
        if nums[i] > max1:
            max2 = max1
            max1 = nums[i]
        # Если текущее число больше max2, обновляем значение max2
        elif nums[i] > max2:
            max2 = nums[i]

    # Возвращаем сумму двух наибольших чисел
    return max1 + max2

# Пример использования функции
nums = [2, 7, 4, 1, 8]
result = max_sum(nums)
print(result)