# This script will check and zero all defined Dp_Ar atributes and transformations. 
# For Dp_Ar_control will copy originalRotate values to Rotate and zero some extra.

# version 1.01 - 2022.08.10

""" Thanks for collaborators:
    | Danilo Pinheiro |
    | André Almeida   |
    | Caio Hidaka     |
"""
from maya import cmds
import dpAutoRigSystem
import dpAutoRigSystem.dpAutoRig as autoRig
from dpAutoRigSystem.Extras import dpSelectAllControls

loadedModuleList = dir()
print(loadedModuleList)

def checkToPublish():
    # List with all atributes to set zero values. 
    setZeroList = ['twist', 'outsideRoll','outsideSpin', 'insideRoll', 'insideSpin',
                   'heelRoll', 'heelSpin', 'toeRoll', 'toeSpin', 'ballRoll', 'ballTurn',
                   'ballSpin', 'footRoll','sideRoll', 'baseTwist', 'phalange1', 'phalange2', 'phalange3',
                   'L_Puff', 'R_Puff', 'Pucker', 'BigSmile', 'AAA', 'OOO', 'UUU', 'FFF', 'MMM']
    # List with all atributes to set one values.
    setOneList = ['stretchable', 'length', 'uniformScale', 'showControls', 'active',
                  'scaleCompensate', ]
    
    
    # Function to call UpdateRigInfo and SelectAllControls Dp functions
    def callUpdateRigInfo():
        # Execute updateRigInfo function
        autoRig.rigInfo.UpdateRigInfo.updateRigInfoLists()
    
    def callSelectAllControls():
        # Execute dpSelectAllControls fuction
        dpSelectAllControls.SelectAllControls(autoRigUI, autoRigUI.langDic, autoRigUI.langName)

    # Function to Zero controls
    def zeroAllTransform():
        selList = cmds.ls(sl=True)
        axisList = ['X','Y','Z']
        dpControl = 'originalRotate'

        for item in selList:
            for axis in axisList:
                try:
                    cmds.setAttr(item+'.translate'+axis, 0)
                except Exception as e:
                    print(e)
                try:
                    cmds.setAttr(item+'.rotate'+axis, 0)
                    # Check if 'useOriginalRotation' atribute exist.
                    if not cmds.objExists(item+'.useOriginalRotation'):
                        origRotate = cmds.getAttr(item+'.'+dpControl+axis)
                        cmds.setAttr(item+'.rotate'+axis,origRotate)
                except Exception as e:
                    print(e)
                try:
                    cmds.setAttr(item+'.scale'+axis, 1)
                except Exception as e:
                    print(e)                   
    
    # This function will zero all extra atributes in DpControls
    def zeroExtraAtributes():
        controlsList = cmds.ls(sl=True)
        for ctrl in controlsList:
            userDefAttrList = cmds.listAttr(ctrl, userDefined=True)
            for attr in userDefAttrList:
                if attr in setZeroList:
                    try:
                        cmds.setAttr(ctrl+'.'+attr,0)
                    except Exception as e:
                        print(e)
                elif attr in setOneList:
                    try:
                        cmds.setAttr(ctrl+'.'+attr,1)
                    except Exception as e:
                        print(e)

    # Function to hide Data_Grp
    def hideDataGroup():
        cmds.setAttr('Data_Grp.visibility', 0)

    def mainFunction():
        # to action UpdateRigInfo Dp fuction 
        callUpdateRigInfo()
        # to action SelectAllControls Dp fuction 
        callSelectAllControls()
        # Function to zero all Translate, Rotate and Scale selected controls
        zeroAllTransform()
        # Zero all aditional atributes
        zeroExtraAtributes()
        # Hide Data_Grp
        hideDataGroup()   
    
    if "autoRigUI" not in loadedModuleList:
        global autoRigUI
        autoRigUI = autoRig.DP_AutoRig_UI()
        
    mainFunction()

checkToPublish()
