import numpy as np

def calcz(double complex z, double complex c, double zabsmax):
    """
    Calculates the recursive function z=z^2 + c with static typing.
    """
    cdef int nit = 0
    cdef int nitmax = 1000
    cdef double ratio = 0.0

    while abs(z) < zabsmax and nit < nitmax:
        z = z**2 + c
        nit += 1
        ratio = (float(nit) / nitmax) * 255.0
    return ratio

def julia_loop(int im_width, int im_height, double xwidth, double yheight, double xmin, double ymin, int nitmax):
    """
    Main loop cythonized for speed.
    """
    print("Calculate the 2D plane...")
    cdef double zabsmax = 10.0
    cdef double complex c = -0.1 + 0.65j
    cdef int ix, iy
    cdef double complex z
    
    # We leave the numpy array dynamically typed as suggested
    julia = np.zeros((im_width, im_height))

    for ix in range(im_width):
        for iy in range(im_height):
            # Map pixel position to a point in the complex plane
            z = (float(ix) / im_width * xwidth + xmin) + (float(iy) / im_height * yheight + ymin) * 1j
            
            # Do the iterations
            julia[ix][iy] = calcz(z, c, zabsmax)
            
    return julia