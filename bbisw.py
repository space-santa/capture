#!/usr/bin/python3

import sys
import time

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
    n = str(i)

    if len(n) == 1:
        n = "000" + n
    elif len(n) == 2:
        n = "00" + n
    elif len(n) == 3:
        n = "0" + n

    st = n + ".bmp"
    pygame.image.save(img, st)
    time.sleep(10)

pygame.camera.quit()
