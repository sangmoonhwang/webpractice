from flask import Flask, redirect, url_for, render_template, request
from firebase import firebase
import sys

#config
#server will reload on source changes, and provide 	a debegger for errors
#DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__) #consume the configuration above
firebase = firebase.FirebaseApplication('https://fiery-torch-7725.firebaseio.com/', None)


#decorator which tells flask what url triggers this fn
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/messages')
def messages():
	result = firebase.get('/messages', None)
	return render_template('list.html', messages=result)

@app.route('/submit_message', methods=['POST'])
def submit_message():
	message = {
	'body': request.form['message'],
	'who' : request.form['who']
	}
	firebase.post('/messages', message)
	return redirect(url_for('messages'))

#start the application if this is the main python module
if __name__ == "__main__":
	port = int(sys.argv[1])
	app.run(host="0.0.0.0",port=port)