from unicodedata import normalize, combining


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold()


# deletion all diacretic signs
def shave_marks(txt):
    norm_txt = normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not combining(c))
    return normalize('NFC', shaved)
