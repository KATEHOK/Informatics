# C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/24/24.txt
# функция возвращает True, если буква по idLetter стоит между двумя одинаковыми буквами
def isLetterCorrectById(idLetter, inputStr):
    if inputStr[idLetter - 1] == inputStr[idLetter + 1]:
        return True
    return False


with open("C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/24/24.txt", "r") as data:
    inputStr = data.read()
print(len(inputStr))
