import re

# def regyl (x):
#     if re.fullmatch(r'\w\d\d\d\w\w\d\d\d', x):
#         return 'Private'
#     elif re.fullmatch(r'\w\d\d\d\w\w\d\d', x):
#         return 'Private'
#     elif re.fullmatch(r'\w\w\d\d\d\d\d', x):
#         return 'Taxi'
#     elif re.fullmatch(r'\w\w\d\d\d\d\d\d', x):
#         return 'Taxi'
#     else:
#         return 'Fail'

f = open('/home/mito/Рабочий стол/email.txt', 'r')
def mail():
    list_mail = re.findall(r"\w[a-z'_+-]+@[a-z-]+\.?[a-z]+", f.read())
    return list_mail


    print(mail())
    print(regyl('СD2757'))

