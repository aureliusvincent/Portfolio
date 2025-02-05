import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

font = figlet.getFonts()



if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(font))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")


text = input("Input: ")
print("Output: ")
print(figlet.renderText(text))