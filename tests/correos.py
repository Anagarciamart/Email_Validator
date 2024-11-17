from emails.validator import EmailValidator

validator = EmailValidator()

dir_email = [
        "ejemplo@prueba.com",
        "nombre@dominio.com",
        "ejemploprueba.com",
        "ejemplo@domain",
        "ejemplo@!domain.com",
        "ejemplo@domain.587"
]

for correo in dir_email:
    if validator.validar(correo):
        print(f"{correo} es válido")
    else:
        print(f"{correo} no es válido")