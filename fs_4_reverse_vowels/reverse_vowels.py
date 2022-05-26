def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    Vowels = set("aeiou")
    stri = list(s)
    a = 0
    b = len(s) - 1
    while a < b:
        if stri[a].lower() not in Vowels:
            i += 1
        elif stri[b].lower() not in Vowels:
            b -= 1
        else:
            stri[a], stri[b] = stri[b], stri[a]
            a += 1
            b -= 1
    return "".join(stri)
