first = nuke.Root()['first_frame'].getValue()
last  = nuke.Root()['last_frame'].getValue()

operate_on = nuke.selectedNodes()
if not operate_on:
    operate_on = nuke.allNodes()
for node in [n for n in operate_on if n.Class() == 'Read']:
    if 'maya' in node['file'].getValue(): #if it's a render
        node['colorspace'].setValue('linear')
    elif 'dpx' in node['file'].getValue():
        node['colorspace'].setValue('AlexaV3LogC')
    #always crush the framerange to frame 1001
    node['frame_mode'].setValue(1)
    node['frame'].setValue('1001')

    #convert single frames to sequences
    path = node['file'].getValue()
    sequence = next( seq for seq in nuke.getFileNameList('/'.join(path.split('/')[:-1])) if path.split('/')[-1].split('.')[0] in seq )
    node['file'].fromUserText('/'.join(path.split('/')[:-1] + [sequence]))

for node in [n for n in operate_on if 'Write' in n.name()]:
    node['colorspace'].setValue('AlexaV3LogC')

#reload all reads
for node in nuke.allNodes('Read'):
        node['reload'].execute()

nuke.Root()['first_frame'].setValue(first)
nuke.Root()['last_frame'].setValue(last)