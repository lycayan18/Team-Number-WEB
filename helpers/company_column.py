def company_check(company, list_table):
    if company == "google":
        company_table = list_table[0]  #Google
    elif company == "yandex":
        company_table = list_table[1]  #Yandex
    else:
        company_table = list_table[2] #OpenAI
    return company_table