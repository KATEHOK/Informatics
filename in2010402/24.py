with open('E:/Py_scr/stat_grad/Informatics/in2010402/files/24/24.txt', 'r') as data:
    minStr = data.readline()
    minCount = minStr.count('N')
    for line in data:
        localCount = line.count('N')
        if localCount < minCount:
            minCount = localCount
            minStr = line
alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
            'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
maxCount = 0
let = ''
for letter, counter in alphabet.items():
    alphabet[letter] = minStr.count(letter)
    if maxCount <= alphabet[letter]:
        maxCount = alphabet[letter]
        let = letter
print(let, maxCount)
