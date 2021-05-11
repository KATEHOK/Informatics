# Текстовый файл 24-s1.txt состоит не более чем из 106 заглавных латинских букв (A..Z). Текст разбит на строки различной длины. Определите количество строк, в которых встречается комбинация A*R, где звёздочка обозначает любой символ.
# E:/Py_scr/stat_grad/Informatics/undefined/24-polyakov.txt
link = 'E:/Py_scr/stat_grad/Informatics/undefined/24-polyakov.txt'
values = [
    'AAR', 'ABR', 'ACR', 'ADR', 'AER', 'AFR', 'AGR', 'AHR',
    'AIR', 'AJR', 'AKR', 'ALR', 'AMR', 'ANR', 'AOR', 'APR',
    'AQR', 'ARR', 'ASR', 'ATR', 'AUR', 'AVR', 'AWR', 'AXR',
    'AYR', 'AZR'
]


def isLineCorrect(line):
    for string in values:
        if string in line:
            return True
    return False


with open(link, 'r') as dataFile:
    counter = 0
    for line in dataFile:
        if isLineCorrect(line):
            counter += 1
print(counter)  # 784
