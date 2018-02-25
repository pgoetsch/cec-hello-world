import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
	with open("/mnt/output.log", "a") as logfile:
    	logfile.write("hello")

    return "Hello World! Greetings from " + socket.gethostname() + "\n"


if __name__ == "__main__":
    application.run()
