import math

def main(n):
    if n == 0:
        return 0.27
        
    fn_1 = 0.27
    for i in range(n):
        fn_1 = math.sqrt((52 * fn_1**2) + (40 * fn_1)) + 1
        
    return fn_1
    
print(main(6))



