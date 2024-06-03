def bank(X, Y):
    # Начальная сумма вклада
    total_amount = X
    # Процентная ставка
    interest_rate = 0.25

    # Расчет суммы вклада с учетом сложных процентов
    for _ in range(Y):
        # Увеличение суммы вклада на процент от текущей суммы
        total_amount += total_amount * interest_rate

    return total_amount

# Пример использования функции:
# X = 10000 рублей, Y = 5 лет
final_amount = bank(10000, 5)
print(f"Сумма на счету после 5 лет: {final_amount} рублей")