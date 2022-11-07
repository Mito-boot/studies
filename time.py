import re

f = open('/home/mito/Рабочий стол/time.txt', 'r')

def time():
    list_time = re.sub(r"(([0-1][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9])|([0-1][0-9]|[2][0-3]):[0-5][0-9]", '(TBD)', f.read())
    return list_time
if __name__ == '__main__':
    print(time())