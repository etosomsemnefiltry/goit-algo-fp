items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортируем еду по убыванию соотношения калорий/стоимость
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(item)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    # Таблица для хранения максимальных калорий
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, data = item_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Находим, какая еда была выбрана
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, data = item_list[i - 1]
            selected_items.append(item_name)
            w -= data["cost"]

    return selected_items, dp[n][budget]

budget = 100

print("Жадный алгоритм:")
selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(f"Выбрано: {selected_items_greedy}")
print(f"Общая стоимость: {total_cost_greedy}, Общие калории: {total_calories_greedy}")

print("\nДинамическое программирование:")
selected_items_dp, max_calories_dp = dynamic_programming(items, budget)
print(f"Выбрано: {selected_items_dp}")
print(f"Максимальные калории: {max_calories_dp}")
