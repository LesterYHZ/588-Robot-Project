#Basic LCD screen code

#Function:
#At the end of 75 seconds, your vehicle should cease operation.
#The locations of bridge damage should be presented on the display in sequential form (one at a time),
#with each location displayed for a duration of approximately 1 second.
#This sequence should continue until the robot is turned off by a team member.

#Inputs: Saved washer locations (i.e. locations of bridge damage)
#At the most four locations in one trial
#NOTE: Python starts counting at 0
locs = ["A1","B1","C1","D1"]

#Import
import Adafruit_CharLCD as LCD
import time

#Declare pins
lcd_rs = 22 
lcd_en = 17
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

#Declare mylcd
lcd =LCD.Adafruit_CharLCD (lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


while True: #sequence continues until robot turns off; loop forever
    count=0
    for x in locs:
        count=count+1
        loc_of_Int = x
        strLoc1 = "Location: #" + str(count)
        strLoc2 = loc_of_Int
        lcd.set_cursor(0,0)
        lcd.message(strLoc1)
        lcd.set_cursor(0, 1)
        lcd.message(strLoc2)
        time.sleep(1) #each location displayed for 1 second
        lcd.clear() #clear to print out next location    




