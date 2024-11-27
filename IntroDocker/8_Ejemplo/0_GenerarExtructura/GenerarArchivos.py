import os
import sys

def create_service_structure(service_name):
    """Crea la estructura de carpetas y archivos para un servicio específico"""
    # Crear directorio del servicio
    os.makedirs(service_name, exist_ok=True)
    
    # Crear main.py
    main_content = f'''from fastapi import FastAPI

app = FastAPI()

@app.get("/{service_name}")
def {service_name}_operation(a: float, b: float):
    """
    Realiza la operación de {service_name}
    Parámetros:
        - a: primer número
        - b: segundo número
    """
    operations = {{
        "addition": lambda x, y: x + y,
        "subtraction": lambda x, y: x - y,
        "multiplication": lambda x, y: x * y,
        "division": lambda x, y: x / y if y != 0 else "Error: División por cero"
    }}
    
    return {{"result": operations["{service_name}"](a, b)}}
'''
    
    with open(f"{service_name}/main.py", "w") as f:
        f.write(main_content)
    
    # Crear requirements.txt
    requirements_content = '''fastapi==0.68.0
uvicorn==0.15.0
'''
    
    with open(f"{service_name}/requirements.txt", "w") as f:
        f.write(requirements_content)

def create_docker_compose():
    """Crea el archivo docker-compose.yml"""
    docker_compose_content = '''version: '3'
services:
  addition:
    build: ./addition
    ports:
      - "8001:80"
    
  subtraction:
    build: ./subtraction
    ports:
      - "8002:80"
    
  multiplication:
    build: ./multiplication
    ports:
      - "8003:80"
    
  division:
    build: ./division
    ports:
      - "8004:80"
'''
    
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose_content)

def main():
    # Crear directorio principal
    os.makedirs("calculator-microservices", exist_ok=True)
    os.chdir("calculator-microservices")
    
    # Crear estructura para cada servicio
    services = ["addition", "subtraction", "multiplication", "division"]
    for service in services:
        create_service_structure(service)
    
    # Crear docker-compose.yml
    create_docker_compose()
    
    print("Estructura de microservicios creada exitosamente!")


def infopath():
    # Obtener el path del archivo actual
    current_file_path = os.path.abspath(__file__)
    print(f"Path del archivo actual: {current_file_path}")

    # Obtener el directorio desde donde se está ejecutando el script
    execution_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f"Directorio de ejecución: {execution_directory}")

if __name__ == "__main__":
    infopath()
    main()