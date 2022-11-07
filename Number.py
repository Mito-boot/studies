import re

f = open('/home/mito/Рабочий стол/Number.txt', 'r')

def repl(m):
    return str(float(m[0])**3)

def sub():
    list_cub = re.sub(r'(?:\d+[.]\d+)|(?:\d+)', repl, f.read())
    return list_cub

if __name__ == '__main__':
    print(sub())