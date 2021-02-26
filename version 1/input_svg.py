## TO DO TOMORROW:

'''
1. get PATH objects to occur as single var -- done
2. combine them by the corners ( x 4)

NEXT DAY:

1. add triangles ( on all 



'''






# create svgpathtools Path objects from an SVG file
from svgpathtools import svg2paths2, parse_path, wsvg
import svgwrite
import sys
from os import path


def svg_in(svg_location):

    
    
    if path.exists(svg_location):
            
        paths, attributes, svg_attributes = svg2paths2(svg_location)
        ##for i in range(4):
            ##wsvg(p,filename='blocks/b_block_'+str(i)+'.svg')
        
        ##print(svg_info)
        return [paths, attributes, svg_attributes]
        


    elif not svg_location.endswith('.svg'):
        sys.exit("invalid filename or extension")
        



## this needs to be passed from the webapp :/

##x=svg_in("img_source/tester_1.svg")




