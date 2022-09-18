num = input('Введите число от 1 до 999999: ')
res = list(num)
len_check = len(res)
out = []

while len(res) < 6:
    zero = ['0']
    res = zero + res    
if res[0] != '0':
    if res[0] == '1': a0 = 'сто'
    if res[0] == '2': a0 = 'двести'
    if res[0] == '3': a0 = 'триста'
    if res[0] == '4': a0 = 'четыреста'
    if res[0] == '5': a0 = 'пятьсот'
    if res[0] == '6': a0 = 'шестьсот'
    if res[0] == '7': a0 = 'семьсот'
    if res[0] == '8': a0 = 'восемьсот'
    if res[0] == '9': a0 = 'девятьсот'
    out.append(a0)
    
if res[1] != '0':
    
    if res[1] == '2': a1 = 'двадцать'
    if res[1] == '3': a1 = 'тридцать'
    if res[1] == '4': a1 = 'сорок'
    if res[1] == '5': a1 = 'пятьдесят'
    if res[1] == '6': a1 = 'шестьдесят'
    if res[1] == '7': a1 = 'семьдесят'
    if res[1] == '8': a1 = 'восемьдесят'
    if res[1] == '9': a1 = 'девяносто'
    if res[1] == '1':
        if res[2] == '0': a1 = 'десять'
        if res[2] == '1': a1 = 'одиннадцать'
        if res[2] == '2': a1 = 'двенадцать'
        if res[2] == '3': a1 = 'тринадцать'
        if res[2] == '4': a1 = 'четырнадцать'
        if res[2] == '5': a1 = 'пятнадцать'
        if res[2] == '6': a1 = 'шестнадцать'
        if res[2] == '7': a1 = 'семнадцать'
        if res[2] == '8': a1 = 'восемнадцать'
        if res[2] == '9': a1 = 'девятнадцать'
    out.append(a1)
    
if res[2] != '0':
    if res[1] != '1':
        if res[2] == '1': a2 = 'одна'
        if res[2] == '2': a2 = 'две'
        if res[2] == '3': a2 = 'три'
        if res[2] == '4': a2 = 'четыре'
        if res[2] == '5': a2 = 'пять'
        if res[2] == '6': a2 = 'шесть'
        if res[2] == '7': a2 = 'семь'
        if res[2] == '8': a2 = 'восемь'
        if res[2] == '9': a2 = 'девять'
        out.append(a2)
        
if len_check > 3:
    out.append('тысяч')
if res[2] != '0':
    if res[1] != '1':
        if res[2] == '1':
            out.pop()
            out.append('тысяча') 
        if res[2] == '2':
            out.pop()
            out.append('тысячи')
        if res[2] == '3':
            out.pop()
            out.append('тысячи')
        if res[2] == '4':
            out.pop()
            out.append('тысячи')
            
if res[3] != '0':
    if res[3] == '1': a3 = 'сто'
    if res[3] == '2': a3 = 'двести'
    if res[3] == '3': a3 = 'триста'
    if res[3] == '4': a3 = 'четыреста'
    if res[3] == '5': a3 = 'пятьсот'
    if res[3] == '6': a3 = 'шестьсот'
    if res[3] == '7': a3 = 'семьсот'
    if res[3] == '8': a3 = 'восемьсот'
    if res[3] == '9': a3 = 'девятьсот'
    out.append(a3)
    
if res[4] != '0':
    if res[4] == '2': a4 = 'двадцать'
    if res[4] == '3': a4 = 'тридцать'
    if res[4] == '4': a4 = 'сорок'
    if res[4] == '5': a4 = 'пятьдесят'
    if res[4] == '6': a4 = 'шестьдесят'
    if res[4] == '7': a4 = 'семьдесят'
    if res[4] == '8': a4 = 'восемьдесят'
    if res[4] == '9': a4 = 'девяносто'
    if res[4] == '1':
        if res[5] == '0': a4 = 'десять'
        if res[5] == '1': a4 = 'одиннадцать'
        if res[5] == '2': a4 = 'двенадцать'
        if res[5] == '3': a4 = 'тринадцать'
        if res[5] == '4': a4 = 'четырнадцать'
        if res[5] == '5': a4 = 'пятнадцать'
        if res[5] == '6': a4 = 'шестнадцать'
        if res[5] == '7': a4 = 'семнадцать'
        if res[5] == '8': a4 = 'восемьадцать'
        if res[5] == '9': a4 = 'девятнадцать'
    out.append(a4)
    
if res[5] != '0':
    if res[4] != '1':
        if res[5] == '1': a5 = 'один'
        if res[5] == '2': a5 = 'два'
        if res[5] == '3': a5 = 'три'
        if res[5] == '4': a5 = 'четыре'
        if res[5] == '5': a5 = 'пять'
        if res[5] == '6': a5 = 'шесть'
        if res[5] == '7': a5 = 'семь'
        if res[5] == '8': a5 = 'восемь'
        if res[5] == '9': a5 = 'девять'
        out.append(a5)
out.append('рублей')

if res[5] != '0':
    if res[4] != '1':
        if res[5] == '1':
            out.pop()
            out.append('рубль') 
        if res[5] == '2':
            out.pop()
            out.append('рубля')
        if res[5] == '3':
            out.pop()
            out.append('рубля')
        if res[5] == '4':
            out.pop()
            out.append('рубля')
print(str.capitalize(' '.join(out)))
