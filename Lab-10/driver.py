import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import time
import sys

# Core modules available in your folder
import mandelbrot_basic as base
import mandelbrot_parallel as para

# These are causing the error because the files are missing from your directory
# import mandelbrot_numba as numb
# import mandelbrot_cython as cyt
# import mandelbrot2 as ccode

def mandelbrot_image(func, xmin, xmax, ymin, ymax, width=3, height=3, maxiter=80, cmap='hot_r', plotting=True, label="Output"):
    dpi = 72
    img_width = int(dpi * width)
    img_height = int(dpi * height)

    # Use perf_counter to accurately measure parallel execution time
    tic = time.perf_counter()    
    z = func(xmin, xmax, ymin, ymax, img_width, img_height, maxiter)
    toc = time.perf_counter()
    
    runtime = toc - tic
    print(f"{label} run time: {runtime:.4f}s")
    
    if plotting:
        fig, ax = plt.subplots(figsize=(width, height), dpi=72)
        ticks = [0, img_width/2, img_width]
        x_ticks = [xmin, (xmax+xmin)/2, xmax]
        plt.xticks(ticks, x_ticks)
        y_ticks = [ymin, (ymax+ymin)/2, ymax]
        plt.yticks(ticks, y_ticks)
        
        norm = colors.PowerNorm(0.3)
        znew = [zi if zi < maxiter else 0 for zi in z]
        znew = np.array(znew).reshape(img_width, img_height)
        
        ax.imshow(np.array(znew).T, cmap=cmap, origin='lower', norm=norm)
        plt.title(f"Method: {label}")
        plt.savefig(f"{label}_Image.png")
    
    return runtime

def magnifier(center, magnify):
    m = 1.0 / magnify
    xl = center[0] - m 
    xu = center[0] + m
    yl = center[1] - m
    yu = center[1] + m
    print(f"Center: {center} | Magnification: {magnify}")
    return (xl, xu, yl, yu)

if __name__ == "__main__":
    # Default settings
    width, height, maxiter = 5, 5, 2048
    center = [-0.743, 0.1264]
    magnify = 100.0

    if len(sys.argv) > 3:
        center = [float(sys.argv[1]), float(sys.argv[2])]
        magnify = float(sys.argv[3])

    xmin, xmax, ymin, ymax = magnifier(center, magnify)

    print("\n--- Starting Performance Comparison ---")
    
    # 1. Run Pure Python (Serial)
    print("Running Serial Python...")
    t_base = mandelbrot_image(base.mandelbrot_set, xmin, xmax, ymin, ymax, 
                              width, height, maxiter, cmap='hot', plotting=True, label="Serial")

    # 2. Run Multiprocessing (Parallel)
    print("Running Multiprocessing...")
    t_para = mandelbrot_image(para.mandelbrot_set_parallel, xmin, xmax, ymin, ymax, 
                              width, height, maxiter, cmap='hot', plotting=True, label="Parallel")

    print("\n" + "="*30)
    print(f"FINAL SPEEDUP: {t_base / t_para:.2f}x")
    print("="*30)