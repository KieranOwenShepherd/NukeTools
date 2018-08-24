import fxT_shareNodes

def ttt():
    import tabtabtab
    m_edit = nuke.menu('Nuke').findItem('Edit')
    m_edit.addCommand('Tabtabtab', tabtabtab.main, 'Meta+Tab')

try:
    ttt()
except Exception:
    import traceback
    traceback.print_exc()

try:
    import scripttomenu
except Exception:
    import traceback
    traceback.print_exc()

try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()
	

try:
    import loadshortcuts
except Exception:
    import traceback
    traceback.print_exc()
	

try:
    import setdefaults
except Exception:
    import traceback
    traceback.print_exc()