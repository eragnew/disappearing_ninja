from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def all():
	filenames = ['leonardo.jpg', 'michelangelo.jpg', 'raphael.jpg', 'donatello.jpg']
	return render_template('ninja.html', filenames=filenames)

@app.route('/ninja/<color>')
def ninja(color):
	if color == 'blue':
		filenames = ['leonardo.jpg']
	elif color == 'orange':
		filenames = ['michelangelo.jpg']
	elif color == 'red':
		filenames = ['raphael.jpg']
	elif color == 'purple':
		filenames = ['donatello.jpg']
	else:
		filenames = ['notapril.jpg']
	return render_template('ninja.html', filenames=filenames)

app.run(debug=True)




