#!/usr/bin/env python3

def sum_equation(L):
    temp = []
    return_string = ""
    if len(L) > 0:  
        for i in L:
            temp.append(str(i))
        return_string += " + ".join(temp)
        return_string += f" = {sum(L)}"
    else:
        return_string = "0 = 0"
    return return_string

def main():
    L = []
    sum_equation(L)

if __name__ == "__main__":
    main()
