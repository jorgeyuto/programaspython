print("Ingrese el año: ")
year = int(input())
if not year % 4 == 0:
    if not year % 100 == 0:
        if not year % 400 == 0:
            print("Es año común")
        else:
           print("Es una año bisiesto")
    else:
        print("Es un año común")
else:
    print("Es un año bisiesto")
