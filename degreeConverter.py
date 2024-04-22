def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Ingrese los grados F° que desea convertir a C°: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print("Los {} F° pasan a {} C°".format(fahrenheit, celsius))