import textwrap

def node_p_to_c( node, node_pos_xy=None ):
    xy = node_pos_xy if node_pos_xy else [node.xpos(),node.ypos()]
    return [ xy[0] + node.screenWidth()/2, xy[1] + node.screenHeight()/2 ]

def node_c_to_p( node, node_cent_xy=None ):
    xy = node_cent_xy if node_cent_xy else node_p_to_c(node)
    return [ int(xy[0] - node.screenWidth()/2), int(xy[1] - node.screenHeight()/2) ]

n = nuke.selectedNode()

new_label = nuke.getInput('new label',n['label'].getValue())
if n.Class() == 'Dot':
    n['note_font_size'].setValue(50)


#replace keywords with extensions

if not new_label is None:
    #wrap the words nicely
    new_label = textwrap.TextWrapper(width = 16, break_long_words = False).fill(new_label)
    
    old_center = node_p_to_c(n)
    n['label'].setValue(new_label)

    #recenter the node since nuke doesn't do that -_____-
    #plus I need a hack to try make sure the UI updates in time to get the right screen height
    #timer = PySide.QtCore.QTimer
    #timer.singleShot(200, lambda : n.setXYpos(*node_c_to_p(n,old_center)) )