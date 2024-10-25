import random
import matplotlib.pyplot as plt

# Функция для симуляции бросков кубиков
def monte_carlo_simulation(num_rolls):
    results = [0] * 13  # Массив для подсчета частоты выпадения сумм
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        result_sum = dice1 + dice2
        results[result_sum] += 1  # Увеличиваем счетчик

    # Преобразуем частоты в вероятности
    probabilities = [count / num_rolls for count in results]
    return probabilities[2:]

# Теоретические вероятности выпадения каждой суммы
theoretical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Количество бросков кубиков
num_rolls = 10000
simulated_probabilities = monte_carlo_simulation(num_rolls)

# Создаем график
x = list(range(2, 13))  # Суммы от 2 до 12
theoretical_values = [theoretical_probabilities[sum_] for sum_ in x]


plt.figure(figsize=(10, 6))
plt.bar(x, simulated_probabilities, width=0.4, label="Монте-Карло", align="center", color="skyblue")
plt.bar([i + 0.4 for i in x], theoretical_values, width=0.4, label="Теоретические значения", align="center", color="orange")

plt.xlabel("Сумма чисел на двух кубиках")
plt.ylabel("Вероятность")
plt.title(f"Сравнение вероятностей сумм чисел (Монте-Карло и Теоретически)\nКол-во бросков: {num_rolls}")
plt.xticks(x)
plt.legend()
plt.show()
