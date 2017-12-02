#
# Python Flask Module for control center
#
# Saatvik Shukla
# Dec 2 2017, 9.51am

import math
import commands
import subprocess
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('index2.html')

def average(n1,n2):
	return ((n1+n2)/2)

@app.route('/update')
def update():
	try:
		pass
	except Exception as e:
		raise e
		res = 'Error Scanning networks.'
		print("Exception."+e)

	try:
		cmd = "iw wlan0 scan | grep 'OP' -B 9 | egrep 'freq:|signal|SSID:' | sed -n '1p;2p;3p'"
		status, res = commands.getstatusoutput(cmd)
		alpha = res.split('\n\t')
		alpha[1] = (alpha[1].strip());
		alpha[0] = alpha[0].replace("\tfreq: ","")
		alpha[1] = alpha[1].replace("signal: -","")
		alpha[1] = alpha[1].replace(".00 dBm","")
		alpha[2] = alpha[2].replace("SSID: ","")

		status, res = commands.getstatusoutput(cmd)
		beta = res.split('\n\t')
		beta[1] = (beta[1].strip());			
		beta[0] = beta[0].replace("\tfreq:: ","")
		beta[1] = beta[1].replace("signal: -","")
		beta[1] = beta[1].replace(".00 dBm","")
		beta[2] = beta[2].replace("SSID: ","")

	except Exception as parsingError:
		print("Exception."+parsingError)
		alpha = 'Error parsing scanned networks.'
		beta = 'Error parsing scanned networks.'
		gamma = 'Error parsing scanned networks.'
		theta = 'Error parsing scanned networks.'
		zeta = 'Error parsing scanned networks.'
		raise parsingError

	temp = average(int(alpha[1]), int(beta[1]))
	alpha[1] = temp
	print(alpha)
	return jsonify(result=alpha)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)