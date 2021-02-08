# -*- coding:utf-8 -*-

def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True

    return False


def palindrome(word): 
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True

    return False


if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))
    # rta = palindrome(word)
    rta = palindrome2(word)

    if rta:
        print('La palabra "{}" es un Palindromo'. format(word))
    else:
        print('La palabra "{}" NO es un Palindromo'. format(word))

