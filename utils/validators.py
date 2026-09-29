def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def get_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except ValueError:
            limits = ""
            if minimum is not None and maximum is not None:
                limits = f" ({minimum}-{maximum})"
            print(f"Please enter a valid integer{limits}.")


def get_float(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt).strip())
            if minimum is not None and value < minimum:
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid number.")
