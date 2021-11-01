letters = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "ye",
    "ё": "yo",
    "ж": "j",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "sh",
    "ъ": "",
    "ы": "i",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}

symbols = {'`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}',
           '}', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/'}


def translate(word):
    eng_word = ""
    for i in str(word.replace(" ", "_")):
        if i in symbols:
            continue
        try:
            eng_word += letters[i.lower()]
        except KeyError:
            eng_word += i
    return eng_word