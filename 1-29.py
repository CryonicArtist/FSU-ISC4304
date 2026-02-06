import sys

def print_args(args):
    n = len(args)
    
    if "-h" in args:
        print("Syntax: is pythoon argumens.py arg1 arg2, ...")
        sys.exit
    
    for i, ai in enumerate(args):
        print("using enumerate", i,ai)
        
    for i,ai in zip(range(n),args):
        print("using zip", i, ai)
        
if __name__ == "__main__":
    print_args(sys.argv)