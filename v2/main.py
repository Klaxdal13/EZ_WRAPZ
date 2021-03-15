from formatt import *
from builder import build as dr


def main():
    s,t = format_svg('10x18.svg')
    dr(s,t)
    
    
main()
