import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
	hostname = socket.gethostname()
	with open("/mnt/output.log", "a") as logfile:
		logfile.write(str(datetime.now()) + " " + hostname + "\n")

	logfile_content = []
	with open("/mnt/output.log", "r") as logfile:
		logfile_content = logfile.readlines()

	return "\n".join(logfile_content);

if __name__ == "__main__":
    application.run()
