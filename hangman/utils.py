def is_word_guessed(secret_word, letters_guessed):
    retv = True

    for letter in secret_word:
        if letter not in letters_guessed:
            retv = False

    return retv
