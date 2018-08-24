import nukescripts
sn = nuke.selectedNode()

#make a panel that we use to apply presets
class buttonPanel(nukescripts.PythonPanel): 
    def knobChanged(self,knob):
        #manually set presets because nuke sets other knobs to default and I don't want that
        for knob_name, setting in nuke.getUserPresetKnobValues( nuke.selectedNode().Class() , knob.name()).items():
            nuke.selectedNode()[knob_name].fromScript(setting)
        self.ok()

panel = buttonPanel('Presets','presets')
panel.setMinimumSize(100, 100)

for preset in nuke.getUserPresets(sn):
    python_button = nuke.PyScript_Knob(preset,preset)
    python_button.setFlag(nuke.STARTLINE)
    panel.addKnob(python_button)

confirm = panel.showModal()