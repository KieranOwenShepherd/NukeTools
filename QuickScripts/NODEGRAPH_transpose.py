selected = nuke.selectedNodes()

def reflection( x, y , pivot ):
    return (y-pivot[1]+pivot[0] , x-pivot[0]+pivot[1])

pivot = ( min( n.xpos() for n in selected ), min( n.ypos() for n in selected ))

for node in selected:
    node.setXYpos(*reflection(node.xpos(),node.ypos(),pivot))