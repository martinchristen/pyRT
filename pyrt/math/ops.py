"""
Various math functions for shading
"""

import math
from math import floor, ceil

# ---------------------------------------------------------------------------------------------------------------------

def fract(x: float) -> float:
    return x - floor(x)

# ---------------------------------------------------------------------------------------------------------------------

def mod(x: float, y: float) -> float:
    """
    Modulo function for cross language compatibility
    In Python use built in "%" if it makes more sense
    """
    return x-y*floor(x/y)

# ---------------------------------------------------------------------------------------------------------------------

def clamp(x: float, minval: float, maxval: float) -> float:
    """
    Clamp value
    """
    if x >= maxval:
        return maxval
    elif x <= minval:
        return minval
    return x

# ---------------------------------------------------------------------------------------------------------------------

def mix(x: float, y: float, a: float) -> float:
    """
    Do a linear blend: x*(1-a) + y*a
    """
    return (1-a)*x + a*y

# ---------------------------------------------------------------------------------------------------------------------

def step(edge: float, x: float) -> float:
    if x>= edge:
        return 1.0
    return 0.0

# ---------------------------------------------------------------------------------------------------------------------

def lerp(x: float, a: float, b: float) -> float:
    return (a + x * (b - a))

# ---------------------------------------------------------------------------------------------------------------------

def s_curve(x: float) -> float:
    return ( x * x * (3.0 - 2.0 * x));

# ---------------------------------------------------------------------------------------------------------------------

def smoothstep(a: float, b: float, x: float) -> float:
    """
    Cubic Approximation (a can't be same as b)
    """
    if x<a: 
        return 0.0
    if x>=b: 
        return 1.0
    x = (x-a) / (b-a)
    return s_curve(x)    

# ---------------------------------------------------------------------------------------------------------------------

def pulse(a: float, b: float, x: float) -> float: 
    return (step(a,x) - step(b,x));

# ---------------------------------------------------------------------------------------------------------------------

def gammacorrect(gamma: float, x: float) -> float:
    return pow(x, 1.0/gamma);

# ---------------------------------------------------------------------------------------------------------------------

''' 
float turbulence(float *v, float freq)
{
   float t, vec[3];

   for (t = 0. ; freq >= 1. ; freq /= 2) {
      vec[0] = freq * v[0];
      vec[1] = freq * v[1];
      vec[2] = freq * v[2];
      t += fabs(noise3(vec)) / freq;
   }
   return t;
}
'''