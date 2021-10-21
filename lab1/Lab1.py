import speech_recognition as sr
import re
import math
from math import sqrt

def listen_voice():
	r = sr.Recognizer()
	mic = sr.Microphone(device_index=0)
	with mic as source:
		print("Speak the operation!")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	res = r.recognize_google(audio)
	res = res.lower()
	return res

def replace_words_with_number(operation):
	operation = operation.replace("free", "3")
	operation = operation.replace("for", "4")
	operation = operation.replace("too", "2")
	operation = operation.replace("to", "2")
	operation = operation.replace("plus", "+")
	operation = operation.replace("minus", "-")
	operation = operation.replace("multiply", "*")
	operation = operation.replace("multiplied", "*")
	operation = operation.replace("times", "*")
	operation = operation.replace("x", "*")
	operation = operation.replace("√", "square root of")
	return operation

def find_bracktes(operation):
	operation = operation.replace("open bracket", "(")
	operation = operation.replace("opened bracket", "(")
	operation = operation.replace("open rocket", "(")
	operation = operation.replace("openrocket", "(")
	operation = operation.replace("close bracket", ")")
	operation = operation.replace("closed bracket", ")")
	operation = operation.replace("closed racket", ")")
	operation = operation.replace("^", "**")
	return operation

def handle_factorial(operation):
	while (re.search("factorial of [0-9]*", operation)):
		factorial_str = re.search("factorial of [0-9]*", operation).group(0)
		num = eval(factorial_str.replace("factorial of ", ""))
		factorial_res = math.factorial(num)
		operation = operation.replace(factorial_str, str(factorial_res) + " ")
	return operation

def handle_sqrt(operation):
	while (re.search("square root of [0-9]*", operation)):
		factorial_str = re.search("square root of [0-9]*", operation).group(0)
		num = eval(factorial_str.replace("square root of ", ""))
		operation = operation.replace(factorial_str, "sqrt(" + str(num) + ")")
	return operation


res = listen_voice()
res = find_bracktes(res)
res = handle_factorial(res)
res = replace_words_with_number(res)
res = handle_sqrt(res)
print(res)


try:
	print(res + " = " + str(eval(res)))
except SyntaxError:
	print("Incorrect/incomplete math operation!")
except ZeroDivisionError:
	print("Division by 0 is not allowed!")



