#(Algebra: quadratic equations) The two roots of a quadratic equation, can be obtained using the following formula
import math

# Class for quadratic equation
class QuadraticEquation:
    
    # constructor (save a, b, c)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # find and display roots
    def display_roots(self):
        d = self.b*self.b - 4*self.a*self.c   # discriminant

        if d > 0:
            # two real roots
            r1 = (-self.b + math.sqrt(d)) / (2*self.a)
            r2 = (-self.b - math.sqrt(d)) / (2*self.a)
            print("Two roots:", r1, r2)

        elif d == 0:
            # one root
            r = -self.b / (2*self.a)
            print("One root:", r)

        else:
            # no real root
            print("No real roots")

# create object
eq = QuadraticEquation(1, 9, 2)

# call method
eq.display_roots()