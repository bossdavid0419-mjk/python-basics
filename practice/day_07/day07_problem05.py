def calculate_final_price(price, discount_rate):
    final_price = price * (1 - discount_rate/100)

    return round(final_price, 2)

result = calculate_final_price(10000, 20)
print(result)