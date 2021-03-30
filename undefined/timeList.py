breakTime = 5
lessonTime = 45
startTime = 8 * 60


def getFullTime(minuties):
    return '{:02}:{:02}'.format(minuties // 60, minuties % 60)


def f():
    lessonNumber = int(input('Введите номер урока: '))
    answer = getFullTime(
        lessonNumber * (breakTime + lessonTime) - breakTime + startTime)
    print(f'{lessonNumber} урок заканчивается в {answer}')


f()
