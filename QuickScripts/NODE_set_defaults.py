sn = nuke.selectedNode()
non_default_knobs = sn.writeKnobs(nuke.WRITE_NON_DEFAULT_ONLY).split(' ')

#set as defaults now and also add lines to the script that sets defaults in the future
with open('C:\Users\oasis3d\.nuke\setdefaults.py','a') as file:
    for k in non_default_knobs:
        setting = ( sn.Class()+'.'+k , sn[k].toScript() )
        nuke.knobDefault(*setting)
        file.write( '\nnuke.knobDefault( "{}" , "{}" ) '.format(*setting) )