import drawSvg as draw
import math



## fuck svgpath tools and stuff this is it


## ratio likely not needed/ needs to be changed

def build(sides,ratio,thickness):

    ## svg shouldnt be too big for efficiencys sake
    ## only needs to be cx+ 2*flaplength(=cx*0.15) ...
    
    
    cy = sides[0][1]
    cx = sides[0][0]

    flap = (round(0.15*(cx/4),4))
    ## canvas object,
    '''
    cx+flap because it shouldnt be huge, canvas is only as large as it needs to be+ 30 px for margin
    '''
    ##print(cx+(2*flap)+30)
    ##print(cy+(2*flap)+30)
    d= draw.Drawing(700,700,
                    origin='center',
                    displayInline=False)

    maxX = 600/2
    maxY = 600/2
    linex =  -flap 
    xval = -maxX + flap + 15 ## 30 is margin..
    initPos = xval - linex
    initNeg= xval +linex
    inter_pts=[]


    d.append(draw.Line(initNeg,-flap,initNeg, cy/4+(2*flap),stroke='black'))

    for s in sides:

        
        ## ratio * any width = the same rectangle proportionally
        ##ratio = get_side_ratio(s)

       #3 s = (384,649)
       ## print(s)
        w,h = s
        w = w/4
        h = h/4


        ## xval, 0 = BOTTOM LEFT CORNER OF RECT
        d.append(draw.Rectangle(xval,
                       0,
                       w,
                       h,
                       stroke_width=1,
                       stroke='white',
                       fill='none'))
        radians45 = math.radians(45)
        
        ##print('flap= '+str(solveforx))
        ##d.append(draw.Line(xval,0,initPos, -flap,stroke='black'))
        ##d.append(draw.Line(xval,0,initNeg, -flap,stroke='black'))

        ## bottom triangles
        d.append(draw.Line(xval,0,initPos, -flap,stroke='black'))
        d.append(draw.Line(xval,0,initNeg, -flap,stroke='black'))

        d.append(draw.Line(initPos,-flap,initPos+w-(flap*2), -flap,stroke='black'))


        ## connect bottom triangles
        

        ## 
        
            
        xval+= w
        initPos += w
        initNeg += w

        print(xval)
    ##triangle= draw.Lines(
    
    ##d.append(draw.Line(initPos,-flap,initPos+w-(flap), -flap,stroke='black'))
    
    ##

    d.append(draw.Line(initPos-(flap*2), -flap, initPos-(flap*2)+flap,0,stroke='black'))
    d.append(draw.Line(initPos-(flap*2)+flap,0,initNeg+flap,cy/4+(2*flap),stroke='black'))

    
    d.saveSvg('ex.svg')



## size as a percent of surface
##def get_flap_size(size):


def get_side_ratio(dim):
     ## rectangular
    ratio = dim[1]/dim[0]
    return ratio


##build([(384.0, 649.0), (361.0, 649.0), (384.0, 649.0), (361.0, 649.0)], 1.6901041666666667, 11.5)
