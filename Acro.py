import re

f = open('/home/mito/Рабочий стол/Test/Акроним.txt', 'r')

def acro():
    list_acronim = ''
    list_acro = re.findall(r'\b\w', f.read())
    for x in list_acro:
        list_acronim += x
    return list_acronim.upper()



if __name__ == '__main__':
    print(acro())