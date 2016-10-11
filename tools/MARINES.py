import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

class Marine:
  def __init__(self):
    self.Xsize = 26
    self.Ysize = 26

    # Read Marine images
    self.Marines = []
    self.Marines.append(self.ReadMarine('../images/marinefront.png'))
    self.Marines.append(self.ReadMarine('../images/marineback.png'))
    self.Marines.append(self.ReadMarine('../images/marineleft.png'))
    self.Marines.append(self.ReadMarine('../images/marineright.png'))


  def show(self):
    plt.imshow(self.front)
    plt.show()

  def placeMarine(self, terrain, x, y):
    marine = self.Marines[random.randint(0,3)]

    for i in range(self.Xsize):
      for j in range(self.Ysize):
        if np.array_equal(marine[i][j], np.array([255,255,255],dtype=np.uint8)):
          continue
        terrain[x+i][y+j] = marine[i][j]
    return terrain
        
  def ReadMarine(self, location):
    img = cv2.imread(location)
    b,g,r = cv2.split(img)
    return cv2.merge((r,g,b))



### Test area
A = Marine()
