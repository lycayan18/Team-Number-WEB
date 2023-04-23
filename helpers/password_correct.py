def password_correct(password):
    if ' ' in password:
        return [False, "Пароль не должен содержать пробелов"]
    if len(password.strip()) < 8 or len(password.strip()) > 20:
        return [False, "Пароль может состоять из 8-20 знаков"]
    if (any(i.isupper() for i in password)) is False:
        return [False, "Пароль должен содержать хотя бы одну заглавную букву"]
    if (any(i.islower() for i in password)) is False:
        return [False, "Пароль должен содержать хотя бы одну строчную букву"]
    if (any(i.isdigit() for i in password)) is False:
        return [False, "Пароль должен содержать хотя бы одну цифру"]
    return [True]
