sn = nuke.selectedNode()
nuke.Root()['first_frame'].setValue(1001)
nuke.Root()['last_frame'].setValue(sn['last'].getValue()-sn['first'].getValue()+1001)
sn['frame_mode'].setValue(1)
sn['frame'].setValue('1001')
nuke.Root()['format'].setValue(sn.format().name())
nuke.frame(1001)