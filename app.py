from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return "Hello, DevOps World! This app is running inside Docker and built by Jenkins!"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)

