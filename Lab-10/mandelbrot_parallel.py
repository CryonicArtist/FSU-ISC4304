import numpy as np
from multiprocessing import Pool
import mandelbrot_basic as base

def calculate_row(args):
    """Worker function to calculate a single row of the Mandelbrot set."""
    y, xmin, xmax, width, maxiter = args
    row = []
    r1 = np.linspace(xmin, xmax, width)
    for x in r1:
        # Using the basic mandelbrot function from your basic file
        row.append(base.mandelbrot(complex(x, y), maxiter))
    return row

def mandelbrot_set_parallel(xmin, xmax, ymin, ymax, width, height, maxiter):
    # Define the y-coordinates (rows)
    r2 = np.linspace(ymin, ymax, height)
    
    # Prepare arguments for each worker (one task per row)
    tasks = [(y, xmin, xmax, width, maxiter) for y in r2]
    
    # Initialize a pool of workers
    # Pool() automatically uses the number of available CPU cores
    with Pool() as pool:
        # map preserves the order of the results (rows)
        results = pool.map(calculate_row, tasks)
    
    # Flatten the list of rows into a single array for the driver
    return np.array(results).flatten()