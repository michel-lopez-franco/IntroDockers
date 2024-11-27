import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mensaje', default='Hola Mundo')
args = parser.parse_args()

print(f"Mensaje recibido: {args.mensaje}")