from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    
    # Salvar IP e User Agent em um arquivo
    with open("ips_log.txt", "a") as log_file:
        log_file.write(f"IP: {ip_address}, User-Agent: {user_agent}\n")
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)