def gradientFunction(number):
    GradTable = {0: [0,0,0],
                 128: [240,0,0],
                 244: [240,240,0],
                 255: [128,128,240]}

    gradList = list(GradTable.keys())
    unum = 0
    onum = 0
    for i in range(1,len(gradList)):
       unum = gradList[i-1]
       onum = gradList[i]
       if unum <= number and onum >= number:
           break

    gradu = GradTable[unum]
    grado = GradTable[onum]
    grad = [0,0,0]

    for i in range(3):
       grad[i] = int(gradu[i] + float((grado[i]-gradu[i])/(onum-unum))*(number-unum))
    return grad

while True:
    number = input('Zahl zwischen 0 und 255')
    col = gradientFunction(int(number))
    print(col)
from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()