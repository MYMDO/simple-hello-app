from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Отримаємо ім'я хоста для наочності, де працює контейнер
    hostname = os.uname()[1]
    return f'Hello, SRE/DevSecOps! Running on host: {hostname}\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
