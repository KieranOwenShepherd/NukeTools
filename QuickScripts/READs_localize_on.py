nodes = nuke.selectedNodes()

for n in nodes:
    if n.Class() == 'Read':
        n['localizationPolicy'].setValue('on')