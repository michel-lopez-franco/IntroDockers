from flask import Flask
import redis
import os

app = Flask(__name__)

# Configuración de Redis
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=int(os.getenv('REDIS_PORT', 6379))
)

@app.route('/')
def hello():
    # Incrementar contador en Redis
    visits = redis_client.incr('visits')
    return f'¡Hola! Esta página ha sido visitada {visits} veces.\n'

@app.route('/reset')
def reset():
    redis_client.set('visits', 0)
    return 'Contador reiniciado.\n'

@app.route('/health')
def health():
    return 'OK\n'

@app.route('/status')
def status():
    visits = redis_client.get('visits').decode('utf-8')
    return f'{{"visits": {visits}}}\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)