number_load = int(input())
bus = 0
truck = 0
train = 0
total_load = 0
bus_ton = 0
truck_ton = 0
train_ton = 0
tons = 0

for i in range(1, number_load + 1):
    load = int(input())
    tons += load
    if load <= 3:
        bus += load * 200
        bus_ton += load
    elif load <= 11:
        truck += load * 175
        truck_ton += load
    elif load > 11:
        train += load * 120
        train_ton += load

total_load = bus + train + truck


average_per_ton = total_load / tons
average_per_ton_bus = (bus_ton / tons) * 100
average_per_ton_truck = (truck_ton / tons) * 100
average_per_ton_train = (train_ton / tons) * 100


print(
    f"{average_per_ton:.2f}\n{average_per_ton_bus:.2f}%\n{average_per_ton_truck:.2f}%\n{average_per_ton_train:.2f}%")