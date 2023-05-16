weather = float(input())

if 35.00 < weather or weather <= 5.0:
    print("unknown")
elif 5.00 <= weather <= 11.9:
    print("Cold")
elif 14.9 >= weather:
    print("Cool")
elif 20.0 >= weather:
    print("Mild")
elif 25.9 >= weather:
    print("Warm")
elif 35.00 >= weather:
    print("Hot")