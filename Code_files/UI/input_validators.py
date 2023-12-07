# Input Validators


class NameLengthException(Exception):
    print("Þessi strengur er lengri en 50 stafir.")


# Validating staff information
def validate_name(name):
    """Check length of name"""
    if len(name) >= 50:
        raise NameLengthException()


def validate_kt(kt):
    """Check if kennitala is 10 digits and all numeric characters."""
    valid = kt.isnumeric()

    if len(kt) != 10:
        print("Úps, þessi kennitala virðist ekki vera rétt. Reyndu aftur.")
        return False
    elif valid != True:
        print("Úps, þessi kennitala virðist ekki vera rétt. Reyndu aftur.")
        return False
    else:
        return True


def validate_phone_number(phone_number):
    """Check validity of phone number by checking if it's only numerical numbers"""
    valid = phone_number.isnumeric()

    if valid != True:
        print("Úps, þetta símanúmer virðist ekki vera rétt. Reyndu aftur.")
        return False
    else:
        return True


def validate_address(address, postal_code, place):
    pass


def validate_occupation(occupation):
    lower_occupation = occupation.lower()

    if lower_occupation == "flugþjónn" or lower_occupation == "flugmaður":
        pass
