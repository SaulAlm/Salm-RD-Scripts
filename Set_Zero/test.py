# This script will zero all atributes translate, rotate and scale selected objects
# For Dp_Ar_control will copy originalRotate values to Rotate.
from maya import cmds
import dpAutoRigSystem
import dpAutoRigSystem.dpAutoRig as autoRig
from dpAutoRigSystem.Extras import dpSelectAllControls

loadedModuleList = dir()
print(loadedModuleList)

def checkToPublish():
    setZeroList = ['twist', 'outsideRoll','outsideSpin', 'insideRoll', 'insideSpin',
                   'heelRoll', 'heelSpin', 'toeRoll', 'toeSpin', 'ballRoll', 'ballTurn',
                   'ballSpin', 'footRoll','sideRoll', 
                   'baseTwist',
                   'L_Puff', 'R_Puff', 'Pucker', 'BigSmile', 'AAA', 'OOO', 'UUU', 'FFF', 'MMM']
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
                        copyAtribute = cmds.setAttr(item+'.rotate'+axis,origRotate)
                except Exception as e:
                    print(e)
                try:
                    cmds.setAttr(item+'.scale'+axis, 1)
                except Exception as e:
                    print(e)

    def setCalibration():
        selList = cmds.ls(sl=True)
        for item in selList:
            if cmds.objExists(item+".calibrationList"):
                calibrationList = cmds.getAttr(item+".calibrationList")
                calibrationList = calibrationList.split(";")
                print(calibrationList)
                for atribute in calibrationList:
                    if cmds.objExists(item+"."+"default"+atribute.capitalize()):
                        print("Atributo Default Value Existe!")
                        defaultAtributeValue = cmds.getAttr(item+"."+"default"+atribute.capitalize())
                        print(defaultAtributeValue)
                        pasteDefaultValue = cmds.setAttr(item+"."+atribute,defaultAtributeValue)
                    else:
                        print("DefaulValue Nao existe")
                        createDefaultAttrValue()
            else:
                print("No have calibration List")
                        
    # Function to create default attribute value                
    def createDefaultAttrValue():
        selList = cmds.ls(sl=True)
        for item in selList:
            calibrationList = cmds.getAttr(item+".calibrationList")
            calibrationList = calibrationList.split(";")
            print(calibrationList)
            for a in calibrationList:
                print(a)
                newAttr = cmds.addAttr(longName="default"+a.title())
                print(newAttr)
    
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
        # Copy default value atributes
        """copyDefaultValues()"""
        # Hide Data_Grp
        hideDataGroup()   
    
    if "autoRigUI" not in loadedModuleList:
        global autoRigUI
        autoRigUI = autoRig.DP_AutoRig_UI()
        
    mainFunction()

checkToPublish()
