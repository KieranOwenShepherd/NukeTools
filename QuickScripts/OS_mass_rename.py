import os

dir = '//ALFRED/Post-3D-VFX/Shotgun/thenightingale_3366/sequences/011_MSH/011_MSH_040/Comp/work/images/move that guy/v002/'
for f in os.listdir(dir):
    os.rename(dir+f,dir+f.replace('v001','v002'))