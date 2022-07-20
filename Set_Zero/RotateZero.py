# This script will zero rotate to zero transform in selected objects.
# And copy original rotate values if is Dp_AR control.

import maya.cmds as cmds

# Declaring variables
selection = cmds.ls(sl=True)
dpControl = 'originalRotate'
axis = ['X','Y','Z']

#For selected object.
for item in selection:
    #check if OriginalRotate atributte exist.
    if not cmds.objExists(item+'.'+dpControl+"X") is True:
        # set each axis to zero.
        for a in axis:
            try:
                cmds.setAttr(item+'.rotate'+a, 0)
            except:
                pass
    else:
        for i in axis:
            try:
                origRotate = cmds.getAttr(item+'.'+dpControl+i)
                copyAtribute = cmds.setAttr(item+'.rotate'+i,origRotate)
            except:
                pass
            