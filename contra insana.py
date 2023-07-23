# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Generador de contraseñas insanas!")
nr_letters = int(input("Cuantas letras te gustarian?\n"))
nr_symbols = int(input(f"Cuantos simbolos quieres?\n"))
nr_numbers = int(input(f"Cuantos numeros quieres ahora pa cerrar trato?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = (
    random.sample(letters, nr_letters)
    + random.sample(numbers, nr_numbers)
    + random.sample(symbols, nr_symbols)
)
random.shuffle(password)

# Convert the list of characters into a single string
password_str = "".join(password)
print(f"Tu contraseña insana es: 😈😈😈😈 + " " + {password_str}")
