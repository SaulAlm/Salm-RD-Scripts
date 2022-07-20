# This script will zero all atributes translate, rotate and scale selected objects
# For Dp_Ar_control will copy originalRotate values to Rotate.
import maya.cmds as cmds

# Declaring variables
selList = cmds.ls(sl=True)
axisList = ['X','Y','Z']
dpControl = 'originalRotate'

for item in selList:
    for axis in axisList:
        try:
            cmds.setAttr(item+'.translate'+axis, 0)
            cmds.setAttr(item+'.scale'+axis, 1)
        except Exception as e:
            print(e)
    #check if OriginalRotate atributte exist.
        if not cmds.objExists(item+'.'+dpControl+axis) is True:
            # set each axis to zero.
            try:
                cmds.setAttr(item+'.rotate'+axis, 0)
            except Exception as e:
                print(e)                  
        else:
            try:
                origRotate = cmds.getAttr(item+'.'+dpControl+axis)
                copyAtribute = cmds.setAttr(item+'.rotate'+axis,origRotate)
            except Exception as e:
                print(e)