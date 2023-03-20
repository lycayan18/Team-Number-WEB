def name_correct(name_user):
    if len(name_user.strip()) < 4 or len(name_user.strip()) > 30:
        return [False, "Имя пользователя может состоять из 4–30 знаков"]
    if any(i in name_user for i in ['&', '=', '+', '<', '>', '*', '/', '(', ')', '_', '-', ',', "'", '"', '!', '@',
                                    '#', '$', '%', '^', '`', '~', '?']):
        return [False, """"Имя пользователя не должно содержать символы : &=+<>*/()_-,"'"""]
    if name_user.strip()[0] == "." or name_user.strip()[-1] == ".":
        return [False, "Имя пользователя не должно заканчиваться или начинаться на знак: ."]
    return [True]

