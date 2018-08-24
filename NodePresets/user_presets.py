import nuke
def nodePresetsStartup():
  nuke.setUserPreset("Dot", "TODO", {'note_font_color': '0xb73737ff', 'selected': 'true', 'note_font_size': '50', 'label': 'TODO'})
  nuke.setUserPreset("Dot", "smalltext", {'selected': 'true', 'note_font_size': '10'})
  nuke.setUserPreset("Merge2", "+", {'operation': 'plus'})
  nuke.setUserPreset("Merge2", "Mask", {'operation': 'mask'})
  nuke.setUserPreset("Merge2", "Stencil", {'operation': 'stencil'})
  nuke.setUserPreset("Merge2", "From", {'operation': 'from', 'selected': 'true'})
  nuke.setUserPreset("Merge2", "mult", {'operation': 'multiply', 'selected': 'true'})
  nuke.setUserPreset("Shuffle", "AlphaToWhite", {'alpha': 'white', 'selected': 'true', 'label': 'Alpha to White'})
  nuke.setUserPreset("ShuffleCopy", "denoise", {'red2': 'blue', 'out2': 'denoise', 'green2': 'alpha', 'selected': 'true', 'label': 'denoise', 'black': 'red', 'alpha': 'alpha2', 'white': 'green'})
  nuke.setUserPreset("ShuffleCopy", "depth", {'alpha': 'alpha2', 'out2': 'depth', 'selected': 'true', 'black': 'red', 'label': 'depth'})
  nuke.setUserPreset("Tracker4", "NoPreviews", {'zoom_window_behaviour': '4', 'keyframe_display': '3', 'transform': 'stabilize'})
  nuke.setUserPreset("Tracker4", "Stabilize", {'transform': 'stabilize', 'center': '1440 810'})
