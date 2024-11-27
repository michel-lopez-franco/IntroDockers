import requests
import time
import argparse

def check(url):

    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("La página está respondiendo correctamente.")
            else:
                print(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar: {e}")
        time.sleep(1)
        
    
if __name__ == '__main__':
     
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default='172.18.0.2')
    parser.add_argument('--hostname', default='http://172.18.0.2')
    parser.add_argument('--name', default='http://172.18.0.2')
    parser.add_argument('--port', default=5000)
    parser.add_argument('--op', default=0)
    
    args = parser.parse_args()
    
    #hostname = args.hostname if args.hostname.startswith('http') else f'http://{args.hostname}'
    
    match int(args.op):
        case 0:
            url = f'http://{args.ip}:{args.port}'
        case 1:
            url = f'{args.hostname}:{args.port}'
        case 2:
            url = f'{args.name}:{args.port}'
        case 3:
            url = f'http://{args.hostname}:{args.port}'
        case 4:
            url = f'http://{args.name}:{args.port}'            
        case _:
            url = "http://172.18.0.2:5000"

    
    print(f"Running on url: {url}")
    
    check(url)