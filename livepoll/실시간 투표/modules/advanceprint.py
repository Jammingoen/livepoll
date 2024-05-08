import time

class colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    underline = '\033[4m'
    reset = '\033[0m'

def advanced_print(string):
	for char in string:
		print(char, end="", flush=True)
		time.sleep(0.04)
	print("")

def log_print(title, content, color, sliceprint):
	if color == "none":
		titlecolor = colors.white
	if color == "red":
		titlecolor = colors.red
	if color == "blue":
		titlecolor = colors.blue
	if color == "cyan":
		titlecolor = colors.cyan
	if color == "green":
		titlecolor = colors.green
	if color == "yellow":
		titlecolor = colors.yellow
	if color == "magenta":
		titlecolor = colors.magenta
	
	if sliceprint == True:
		print("[" + titlecolor + title + colors.reset + "]" + " ", end="")
		advanced_print(content)
	if sliceprint == False:
		print("[" + titlecolor + title + colors.reset + "]" + " " + content)