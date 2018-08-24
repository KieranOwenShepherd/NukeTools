import os
#print 'explorer %s' % '\\'.join(nuke.root().name().split('/')[:-1])

file = ''

if nuke.selectedNodes() and  'file' in nuke.selectedNode().knobs():
    file = nuke.selectedNode()['file'].getValue()
else:
    file = nuke.root().name()

os.system('explorer %s' % '\\'.join(file.split('/')[:-1]))