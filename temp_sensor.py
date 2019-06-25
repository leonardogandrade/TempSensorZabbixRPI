import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import MySQLdb as mysql

#Mysql connection
db = mysql.connect(host="localhost",
                      user="pi",
                      passwd="<password>",
                      db="<db_name> ")
                      
cur = db.cursor()
sql = """ insert into dht11(temp,humi) values(%s,%s) """
 
# Definiton of sensor type
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
 
GPIO.setmode(GPIO.BOARD)
 
# Raspberry Pi Gpio
pino_sensor = 25
 
print ("Reading data...")
# Data from sensor
umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
if umid is not None and temp is not None:
  print ("Temperature = {0:0.1f}  Humidity = {1:0.1f}n").format(temp, umid)
  try:
    #Record data to database
    cur.execute(sql,(temp,umid))
    db.commit()
    time.sleep(5)
  except:
    print("Error")
else:
  print("Error while reading data from sensor.")