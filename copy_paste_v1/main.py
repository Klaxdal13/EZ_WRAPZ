# spoof webapp essentially
from input_svg import svg_in
from formatt import remove_tb as rtb
##from formatt import create_blocks as cb

def main():
    print('EZ WRAPS!')
    print('...')
    print('...')

    file = input('enter filename: ')

    ## read file
    svg_info = svg_in(file)

    # parse info
    glob_paths = svg_info[0]
    attrs = svg_info[1]
    svg_attrs = svg_info[2]

    # step 1, remove top/bottom (also creates blocks)
    rtb(glob_paths)

    

    

    

    

    
    
