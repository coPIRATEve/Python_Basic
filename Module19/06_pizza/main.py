orders = {}
n = int(input("Введите количество заказов: "))
for i in range(n):
    order_info = input(f"Введите информацию о {i + 1}-м заказе: ")
    customer, pizza, quantity = order_info.split()
    quantity = int(quantity)
    if customer in orders:
        if pizza in orders[customer]:
            orders[customer][pizza] += quantity
        else:
            orders[customer][pizza] = quantity
    else:
        orders[customer] = {pizza: quantity}
for customer in sorted(orders.keys()):
    print(customer + ":")
    for pizza, quantity in sorted(orders[customer].items()):
        print(f"\t{pizza}: {quantity}")
