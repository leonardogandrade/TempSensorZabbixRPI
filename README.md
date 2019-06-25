# TEMPERATURE/HUMIDITY SENSOR USING RASPBERRY ZERO AND ZABBIX

## ABSTRACT

This project aimed to develop from scratch a temperature and humidity sensor to be monitored in Zabbix Monitoring System as well the python script to collect data and the Zabbix configuration.

## MOTIVATION

The motivation to create a circuit and no simply buy a commercial one from the internet, was the was not possible to find this one. The choice for Raspberry Pi and not a simplest microcontroller as Arduino, was due forbid POST requests to feed itens data in its API.

## EQUIPMENTS TO SENSOR

* Raspberry PI Zero W
* DHT11 Temperature and Humidity sensor
* SD Card
* 10k resistor
* Raspberry Pi 5v charger
* Raspberry Pi case

## SCHEMATIC

![GitHub Logo](https://github.com/generalAndrade/tempSensorZabbixRPI/blob/master/img/schematic.png)

** In this case we are using GPIO15.

## 3D SKETCH

Into etc folder you'll find a raspberry Pi case sketch to print in a 3D printer.

## MYSQL

Use the commands bellow to install and configure the mariadb database

> sudo apt-get install mariadb-server

> mysql –u pi -p

> create database <database_name>;

> use <database_name>;

> create table dht11(id int(10) auto_increment primary key,temp varchar(15),humi varchar(15), created timestamp default current_timestamp);

> grant all privileges on <database_name>.* to ‘pi’@’%’ identified by ‘<password>’ with grant options;
  
> flush privileges;

## PYTHON SCRIPT

Use the commands bellow to update your system and install the pre reqs.

> sudo apt-get update

> sudo apt-get install build-essential python-dev

> git clone https://github.com/adafruit/Adafruit_Python_DHT.git

> cd Adafruit_Python_DHT

> sudo python setup.py install

> sudo python3 setup.py install

After that you can use the python script temp_sensor.py to collect data.

## ZABBIX AGENT

Is necessary to install zabbix agent on Raspberry Pi. You can use the command bellow to do that.

> $ apt-get install zabbix-agent

Having installed the agent, edit the file /etc/zabbix/zabbix_agentd.conf and replace the the value in the keys Server and Server and ServerActive for the zabbix server ip.


## ZABBIX CONFIGURATION

In Zabbix side, we’ll use the database monitoring. You can find in the link bellow how to configure Zabbix for that. If you found some problems in this step, probably is because you forgot to set privileges in mariadb to be accessed remotely, so please take a new look at MYSQL step.
After, this configuration, you can create a host in Zabbix and import the template attached called zbx_export_temperature_sensor.xml

