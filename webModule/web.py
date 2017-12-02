#
# Python Flask Module for control center
#
# Saatvik Shukla
# Dec 2 2017, 9.51am

import commands
import subprocess
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/update')
def add_numbers():
	try:
		status, res = commands.getstatusoutput("iw wlp2s0 scan | grep 'abc' -B 4 -A 5 | egrep 'SSID|signal|last seen'")
		print(status)
		print(res)
	except Exception as e:
		raise e
		print("Exception."+e)

	if status == 0:
		print "Scanning success."
	elif status == 1:
		res=None
		print("Error while scanning")

	return jsonify(result=res)


if __name__ == "__main__":
    app.run()