def main(S, d):
    
    a = (S - d**2)/(2*d)
    b = a + d
    x = b - (a**2) / (2*b)
    return x

result = main (10, 2)
print(result)