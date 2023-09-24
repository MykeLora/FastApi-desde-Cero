def get_full_name(firts_name: str,last_name: str):
    full_name = firts_name.capitalize() + ' ' + last_name.title()
    return full_name

full_name = get_full_name('maycol', 'lora')
print(full_name)
