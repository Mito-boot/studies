import re

f = open('/home/mito/Рабочий стол/adr.txt', 'r')


def adr():
    list_adr = re.findall(r"(?:\b[А-Я][А-Я\s]{2,}[А-Я]\b)", f.read())
    return list_adr
if __name__ == '__main__':
    print(adr())