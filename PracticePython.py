#Problems
"""
Copyright: https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html

1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******

"""

#Variables
a = 5
b = 7
c = 6
lista = "Este es el recorrido de una vaca en un pastizal"
listNumbers = [1,2,3,4]
vowel = "E"
list_inverse = "Sergio Antonio Aguilar Basto"
word = "radar"

nested_list_1 = [1,2,3,4,5,6]
nested_list_2 = [6,7,8,9,10,11]

list_procedures = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]

#Functions
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
    
def max (a,b):
    if a > b:
        return a
    else: 
        return b
    
def calculate_long_string (stringTemp):
    cont = 0;
    for x in stringTemp:
        cont+=1
    return cont

def identify_vowel(charTemp):
    if charTemp == "a" or charTemp=="e" or charTemp=="i" or charTemp=="o" or charTemp=="u":
        return True
    elif charTemp== "A" or charTemp=="E" or charTemp=="I" or charTemp=="O" or charTemp== "U":
        return True
    else:
        return False

def addNumber (list):
    cont = 0
    for x in list:
        cont = cont+x
    return cont

def multiplyNumber (list):
    cont = 1
    for x in list:
        cont = cont * x
    return cont

def inverse_string(inverse_temp):    
    result = "";
    for x in range(len(inverse_temp),0,-1):                       
        result+=inverse_temp[x-1]    
    return result

def palindrome(word):
    inverse = inverse_string(word)
    if (inverse == word):
        return True
    else:
        return False

def superposition(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False

def generate_n_character(quantity, character):
    result = ""
    for x in range(quantity):
        result+= character
    return result

def procedures(temp_list_procedures):
    result = ""
    for x in temp_list_procedures:        
        result += temp_list_procedures[x-1] * '*' + "\n"
    return result

#Solutions
print("1. El mayor es: ", max(a,b))
print("2. El mayor de tres es: ", max_of_three(a,b,c))
print("3. La longitud de la cadena es: ", calculate_long_string(lista))
print("4. The character: ", vowel ," was identified as vowel: ",identify_vowel(vowel))
print("5. Results were: Add: ", addNumber(listNumbers), "| Multiply: ",multiplyNumber(listNumbers))
print("6. The inverse of string is:", inverse_string(list_inverse))
print("7. This word is palindrome: ", palindrome(word))
print("8. Are there the same elements in both lists? : ", superposition(nested_list_1, nested_list_2))       
print("9. The new word generate is: ", generate_n_character(10, 'x'))
print("10. The procedure was: \n",procedures(list_procedures))