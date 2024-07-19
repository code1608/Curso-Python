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


#Comprobación de datos 

second_name = "Esteban"
second_lastname = "Vasquez"
print(type(second_name))
print(len(second_name))

print(type([1,2,3]))
print(type({'name', 'age', 17, 0.8}))
print(type((1,2,3)))
print(type({'age': 17}))

#Conversión de tipo de datos --> se usa int(), float(), str(), list, set

#De entero a float

num_int = 10
print('num_int', num_int) 
print(type(num_int))

num_float = float(num_int)
print("Este es un numero de entero a float", num_float)
print(type(num_float))

#De float a entero
gravity = 9.81
print(int(gravity))
print(type(gravity))

#De entero a str

num = 10
print(str(num))
va = type(str(num))
print("Es de tipo", va)



num_str = '10.2'
print(num_str)
print(type(num_str))

f = 57
print(float(f))
print(type(float(f)))

i = 10.2

print(int(i))
print(type(int(i)))

c = 12
print(str(c))
print(type(str(c)))

user = "Carl"
lines = 50

#Usar la (,) o (+) no los dos juntos
print("Hola mundo, " + "Soy " + user +  str(lines) + " lineas de codigos")


num_str = '10.6'
num_float = float(num_str)
print("Este es un str a float",num_float)
print(type(num_float))

num_int = int(num_float)
print("Este es un str a float a int", num_int)
print(type(num_int))

