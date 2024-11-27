import redis
import time
from flask import Flask

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis_client.incr('visits')
    return f'Visita número: {count}\n'

@app.route('/stats')
def stats():
    count = redis_client.get('visits')
    return f'Total de visitas: {count}\n'

if __name__ == '__main__':
    # Intentar conectar a Redis con retry
    retry_count = 5
    while retry_count > 0:
        try:
            redis_client.ping()
            break
        except redis.ConnectionError:
            retry_count -= 1
            time.sleep(1)
    
    app.run(host='0.0.0.0', port=5000)