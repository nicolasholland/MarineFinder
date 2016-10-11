import cv2
import numpy as np
from matplotlib import pyplot as plt
from MARINES import Marine
import random

M = Marine()

locations = ['../images/Terrain 002.jpg']

for location in locations:
  # read terrain
  terrain = cv2.imread(location)
  b,g,r = cv2.split(terrain)
  terrain = cv2.merge((r,g,b))

  Xsize = len(terrain)
  Ysize = len(terrain[0])

  # create a random amount of marines at random locations
  for i in range(random.randint(0,10)):

    x = random.randint(26,Xsize-26)
    y = random.randint(26,Ysize-26)

    terrain = M.placeMarine(terrain, x, y)

  plt.imshow(terrain)
  plt.show()

