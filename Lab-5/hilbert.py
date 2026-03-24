import sys
import argparse
import matplotlib.pyplot as plt

coords = []

def hilbert(x0, y0, xi, xj, yi, yj, n):
    """
    Recursive function to generate Hilbert curve coordinate pairs.
    """
    if n == 0:
        # Base case: Append the coordinate pair to the global list 
        x = x0 + (xi + yi) / 2
        y = y0 + (xj + yj) / 2
        coords.append((x, y))
    else:
        # Recursively divide the space and rotate/flip the quadrants
        hilbert(x0,               y0,               yi/2, yj/2,  xi/2,  xj/2, n - 1)
        hilbert(x0 + xi/2,        y0 + xj/2,        xi/2, xj/2,  yi/2,  yj/2, n - 1)
        hilbert(x0 + xi/2 + yi/2, y0 + xj/2 + yj/2, xi/2, xj/2,  yi/2,  yj/2, n - 1)
        hilbert(x0 + xi/2 + yi,   y0 + xj/2 + yj,  -yi/2,-yj/2, -xi/2, -xj/2, n - 1)

def main():
    # 1. Take recursion level as commandline input 
    parser = argparse.ArgumentParser(description="Generate a Hilbert curve.")
    parser.add_argument("level", type=int, help="Recursion level (1-8)")
    args = parser.parse_args()

    level = args.level

    # 2. Allow values between 1 and 8 and reject others 
    if not (1 <= level <= 8):
        print("Error: Recursion level must be between 1 and 8.")
        sys.exit(1)

    # 3. Use the hilbert function to generate coordinates in a 1x1 space
    # Initial bounds: x=0, y=0, width=1.0, height=1.0
    hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, level)

    # 4. Convert coordinate pairs to separate x and y vectors 
    X = [pair[0] for pair in coords]
    Y = [pair[1] for pair in coords]

    # 5. Plot using matplotlib 
    plt.figure(figsize=(6, 6))
    plt.plot(X, Y, color='maroon', linewidth=0.8) 
    
    # axes to 0.0 to 1.0
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title(f"Hilbert Curve - Level {level}")
    
    filename = f"hilbert{level}.pdf"
    plt.savefig(filename, bbox_inches='tight')
    print(f"Successfully generated and saved: {filename}")

if __name__ == "__main__":
    main()