
#this is a group node
g = nuke.selectedNode()
knobs_to_link = nuke.getInput('Knobs to expose','size')
knobs_toadd = [k.strip() for k in knobs_to_link.split(',')]
to_link = []

with g:
    for n in nuke.allNodes():
        for k_a in knobs_toadd:
            for knobname,k in n.knobs().items():
                if k_a in k.fullyQualifiedName():
                    to_link.append(( n.name() , knobname ))

for node, knob in to_link:
    link_knob = nuke.Link_Knob(knob, knob)
    link_knob.makeLink(node,knob)
    g.addKnob(link_knob)