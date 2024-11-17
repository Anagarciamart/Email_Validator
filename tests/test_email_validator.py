import unittest
from emails.validator import EmailValidator

class TestEmailValidator(unittest.TestCase):

    def valid_email(self):
        validator = EmailValidator()
        self.assertTrue(validator.validar("ejemplo@prueba.com"))
        self.assertTrue(validator.validar("nombre@dominio.com"))

    def invalid_email(self):
        validator = EmailValidator()
        self.assertFalse(validator.validar("ejemploprueba.com"))
        self.assertFalse(validator.validar("ejemplo@domain"))
        self.assertFalse(validator.validar("ejemplo@!domain.com"))
        self.assertFalse(validator.validar("ejemplo@domain.587"))


if __name__ == "__main__":
    unittest.main()