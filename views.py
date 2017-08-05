from flask import Flask, render_template, redirect, url_for, request
import json, time, random

application = Flask(__name__)

freeWords = ["donkey", "cat", "mouse", "doggo"]
usedWords = []
stasisDict = {name: "" for name in freeWords}

@application.route("/")
def index():
	return render_template('landing.html')

@application.route("/newdoc")
def newDocument():
	newDocName = freeWords.pop()
	usedWords.append(newDocName)
	return redirect("/{0}#&togetherjs={0}".format(newDocName))

@application.route("/store", methods = ['POST'])
def storeText():
	currentPage = request.form.get('name')
	currentText = request.form.get('text')
	print("Page is {0} and text is {1}".format(currentPage, currentText))
	stasisDict[currentPage] = currentText
	return ""

@application.route("/retrieve", methods = ['POST'])
def retrieveText():
	currentPage = request.form.get('name')
	print(stasisDict.get(currentPage))
	return stasisDict.get(currentPage)

@application.route('/<path:path>')
def handleRequest(path):
	return render_template("doc.html", name = path.strip("#"))

if __name__ == "__main__":
    application.debug = True
    application.run()