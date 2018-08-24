for n in nuke.allNodes('Viewer'):
    n['gain'].setValue(1)
    n['gamma'].setValue(1)