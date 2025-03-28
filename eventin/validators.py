import re
from validate_docbr import CPF
def nome_invalido(nome):
    return len(nome) < 3 or not all(char.isalpha() or char.isspace() for char in nome)

def email_invalido(email):
    return '@' not in email or '.' not in email.split('@')[1]

def telefone_invalido(telefone):
    # return len(telefone) < 8 or not telefone.isdigit()
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    response = re.findall(modelo, telefone)
    return not response

def cpf_invalido(cpf):
    return not CPF().validate(cpf)