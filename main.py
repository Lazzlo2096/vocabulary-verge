# -*- coding: utf-8
# from flask import Flask
# from flask import render_template
from flask import Flask, render_template, request
from flask import redirect, url_for

# import db_layer_mySQL as db_layer
#import db_layer_SQLite as db_layer

import random

app = Flask(__name__)

freq_word_list1 = [
(1, "and"),
(2, "at"),
(5, "good"),
(66, "black"),
(135, "keyboard"),
]

freq_word_list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]

class ClassA(object):
	"""docstring for ClassA"""

	_iterr = 0

	# range1 <= easyness
	# easyness < len(freq_word_list2)
	range1 = 20
	easyness = 20
	easyness_step = 10

	def __init__(self):
		pass
		#self.setNewIter()

	def setNewIter(self):
		self._iterr = random.randrange(self.easyness-self.range1, self.easyness)

	def getIter(self):
		return self._iterr

	def getWord(self):
		self.setNewIter()
		return freq_word_list2[self._iterr]

	def processButtons(self):

		if request.method == 'POST':
			if request.form['submit_button'] == 'Да':
				#if you right then ++
				self.easyness += self.easyness_step
				word = self.getWord()
			elif request.form['submit_button'] == 'Нет':
				self.easyness -= self.easyness_step
				word = self.getWord()
				#word = "a.getWord()"
			elif request.form['submit_button'] == 'не знаю':
				self.easyness -= self.easyness_step
				word = self.getWord()
			else:
				word = "SOME UNEXPECTED ERROR!!!!"
		elif request.method == 'GET':
			word = "Нажми на кнопушку!"
			pass
		return word

a = ClassA()

@app.route("/", methods=["POST","GET"])
def index():
	
	word="NULL"
	word = a.processButtons()

	return render_template("index.html", word=word)

if __name__=="__main__" :
	# app.run()
	app.run(debug = True)