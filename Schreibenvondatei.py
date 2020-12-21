userInput= """
ToDo:
- schreiben
-lesen
-schlafen
-atmen
"""

'''
1.
r: read
w: write
x: write (only if new file)
a: append (only, if exists)

2.
t: text
b: binary
'''
fileOutput = open("notizen.txt","wt")
InfoBytes = fileOutput.write(userInput)
fileOutput.close()

#
print("Byte number: {}".format(InfoBytes))
print("String number: {}".format(len(userInput)))

