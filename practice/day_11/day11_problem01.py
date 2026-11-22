def get_number(message):
    try:
        number = int(input(message))
        return number
    except ValueError:
        return None