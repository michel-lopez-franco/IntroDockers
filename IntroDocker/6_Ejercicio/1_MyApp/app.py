import os
import argparse
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    count = 200
    return f'Visita número: {count}\n'

@app.route('/stats')
def stats():
    count = 200
    return f'Total de visitas: {count}\n'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname', default='0.0.0.0')
    parser.add_argument('--name', default='app-flask')
    parser.add_argument('--port', default=5000)
    args = parser.parse_args()
    
    port1 = int(os.getenv('FLASK_RUN_PORT', 5000)) 
    port2 = int(args.port)
    port = port1 if port1 != 5000 else port2
    
    print(f"Running on port: {port}")
    print(f"Running on hostname: {args.hostname}")
    print(f"Running on name: {args.name}")
    app.run(host='0.0.0.0', port=port)
    
    
    
    




