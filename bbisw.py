#!/usr/bin/python3

import os
import sys
import time
from datetime import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

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
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S")

    st = file_name + ".bmp"
    pygame.image.save(img, st)
    new_image = Image.open(st)
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype("DejaVuSans.ttf", 16)
    w, h = draw.textsize(file_name, font)
    draw.rectangle([0, 0, w, h], fill=(255, 255, 255))
    draw.text((0, 0), file_name, (0, 0, 0), font=font)
    new_image.save(file_name + ".jpg", "JPEG")
    os.remove(st)

    time.sleep(10)

pygame.camera.quit()
