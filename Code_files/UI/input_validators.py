class NameLengthException(Exception):
    print("þessi strengur er lengri en 50 stafir")

def validate_name(name):
    if len(name) >= 50:
        raise NameLengthException()