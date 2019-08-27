#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'image2ink/pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'image2ink/lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd7in5bc.EPD()
    HBlackimage = Image.open(os.path.join(picdir, '7in5b-b.bmp'))
    HRYimage = Image.open(os.path.join(picdir, '7in5b-r.bmp'))    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
 
    while True:
        logging.info("epd7in5bc Demo")
        logging.info("init and Clear")
        epd.init()
        epd.Clear()
        time.sleep(1)
        
        # Drawing on the image
        logging.info("Drawing")    
            
        logging.info("3.read bmp file")

        epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
        time.sleep(10)
        
        logging.info("Clear...")
        epd.init()
        epd.Clear()
        
            
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("Goto Sleep...")
    epd.sleep()   
    logging.info("ctrl + c:")
    epd7in5bc.epdconfig.module_exit()
    exit()
