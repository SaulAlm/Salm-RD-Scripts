# This script will zero translate to zero transform in selected objects.

import maya.cmds as cmds

sel = cmds.ls(sl=True)
axis = ['X','Y','Z']
for item in sel:
    for a in axis:
        try:
            cmds.setAttr(item+'.translate'+a, 0)
        except:
            pass