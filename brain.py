import sys
import RPi.GPIO as GPIO
import time

#setting up the GPIOS, BCM indicates we're referring to the GPIO number, not the PIN number
GPIO.setmode(GPIO.BOARD)

#set all the GPIO to out mode

#turn on feature GPIOs
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


#turn off feature GPIOs
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)


try:
    if len(sys.argv) > 1:
        if sys.argv[1] == 'lights':
            if sys.argv[2] == 'on':
              
                GPIO.output(40, True)

            elif sys.argv[2] == 'off':

                GPIO.output(33, True)


        elif sys.argv[1] == 'ac':
            if sys.argv[2] == 'on':

                GPIO.output(38, True)

            elif sys.argv[2] == 'off':
        
                GPIO.output(35, True)


        elif sys.argv[1] == 'sunlight':
            if sys.argv[2] == 'on':

                GPIO.output(36, True)


            elif sys.argv[2] == 'off':

                GPIO.output(37, True)


finally:
    time.sleep(1)
    GPIO.cleanup() #clean exit
