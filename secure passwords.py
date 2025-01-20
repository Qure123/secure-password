def num_is_valid(): #checking numbers for validity
    while True:
        qt_iter = input('Введите количество паролей для генерации (числом): ')
        len_pas = input('Введите Длину одного пароля (числом): ')
        if qt_iter.isdigit():
            if len_pas.isdigit():
                return map(int, [qt_iter, len_pas])
        else:
            print('Введите именно цифры!')
            continue
def check_answ(answer): #checking answers for validity
    while True:
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            answer = input('Повторите еще раз. Введите именно yes или no: ')
            continue
def generate_password(chars, len_pas): #generating passwords
    print(''.join(sample(chars, len_pas)))
from random import sample
digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
qt_iter, len_pas = num_is_valid()
chars = ''
num_inpas = check_answ(input('Включать ли цифры 0123456789?(yes/no): '))
up_let = check_answ(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(yes/no): '))
dn_let = check_answ(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?(yes/no): ')) 
sp_char = check_answ(input('Включать ли символы "!#$%&*+-=?@^_"?(yes/no): '))
controversial_ch = check_answ(input('Исключать ли неоднозначные символы il1Lo0O?(yes/no): '))
if num_inpas:
    chars += digits
if up_let:
    chars += uppercase_letters
if dn_let:
    chars += lowercase_letters
if sp_char:
    chars += punctuation
if controversial_ch:
    for c in 'il1Lo0O':
        chars.replace(c,'')
if len(chars) < len_pas:
    print('Увы, список допустимых символов меньше, чем длина пароля')
else:
    print('Ваши пароли:')
    for i in range(qt_iter):
        generate_password(chars,len_pas)