import nuke
import operator

def node_p_to_c( node, node_pos_xy=None ):
    xy = node_pos_xy if node_pos_xy else [node.xpos(),node.ypos()]
    return [ xy[0] + node.screenWidth()/2, xy[1] + node.screenHeight()/2 ]

def node_c_to_p( node, node_cent_xy=None ):
    xy = node_cent_xy if node_cent_xy else node_p_to_c(node)
    return [ int(xy[0] - node.screenWidth()/2), int(xy[1] - node.screenHeight()/2) ]

def getnodecolor( node ):
    if node['tile_color'].toScript() is '0':
       return nuke.defaultNodeColor( node.Class() )
    return node['tile_color'].getValue()

head = nuke.selectedNode()
out_attached = [node for node in nuke.allNodes() if head in [node.input(n) for n in range(node.inputs())] and not node.Class() in 'Viewer' ]
out_attached.sort( key = operator.methodcaller('ypos') )
chain = [head]
for node in out_attached:
    dotnode = nuke.nodes.Dot()
    dotnode.setXpos(   node_c_to_p(  dotnode, node_p_to_c(head)  )[0]   )
    dotnode.setYpos(   node_c_to_p(  dotnode, node_p_to_c(node)  )[1]   )
    dotnode['tile_color'].setValue(int(getnodecolor(head)))
    dotnode.setInput(0,chain[-1]) #attach to last link
    chain.append(dotnode)
    dotnode.setSelected(True)
    for n in range(node.inputs()): 
        if node.input(n) is head:
            node.setInput(n,dotnode) 