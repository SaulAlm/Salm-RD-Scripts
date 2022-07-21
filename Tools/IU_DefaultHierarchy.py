# Ultra simple script to change the hierarchy folder for InvisibleUniverse studio.

from maya import cmds

def parentFxGrp():
    if cmds.objExists('All_Grp'):
        cmds.parent('FX_Grp', 'Render_Grp')
        
parentFxGrp()