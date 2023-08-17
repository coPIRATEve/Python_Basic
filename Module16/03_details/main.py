shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
         ['педаль', 100], ['седло', 1500], ['рама', 12000],
         ['обод', 2000], ['шатун', 200], ['седло', 2700]]
total_count = 0
total_cost = 0

print("Наш ассортимент:", shop)

part_name = input("Название детали: ")

for item in shop:
         if item[0] == part_name:
                 total_count += 1
                 total_cost += item[1]

print(f"Кол-во деталей — {total_count}")
print(f"Общая стоимость — {total_cost}")

