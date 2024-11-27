import os

message = os.getenv('MESSAGE', 'Mensaje por defecto')
env = os.getenv('APP_ENV', 'development')

print(f"Mensaje: {message}")
print(f"Ambiente: {env}")