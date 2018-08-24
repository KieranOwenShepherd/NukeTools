from itertools import chain
import nukescripts
import math
import re

selected = nuke.selectedNodes()

#pop up a panel for search item
#regular expression filter on user input
filter = nuke.getInput('Selection Filter','')


#make a dictionary of knob classes and how to get possible options for that knob

class_options = {
                'Channel_Knob'     : lambda x : x.node().channels()+['none'] if x.depth() == 1 else nuke.layers()+['none'],
                'ChannelMask_Knob' : lambda x : x.node().channels()+['none'] if x.depth() == 1 else nuke.layers()+['all','none'],
                'Enumeration_Knob' : lambda x : x.values(),
                'Format_Knob' : lambda x : [ f.name() for f in nuke.formats() if f.name()]
                }

#find any knobs on the nodes that match the types we're aware of
selection_knobs = [ k for n in selected for name,k in n.knobs().items() if k.Class() in class_options ]

#eliminate knobs that dont have a match to user input,and get the settings that match
filtered_knobs = [ ( k,[op for op in class_options[k.Class()](k) if re.match( '.*'+filter , op.lower() ) ] ) for k in selection_knobs ]
filtered_knobs = [ tup for tup in filtered_knobs if tup[1] ]
#'.*'.join(list(filter))
#'.*'+filter

#separate unique
#any knobs that have the same name and same options get grouped together into one
possible_selections = list(set([ (k[0].name(), k[0].label() ,tuple(k[1])) for k in filtered_knobs ]))
print possible_selections

#make a panel that allows us to set knobs
panel = nukescripts.PythonPanel('Set Knobs','test')
panel.addKnob(nuke.String_Knob('',''))
panel.setMinimumSize(400, 400)

#now the tricky part; make python script buttons that do the things I want it to
command = 'for n in nuke.selectedNodes():\n  if {0} in n.knobs():\n    n[{0}].setValue({1})'
#for n in nuke.selectedNodes():
#  if place1 in n.knobs:
#    n[place1].setValue(place2)

for name,label,options in possible_selections:
    if not label:
        label = name
    for option in options:
        python_button = nuke.PyScript_Knob(name+option,'<b>'+label+' -> '+option)
        python_button.setFlag(nuke.STARTLINE)
        python_button.setValue(command.format('"'+name+'"','"'+option+'"') )
        panel.addKnob(python_button)
        
confirm = panel.showModalDialog()

            