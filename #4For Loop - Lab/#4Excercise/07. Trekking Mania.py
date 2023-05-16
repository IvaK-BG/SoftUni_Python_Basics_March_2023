number_of_groups = int(input())
total_people = 0
musala = 0
monblan = 0
kalimandjaro = 0
k2 = 0
everest = 0
five_p_gr = 0
six_p_gr = 0
thirteen_p_gr = 0
twentysix_p_group = 0
over_fortyone_p_group = 0



for groups in range (0, number_of_groups):
    group = int(input())
    total_people += group
    if group <= 5:
        five_p_gr += 1
        musala += group
    elif 5 < group <= 12:
        six_p_gr += 1
        monblan += group
    elif 12 < group <= 25:
        thirteen_p_gr += 1
        kalimandjaro += group
    elif 25 < group <= 40:
        twentysix_p_group += 1
        k2 += group
    elif group > 40:
        over_fortyone_p_group += 1
        everest += group

musala_percent = musala / total_people * 100
monblan_percent = monblan / total_people * 100
kalimandjaro_percent = kalimandjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kalimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")




