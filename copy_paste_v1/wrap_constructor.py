## CONSTRUCTOR
## GOAL: to take the bblocks and make a line of 4
'''
[][][][]

where [] is a bblock svg file
'''

import svgutils.transform as sg
from svgutils.compose import *
import sys



def create_figure():

##    fin = Figure("500px","500px",
##                 SVG("blocks/b_block_0.svg").scale(0.6),
##                 SVG("blocks/b_block_1.svg").scale(0.6),
##                 SVG("blocks/b_block_2.svg").scale(0.6),
##                 SVG("blocks/b_block_3.svg").scale(0.6),
##                 ).tile(4,1)
##    fin.save("skeleton.svg")

    f = Figure("16cm","6.5cm",
           SVG("blocks/b_block_0.svg").scale(0.6).move("8cm","1cm"))

    f.save('skele.svg')
















## will definetley have params
##def construct(x=1700,y=1820):
##    fig= sg.SVGFigure("16cm","6.5cm")
##
##    fig0 = sg.fromfile('blocks/b_block_0.svg')
##    fig1 = sg.fromfile('blocks/b_block_0.svg')
##
##    plot0 = fig0.getroot()
##    plot1 = fig1.getroot()
##    
##
##    plot1.moveto(600,0)
##    
##    
##
##    fig.append([plot0,plot1])
##
##    fig.save("final_img.svg")
