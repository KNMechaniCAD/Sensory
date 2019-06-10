import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG = 8                                   #Associate pin 23 to TRIG
ECHO_R = 36                                #Associate pin 24 to ECHO
ECHO_F = 40                                #Associate pin 24 to ECHO
ECHO_L = 38                               #Associate pin 24 to ECHO



GPIO.setup(TRIG,GPIO.OUT)                    #Set pin as GPIO out
GPIO.setup(ECHO_F,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(ECHO_L,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(ECHO_R,GPIO.IN)                   #Set pin as GPIO in

try:


	while True:

		GPIO.output(TRIG, False)                 #Set TRIG as LOW
		print "Waitng For Sensors To Settle"
		time.sleep(2)                            #Delay of 2 seconds

		GPIO.output(TRIG, True)                  #Set TRIG as HIGH
		time.sleep(0.00001)                      #Delay of 0.00001 seconds
		GPIO.output(TRIG, False)                 #Set TRIG as LOW

		while GPIO.input(ECHO_F)==0:               #Check whether the ECHO is LOW
			pulse_start_F = time.time()              #Saves the last known time of LOW pulse

		while GPIO.input(ECHO_F)==1:               #Check whether the ECHO is HIGH
			pulse_end_F = time.time()                #Saves the last known time of HIGH pulse 
	
		while GPIO.input(ECHO_R)==0:               #Check whether the ECHO is LOW
			pulse_start_R = time.time()              #Saves the last known time of LOW pulse

		while GPIO.input(ECHO_R)==1:               #Check whether the ECHO is HIGH
			pulse_end_R = time.time()                #Saves the last known time of HIGH pulse 
	
		while GPIO.input(ECHO_F)==0:               #Check whether the ECHO is LOW
			pulse_start_F = time.time()              #Saves the last known time of LOW pulse

		while GPIO.input(ECHO_L)==1:               #Check whether the ECHO is HIGH
			pulse_end_L = time.time()                #Saves the last known time of HIGH pulse 

		pulse_duration_F = pulse_end_F - pulse_start_F #Get pulse duration to a variable
		pulse_duration_L = pulse_end_L - pulse_start_L #Get pulse duration to a variable
		pulse_duration_R = pulse_end_R - pulse_start_R #Get pulse duration to a variable

		distance_F = pulse_duration_F * 17150        #Multiply pulse duration by 17150 to get distance
		distance_F = round(distance_F, 2)            #Round to two decimal points
  
		distance_L = pulse_duration_L * 17150        #Multiply pulse duration by 17150 to get distance
		distance_L = round(distance_L, 2)            #Round to two decimal points
  
		distance_R = pulse_duration_R * 17150        #Multiply pulse duration by 17150 to get distance
		distance_R = round(distance_R, 2)            #Round to two decimal points

 # if distance > 2 and distance < 400:      #Check whether the distance is within rane
		print "Distance forward:",distance_F - 0.5,"cm"  #Print distance with 0.5 cm calibration
		print "Distance left:",distance_L - 0.5,"cm"  #Print distance with 0.5 cm calibration
		print "Distance right:",distance_R - 0.5,"cm"
