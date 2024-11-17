
## TODO Gestión de excepciones
import re
class EmailValidator:
    def __init__(self):
        self.regex  = re.compile(r'([A-Za-z]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    def validar(self,correo:str):
        return re.fullmatch(self.regex, correo)
