# C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/24/24.txt
# функция возвращает True, если буква по idLetter стоит между двумя одинаковыми буквами
def isLetterCorrectById(idLetter, inputStr):
    if inputStr[idLetter - 1] == inputStr[idLetter + 1]:
        return True
    return False


dictionary = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0
}
with open("C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/24/24.txt", "r") as data:
    inputStr = data.read()
print(len(inputStr))
