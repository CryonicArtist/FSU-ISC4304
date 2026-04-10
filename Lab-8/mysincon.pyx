# mysincon.pyx
from libc.math cimport sin, cos, pow

cdef double calc_cython(double x, double y):
    cdef double z = 0.0
    cdef int i
    for i in range(1, 11):
        z += sin(pow(x, 1.0/i)) * cos(pow(y, 1.0/i))
    return z

def compute_cython():

    cdef int x, y
    cdef double nx, ny, z
    output = []
    
    for x in range(1000):
        line = []
        for y in range(1000):
            nx = x / 100.0
            ny = y / 100.0
            z = calc_cython(nx, ny) * 255.0
            line.append(z)
        output.append(line)
        
    return output