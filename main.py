#string slicing
name = 'Flavian Onyango'
print(name[::-1])

#counting the number of vowels in a string
name = 'Flavian'
my_vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in name:
    if char in my_vowels:
        count += 1
print(count)

#title method, capitalize method
name = 'mephia stephane'
print(name.title())
print(name.capitalize())

#strip method
my_world = '   My world needs you   '
print(my_world.strip())

#split method
snack ='I love pizza'
print(snack.split())

#replace method
name = 'My name is Marian Onyango'
print(name)
print(name.replace('Marian','Flavian'))

#find method
age = 'eighteen'
print(age.find('i'))

#upper method, lower method
name = 'Flavian Onyango'
print(name.upper())
print(name.lower())





