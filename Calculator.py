import numpy as np

def compute(operation, *args):
    """
    Given two or more numbers compute its addition, or multiplication.
    Given two numbers, compute addition, subtraction, multiplication or division.
    
    Parameters:
        x: Integer
        y: Integer
        operation: String. "add", "sub", "mul", "div"
    
    Returns:
        Result's computation. Float
    """
    
    # --- Error handling ---
    
    # Operation argument should be one of the following: "add", "sub", "mul" or "div"
    if operation.lower() not in ["add", "sub", "mul", "div"]:
        raise ValueError("Operation parameter should be one of the following add, sub, mul or div")
        
    # Numbers should be all integers 
    if not all(isinstance(number, int) for number in args):
        raise TypeError("args values should be all integer")

    
    # --- Main ---
    
    # Subtraction
    if len(args) == 2 and operation.lower() == "sub":
        x, y = args
        print(x - y)
        return float(x - y)
    elif len(args) != 2 and operation.lower() == "sub":
        raise ValueError("args should be two numbers")
    
    # Division
    if len(args) == 2 and operation.lower() == "div":
        x, y = args
        print(x / y)
        return float(x / y)
    elif len(args) != 2 and operation.lower() == "div":
        raise ValueError("args should be two numbers")
    
    # Addition
    if len(args) > 1 and operation.lower() == "add":
        res = sum(args)
        print(res)
        return float(res)
    
    # Multiplication
    if len(args) > 1 and operation == "mul":
        res = np.prod(args)
        print(res)
        return float(res)
        
        
compute("add", 5,2,3)
compute("sub", 5,2)
compute("mul", 5,2,3)
compute("div", 5,2)
