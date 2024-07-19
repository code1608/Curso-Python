#Día 2 - 30 día - python

#Variables --> Skane_case

name = "David"
last_name = "Ramírez"
country = "Colombia"
age = 17
is_married = True
skills = ['HTML', 'Css', 'JS']

#longitud del dato con la función len

print(name)
print(f"Contiene {len(name)} letras {name}")
print(last_name)
print(country)
print(f"El Pais {country} tiene {len(country)} letras")
print(age)
print(is_married)
print(skills)

#Información de entrada por usuario --> input

first_name = input("Ingrese su primer nombre: ")
last_name = input("Ingrese su apellido: ")

print(f"Usted se llama {first_name}")
print(f"Su apellido es {last_name}")