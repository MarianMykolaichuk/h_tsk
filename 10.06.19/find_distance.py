# Given two ordered pairs calculate the distance between them.
#  Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**.5
    return round(dist,2)
    