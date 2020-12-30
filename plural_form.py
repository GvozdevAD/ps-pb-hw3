def plural_form(quantity, without_declination, first_declension, second_declension):
    """
    Функция согласования окончаний существительных 
    в зависимости от переданного числа.
    :parm Число
    :parm Склонение существительных в единственном числе
    :parm Склонение существительных с оканчанием на -а 
    :parm Склонение существительных с оканчанием на -ов
    """
    
    num = quantity % 10
    
    if num == 1 and quantity != 11:
        result = f'{quantity} {without_declination}'
    elif (quantity >= 11 and quantity <= 14) or num == 0 or num > 4:
        result = f'{quantity} {second_declension}'
    elif num >= 2 and num <= 4:
        result = f'{quantity} {first_declension}'
    
    return result



print (plural_form(11, 'студент', 'студента', 'студентов'))
print (plural_form(1, 'студент', 'студента', 'студентов'))
print (plural_form(3, 'студент', 'студента', 'студентов'))
print (plural_form(2, 'яблоко', 'яблока', 'яблок'))
print (plural_form(1, 'яблоко', 'яблока', 'яблок'))
print (plural_form(11, 'яблоко', 'яблока', 'яблок'))
