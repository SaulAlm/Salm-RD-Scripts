# Simple script to change the hierarchy folder for InvisibleUniverse studio.
# version 1.01 - 2022.07.25

from maya import cmds

parentGroup = "FX_Grp"
toParentGroup = 'Render_Grp'

def parentFxGrp():
    if cmds.objExists('All_Grp'):
        cmds.parent(parentGroup, toParentGroup)

# Search if exist some nodes in FX_Grp      
def searchNodes():
    someObj= cmds.listRelatives(parentGroup)
    if not str(someObj) == 'None':
        # Call the parent function
        return parentFxGrp()

searchNodes()