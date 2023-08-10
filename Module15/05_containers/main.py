containers = []

N = int(input('Кол-во контейнеров: '))

for i in range(N):
    weight = int(input(f'вес {i+1} контейнера: '))
    containers.append(weight)

new_container_weight = int(input("Введите вес нового контейнера: "))

position = 1
while position <= N and new_container_weight <= containers[position - 1]:
    position += 1

print("Номер, который получит новый контейнер:", position)



