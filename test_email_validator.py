import sys
import os
sys.path.append(os.path.expanduser("~/Desktop/ejerciciovalidacionemail"))

import unittest
from emails.validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        # Inicializar el validador antes de cada prueba
        self.validator = EmailValidator()

    def test_valid_emails(self):
        # Casos de correos válidos
        valid_emails = [
            "test@example.com",
            "user.name@domain.com",
            "user-name@domain.org",
            "user_name@domain.net",
            "user@sub.domain.com",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(self.validator.validar(email), f"Failed for {email}")

    def test_invalid_emails(self):
        # Casos de correos inválidos
        invalid_emails = [
            "user@domain",         # Falta TLD
            "user@.com",           # Falta dominio
            "@domain.com",         # Falta nombre de usuario
            "userdomain.com",      # Falta @
            "user@domain..com",    # Doble punto en dominio
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(self.validator.validar(email), f"Failed for {email}")

if __name__ == "__main__":
    unittest.main()