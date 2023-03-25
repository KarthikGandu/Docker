# write aflask prohgram with two routes one for home and one for container and return the hostname of the container

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'
@app.route('/container')
def container():
    return 'Container running sucessfully '

if __name__ == '__main__':
    app.run()
            