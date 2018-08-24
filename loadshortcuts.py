import os
import nuke

def _restore_overrides(overrides):
    for item, key in overrides.items():
        menu_name, _, path = item.partition("/")
        m = nuke.menu(menu_name)
        item = m.findItem(path)
        if item is None:
            nuke.warning("WARNING: %r (menu: %r) does not exist?" % (path, menu_name))
        else:
            #print "Restoring shortcut %r for %r (menu: %r)" % (key, path, menu_name)
            item.setShortcut(key)
			
def _load_yaml(path):
    def _load_internal():
        import json
        if not os.path.isfile(path):
            print "Settings file %r does not exist" % (path)
            return
        f = open(path)
        overrides = json.load(f)
        f.close()
        return overrides

    # Catch any errors, print traceback and continue
    try:
        return _load_internal()
    except Exception:
        print "Error loading %r" % path
        import traceback
        traceback.print_exc()

        return None
		

path = os.path.expanduser("~/.nuke/shortcuteditor_settings.json")
settings = _load_yaml(path)
overrides = settings['overrides']
_restore_overrides(overrides)