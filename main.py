from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def myip():
  return request.remote_addr

if __name__ == "__main__":
  application.run(host='0.0.0.0')
