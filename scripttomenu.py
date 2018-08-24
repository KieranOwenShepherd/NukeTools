import os
import sys
import nuke

script_folder = os.path.dirname(__file__)+'/'+'QuickScripts'
sys.path.insert(0, script_folder)

#let shortcuts be handled by bens script

#dump all commands within my menu
#if theres no my menu add one
nuke_menu = nuke.menu("Nuke")
mymenu_name = "QuickScripts"

menu = nuke_menu.findItem(mymenu_name)
if menu:
    menu.clearMenu()
else:
    menu = nuke_menu.addMenu(mymenu_name)


#scan through directory for python files
#create menu items which in turn run the scripts
modules = os.listdir(script_folder)
for m in modules:
    if m[-3:] == '.py':
        menu.addCommand(m[:-3], lambda s=script_folder+'/'+m: execfile(s,globals()))
        