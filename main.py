#!/usr/bin/python3

import pygame
import optparse
import sys
import settings
from pypboy.core import Pypboy

def main():
    #Enable use of cached map via "-c True" command
    parser = optparse.OptionParser(usage='python %prog -c True\nor:\npython %prog -c True', version="0.0.1", prog=sys.argv[0])
    parser.add_option('-c','--cached-map', action="store_true", help="Loads the cached map file stored in map.cache", dest="load_cached", default=False)
    options, args = parser.parse_args()

    try:
        import RPi.GPIO as GPIO
        # GPIO.setmode(GPIO.BCM)
        settings.GPIO_AVAILABLE = True
    except Exception:
        _, err, _ = sys.exc_info()
        print("GPIO UNAVAILABLE (%s)" % err)
        settings.GPIO_AVAILABLE = False

    try:
        pygame.mixer.pre_init(44100, -16, 2, 512)
        settings.SOUND_ENABLED = True
    except Exception as e:
        settings.SOUND_ENABLED = False

    boy = Pypboy('Pip-Boy 3000 MK IV', settings.WIDTH, settings.HEIGHT)
    print("RUN")
    boy.run()


if __name__ == "__main__":
    main()