#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 12.08.2018

@author: Niels
"""

from pyblnet import BLNETWeb, test_blnet, BLNETDirect, BLNET

if __name__ == '__main__':

    ip = '192.168.178.10'

    # Check if there is a blnet at given address
    print(test_blnet(ip))

    # Easy to use high level interface
    blnet = BLNET(ip, timeout=5)
    print(blnet.turn_on(10))
    print(blnet.fetch())

    # Fetch the latest data via web interface
    blnet = BLNETWeb(ip, timeout=5)
    print(blnet.read_analog_values())
    #print(blnet.read_analog_values())
    d=blnet.read_digital_values()
    print(d)
    
    print(blnet.get_digital_value(type='mode' , name='Pumpe-Solar1'))
    print(blnet.get_digital_value(type='value' , cached=d, name='Pumpe-Solar1'))    
    

    # For publishing values
    #print(blnet.set_digital_value("10", 'AUS'))
    #print(blnet.read_digital_values())

    blnet = BLNETDirect(ip)
    # Fetching the latest data from the backend
    print(blnet.get_latest())
    # Still inofficial because unexplicably failing often
    print(blnet._get_data(1))
