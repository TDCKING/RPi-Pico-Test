import select
import sys
import machine
import time
 
MAX_BUFFER = 16 #max buffer for reading timer values

led = machine.Pin(25, machine.Pin.OUT) #controls LED
pollObj = select.poll() #instantiate a poll object
pollObj.register(sys.stdin,1) #register stdin for monitoring read

buffer = [MAX_BUFFER]
y = 0
ledBlink = 1

#For things that need to be initialized
def initRPico():
    print("~Rpico Start~")

initRPico()

def blinkLed():
    led.value(not led.value())
    time.sleep(1)
    #ledBlink = not ledBlink
    #led.value(0)
    #time.sleep(1)
 
while True:
    #Check for data available on stdin
    if pollObj.poll(0):
        num = sys.stdin.read(1) #read one character from stdin
        if num == 'p':
            print("Received: " + num)
            blinkLed()

    time.sleep(0.1)
