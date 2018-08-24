import math
import re

selected = nuke.selectedNode()
layers = nuke.layers(selected)

#now regular expression filter on user input
filter = nuke.getInput('Layer Filter','rgb')
layers = [ l for l in layers if re.match( '.*'+'.*'.join(list(filter)), l ) ]
print layers

selected.setSelected(False)

row_length = int(math.ceil(math.sqrt(len(layers))))
grid_size = 80

for row in reversed(range(row_length)):
    for col in range(row_length):
        l_number = row_length*row + col
        if l_number < len(layers):
            shuffle = nuke.nodes.Shuffle()
            shuffle.connectInput(0,selected)
            shuffle['in'].setValue(layers[l_number])
            shuffle['label'].setValue('[value in]')
            shuffle['postage_stamp'].setValue(True)
            shuffle.setXYpos( selected.xpos() + grid_size*col, selected.ypos() + grid_size*row )
            shuffle.setSelected(True)