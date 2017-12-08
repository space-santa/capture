#!/usr/bin/python3

import os
import sys
import time
from datetime import datetime

import pygame.camera
import pygame.image

pygame.camera.init()

for _ in range(10):
    try:
        cam = pygame.camera.Camera(
            pygame.camera.list_cameras()[0], (1280, 720))
    except IndexError:
        print("Can't access camera, trying again...")
        time.sleep(10)
    else:
        cam.start()
        break
else:
    sys.exit(1)

for i in range(11):
    img = cam.get_image()

    st = datetime.now().strftime("%Y%m%d_%H%M%S") + ".bmp"
    pygame.image.save(img, st)
    status = os.system("mogrify -format jpg " + st)
    os.remove(st)

    if status != 0:
        pygame.camera.quit()
        sys.exit("Couldn't run mogrify, is ImageMagick installed?")

    time.sleep(10)

pygame.camera.quit()
