import math
import numpy as np

def get_velocity_vortex(strength, xv, yv, X, Y):
    u = +strength / (2 * math.pi) * (Y - yv) / ((X - xv)**2 + (Y - yv)**2)
    v = -strength / (2 * math.pi) * (X - xv) / ((X - xv)**2 + (Y - yv)**2)
    
    return u , v
    
def get_stream_vortex(strength, xv, yv, X, Y):
    psi = strength / (4 * math.pi) * np.log((X - xv)**2 + (Y - yv)**2)
    
    return psi
    
def get_velocity_source(strength, xs, ys, X, Y):
    
    u = strength / (2 * math.pi) * (X - xs) / ((X - xs)**2 + (Y - ys)**2)
    v = strength / (2 * math.pi) * (Y - ys) / ((X - xs)**2 + (Y - ys)**2)
    
    return u , v
    
def get_stream_func_source(strength, xs, ys, X, Y):
    psi = strength / (2 * math.pi) * np.arctan2((Y - ys), (X - xs))
    
    return psi
    
def get_velo_doublet(strength, xd, yd, X, Y):
    u = (-strength / (2*math.pi) *
        ((X - xd)**2 - (Y - yd)**2) /
        ((X - xd)**2 + (Y - yd)**2)**2)
    v = (-strength / (2*math.pi) *
        2 * (X - xd) * (Y - yd) /
        ((X - xd)**2 + (Y - yd)**2)**2)
    
    return u, v
    
def get_streamfunc_doublet(strength, xd, yd, X, Y):
    
    psi = (-strength / (2*math.pi) * 
           (Y - yd) / ((X - xd)**2 +
                       (Y - yd)**2))
    return psi