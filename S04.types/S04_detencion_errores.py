def get_name_whit_age(name: str, age: int):
    name_whit_age = name.title() +' is this old: ' + str(age)
    return name_whit_age

information = get_name_whit_age('Maycol',20)
print(information)