 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

R = 1                     #Define the radius of the support of the funtion
sigma_max = 50                #Defines the maximum value of sigma to be included on the animation 
NumberFrames = 120          #Defines the number of frames in the animation

def tanh (x) :              #Defines the tanh function
  return (np.e ** x - np.e ** (-x) ) / (np.e ** x + np.e ** (-x) )


fig = plt.figure()          #Start to create the figure
ax = plt.axes(xlim=(-2*R, 2*R), ylim=(-0.00001, 1.00001))
line, = plt.plot([], [], 'r-', lw=3)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)


def animate(l):                   #calculates the Alcubierre function
  sigma = ( (l +1)/NumberFrames ) ** 3*sigma_max  #funtion that makes sigma to increase slower at the beginning of the animation
  X=[ ]
  Y=[ ]
  x = - 2*R
  while x <= 2*R :
      X.append( x )
      Y.append( (tanh(sigma*(x+R)) - tanh(sigma*(x-R))) / 2. / tanh(sigma*R) )
      x = x + R/100.
      
  line.set_ydata( Y )  # update the data
  line.set_xdata( X )  # update the data
  time_text.set_text('sigma = {0}'.format(str(sigma)))
  return line, time_text
 
def init():          #The initialization of the animation
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text
  
    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=NumberFrames, interval=150, blit=True)

plt.grid()
plt.title('f(r) with R = {0}'.format(str(R)))
plt.show()
