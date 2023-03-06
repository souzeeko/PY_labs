while True:
    email = input("Пожалуйста, введите адрес электронной почты: ")
    if email.endswith("@kpfu.ru") == 0:
        print("Требуется указать адрес в доменной зоне kpfu.ru")
    else:
        break

while True:
    password = input("Пожалуйста, придумайте новый пароль: ")
    c1 = (not password.isalpha())
    c2 = (not password.isdigit())
    c3 = (not password.islower())
    c4 = '!' in password or '“' in password or '#' in password or '$' in password or '%' in password or '&' in password
    c5 = len(password) > 7
    cn = c1 and c1 and c3 and c4 and c5
    if not cn:
        if not c5:
            print("Пароль должен состоять как минимум из 8ми символов")
        elif not c1:
            print("Пароль не может состоять из одних только букв")
        elif not c2:
            print("Пароль не может состоять из одних только цифр")
        elif not c3:
            print("Пароль должен содержать хотя бы одну заглавную букву")
        elif not c4:
            print("Пароль должен содержать хотя бы один спец. символ формата !, “, #, $, %, &")
    else:
        passwordcheck = input("Пожалуйста, введите пароль повторно: ")
        if passwordcheck == password:
            print("Вы успешно прошли регистрацию")
            break
        else:
            passwordcheck = input("Пароли не совпадают, попробуйте ввести пароль повторно: ")
        if passwordcheck == password:
            print("Вы успешно прошли регистрацию")
            break
        else:
            passwordcheck = input("Пароли не совпадают, попробуйте ввести пароль повторно: ")
        if passwordcheck == password:
            print("Вы успешно прошли регистрацию")
            break
        else:
            print("Вы израсходовали 3 попытки, пожалуйста, придумайте новый пароль")