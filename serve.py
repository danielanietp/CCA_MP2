from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Handle POST request to stress CPU
        stress_process = subprocess.Popen(['python3', 'stress_cpu.py'])
        return "Stressing CPU initiated."
    elif request.method == 'GET':
        # Handle GET request to return private IP address
        private_ip = socket.gethostbyname(socket.gethostname())
        return private_ip

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(host='0.0.0.0', port=5000)
