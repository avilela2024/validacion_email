
## TODO Gestión de excepciones

import re
import logging

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,  # Nivel mínimo que se registrará (puede cambiarse a DEBUG, ERROR, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("email_validator.log"),  # Guardar los logs en un archivo
        logging.StreamHandler()  # Mostrar los logs en la consola
    ]
)

class EmailValidator:
    def __init__(self):
        self.regex = re.compile(r'^([A-Za-z0-9]+([._-][A-Za-z0-9]+)*)@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$')

    def validar(self, correo: str) -> bool:
        try:
            if not isinstance(correo, str):
                logging.error(f"Entrada no válida: {correo} (tipo: {type(correo)})")
                return False
            
            resultado = bool(re.fullmatch(self.regex, correo))
            
            if resultado:
                logging.info(f"Correo válido: {correo}")
            else:
                logging.warning(f"Correo inválido: {correo}")
                
            return resultado
        
        except Exception as e:
            # Registrar cualquier error inesperado
            logging.exception(f"Error al validar el correo: {correo}")
            return False