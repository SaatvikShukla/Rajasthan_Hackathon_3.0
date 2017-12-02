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
    return render_template('index2.html')

@app.route('/update')
def update():
	try:
		
		status, res = commands.getstatusoutput("iw wlp2s0 scan | grep 'Ayush' -B 3 | sed -n '1p;4p'")
		# status, res = commands.getstatusoutput("iwlist wlp2s0 scanning | grep 'RONAK' -B 3 -A 3 | egrep 'ESSID|Quality'")
		# status, res = commands.getstatusoutput("iw wlp2s0 scan | grep 'RONAK' -B 4 -A 5 | egrep 'SSID|signal|last seen'")
	except Exception as e:
		raise e
		res = 'Error Scanning networks.'
		print("Exception."+e)

	if status == 0:
		try:
			alpha = res.split('\n\t')
			alpha[1] = (alpha[1].strip());
			alpha[0] = alpha[0].replace("\tsignal: -","")
			alpha[0] = alpha[0].replace(".00 dBm","")
			alpha[1] = alpha[1].replace("SSID: ","")
		except Exception as e:
			print("Exception."+e)
			alpha = 'Error parsing scanned networks.'
			raise e

	print(alpha)
	print(status)
	# print(res)
	return jsonify(result=alpha)


if __name__ == "__main__":
    app.run()