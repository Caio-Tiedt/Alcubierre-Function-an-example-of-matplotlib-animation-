# Alcubierre-Function-an-example-of-matplotlib-animation-
Creates an animation of the Alcubierre function from Alcubierre's warp drive described in https://arxiv.org/abs/gr-qc/0009013, as we vary the parameter sigma.

The Alcubierre metric is a solution to Einstein's general relativity equation such that allows travel at a speed faster than light proposed by  Miguel Alcubierre. 

The idea is the creation of a region on space, called bubble, such that spacetime will contract in the front of the bublle and spacetime will expand behind it. Therefore, locally a spacecraft inside the bubble will not violate the local laws of relativity and will maintin a speed slower than light, but the globally th bubble is going to move faster than light.

The metric is:
ds^2 = -dt^2 + (dx - v f(r)dt)^2 + dy^2 + dz^2

The function f(r), here called Alcubierre's funcion, serves as the definition of the bubble on space, and is given by
f(r) = (tanh(sigma(r+R)) - tanh(sigma(r-R)))/(2tanh(sigmaR))

The format of this function changes with the parameter sigma. The higher the sigma, the sharper the bubble.

This project uses this function as an example of creating animations of functions with a varying parameter using matplotlib.animation.
