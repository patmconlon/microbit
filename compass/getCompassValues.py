##############################
# Name: compass.py
# Author: Patrick Conlon
# Date: 07/24/2017
# Description:
# Simple script that just obtains the data from the compass chipset.
##############################
from microbit import *

###
# Function : calibrateCompass
# Description : clear and calibrate the compass on the microbit.
#######
def calibrateCompass():
	compass.clear_calibration()
	compass.calibrate()

# Check if the compass has been calibrated.
if( compass.is_calibrated() == False ):
	calibrateCompass()

while True:
	axisX = str( compass.get_x() ) # Gives the magnetic force on the X axis
	axisY = str( compass.get_y() ) # Gives the magnetic force on the Y axis
	axisZ = str( compass.get_z() ) # Gives the magnetic force on the Z axisw

	# Display the values of x, y, and z.
	display.scroll( " ~ " + axisX + " ~ " )
	display.scroll( " ~ " + axisY + " ~ " )
	display.scroll( " ~ " + axisZ + " ~ " )

	sleep( 10 )
	