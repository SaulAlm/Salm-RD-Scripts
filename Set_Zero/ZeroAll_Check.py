# This script will zero all atributes translate, rotate and scale selected objects
# For Dp_Ar_control will copy originalRotate values to Rotate.
from maya import cmds
import dpAutoRigSystem
import dpAutoRigSystem.dpAutoRig as autoRig
from dpAutoRigSystem.Extras import dpSelectAllControls

loadedModuleList = dir()
print(loadedModuleList)

def checkToPublish():
    # Function to call UpdateRigInfo and SelectAllControls Dp functions
    def callUpdateRigInfo():
        # Execute updateRigInfo function
        autoRig.rigInfo.UpdateRigInfo.updateRigInfoLists()
    
    def callSelectAllControls():
        # Execute dpSelectAllControls fuction
        dpSelectAllControls.SelectAllControls(autoRigUI, autoRigUI.langDic, autoRigUI.langName)
        # autoRigUI.initExtraModule("dpSelectAllControls", "Extras")
        #zeroAllTransform()
        

    # Function to Zero controls
    def zeroAllTransform():
        #callSelectAllControls()
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
            # clearSelection = cmds.select(cl=True)

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
        return


        
    if "autoRigUI" in loadedModuleList:
        global autoRigUI
        # to action UpdateRigInfo Dp fuction 
        callUpdateRigInfo()
        # to action SelectAllControls Dp fuction 
        callSelectAllControls()
        # Function to zero all Translate, Rotate and Scale selected controls
        zeroAllTransform()
        


    else:
        print("ELSE")
        autoRigUI = autoRig.DP_AutoRig_UI()
        #callSelectAllControls()

checkToPublish()

# TO DO

# -> Função para selecionar todos os atributos adicionais dos controles
# -> Mudar sistema Sistema leitura e adicionar condição para "useOriginalRotate"
