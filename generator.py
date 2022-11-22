import sys
import random
import string
password = []
password_length = int(input("Jak długie ma być hasło?"))
characters_left = -1

def update_characters_left (number_of_characters):
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znaków spoza przedziałów 0,", characters_left)
        sys.exit(0)
    else:
        characters_left -= lowercase_letters
        print("Pozostało znaków:", characters_left)

if password_length < 5:
    print("Długość hasła za krótka. Musi miec minimum 5 znaków")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("Ile małych liter ma mieć hasło?"))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile dużych liter ma mieć hasło?"))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specialnych ma mieć hasło?"))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło?"))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki zostały wyokrzystane. Hasło zostanie uzupełnione małymi znakami")
    lowercase_letters += characters_left

    print()
    print("Długość hasła:", password_length)
    print("Małe litery:", lowercase_letters)
    print("Duże litery:", uppercase_letters)
    print("Znaki specialne:", special_characters)
    print("cyfry:", digits)

    for _ in range(password_length):
        if lowercase_letters > 0:
            password.append(random.choice(string.ascii_lowercase))
            lowercase_letters -= 1
        if uppercase_letters > 0:
            password.append(random.choice(string.ascii_uppercase))
            uppercase_letters -= 1
        if special_characters > 0:
            password.append(random.choice(string.punctuation))
            special_characters -= 1
        if digits > 0:
            password.append(random.choice(string.digits))
            digits -= 1

    random.shuffle(password)
    print("Wygenerowane hasło:", "".join(password))

    #powinnismy zastosowac validacje, sprawdzić czy uzytkownik zawsze podaje licze gdy trzeba liczbe,
    #gdy uzytkownik nie poda, wtedy powinnismy poprosic o podanie własiwej wartości
    #powinnismy podac usytownikowi mozliwosc na poprawienie bledu
    #gdy uzytkownik poda liczbe spoza zdefiniowanego przedziału, zamiast wyłączyć program, powinniśmy pozwolić
    #uzytkownikowi na poprawienie swojego błędu
    #gdy zla długosc hasła, powinnismy powiedziec haslo jest za krotkie podaj wieksza liczbę

    