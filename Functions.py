from PIL import Image, ImageDraw
from random import randint
import os
import collections

#Background Functions
def getBackground(num):
    background = Image.open(r"Images\Background\{}.png".format(num))
    return background
def getBackgroundFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Background'))
def getRandomBackground():
    num = randint(0,getBackgroundFolderSize()-1)
    if(num >= 18):
        num = randint(0,getBackgroundFolderSize()-1)
        if(num >= 22):
            num = randint(0,getBackgroundFolderSize()-1)

    return num
def getBlank():
    background = Image.open(r"resources\0.png")
    return background

#Case Functions
def getCaseNzxt(num):
    case = Image.open(r"Images\Case\NZXT\{}.png".format(num))
    return case
def getCaseNzxtFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Case/NZXT'))
def getRandomCaseNzxt():
    return randint(0,getCaseNzxtFolderSize()-1)

def getCasePhanteks(num):
    case = Image.open(r"Images\Case\Phanteks\{}.png".format(num))
    return case
def getCasePhanteksFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Case/Phanteks'))
def getRandomCasePhanteks():
    return randint(0,getCasePhanteksFolderSize()-1)

def getCaseBitFenix(num):
    case = Image.open(r"Images\Case\BitFenix\{}.png".format(num))
    return case
def getCaseBitFenixFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Case/BitFenix'))
def getRandomCaseBitFenix():
    return randint(0,getCaseBitFenixFolderSize()-1)


#Glass Overlay Functions
def getNzxtGlass():
    glass = Image.open(r"Images\Glass\NzxtGlass\0.png")
    return glass
def getPhanteksGlass(num):
    glass = Image.open(r"Images\Glass\PhanteksGlass\{}.png".format(num)) 
    return glass
def getBitFenixGlass():
    glass = Image.open(r"Images\Glass\BitFenixGlass\0.png") 
    return glass

#Cpu Functions
def getCPU(num):
    cpu = Image.open((r"Images\CPU\{}.png".format(num)))
    return cpu
def getCPUFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/CPU'))
def getRandomCPU():
    return randint(0,getCPUFolderSize()-1)

def getAIO(num):
    AIO = Image.open((r"Images\AIO\{}.png".format(num)))
    return AIO
def getAIOFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/AIO'))
def getRandomAIO():
    return randint(0,getAIOFolderSize()-1)

#GPU Functions
def getGPU(num):
    gpu = Image.open(r"Images\GPU\{}.png".format(num))
    return gpu
def getGPUFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/GPU'))
def getRandomGPU():
    return randint(0,getGPUFolderSize()-1)


#Motherboard Functions
def getMotherboardATX(num):
    motherboard= Image.open(r"Images\Motherboard\ATX\{}.png".format(num))
    return motherboard
def getMotherboardATXFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Motherboard/ATX'))
def getRandomMotherBoardATX():
    return randint(0,getMotherboardATXFolderSize()-1)

def getMotherboardMATX(num):
    motherboard= Image.open(r"Images\Motherboard\MATX\{}.png".format(num))
    return motherboard
def getMotherboardMATXFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Motherboard/MATX'))
def getRandomMotherBoardMATX():
    return randint(0,getMotherboardMATXFolderSize()-1)

def getMotherboardITX(num):
    motherboard= Image.open(r"Images\Motherboard\ITX\{}.png".format(num))
    return motherboard
def getMotherboardITXFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Motherboard/ITX'))
def getRandomMotherBoardITX():
    return randint(0,getMotherboardITXFolderSize()-1)


#Ram Functions
def getRam(num):
    ram = Image.open((r"Images\Ram\{}.png".format(num)))
    return ram
def getRamFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Ram'))
def getRamdomRam():
    return randint(0,getRamFolderSize()-1)


#Psu Functions
def getPSU(num):
    psu = Image.open((r"Images\PSU\{}.png".format(num)))
    return psu
def getPSUFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/PSU'))
def getRandomPSU():
    return randint(0,getPSUFolderSize()-1)


#Sticker Functions ( for case )
def getStickerFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/Stickers'))
def getSticker(num):
    sticker = Image.open(r"Images\Stickers\{}.png".format(num))
    return sticker
def getRandomSticker():
    return randint(0,getStickerFolderSize()-1)

#Case Fan Functinos
def getCaseFanLeft(num):
    fan = Image.open((r"Images\CaseFans\Left\{}.png".format(num)))
    return fan
def getCaseFanRight(num):
    fan = Image.open((r"Images\CaseFans\Left\{}.png".format(num))).rotate(180)
    return fan
def getCaseFanTop(num):
    fan = Image.open((r"Images\CaseFans\Left\{}.png".format(num))).rotate(270,expand=True)
    return fan
def getCaseFanFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/CaseFans/Left'))
def getRandomCaseFan():
    return randint(0,getCaseFanFolderSize()-1)

def getBlackCpufan(num):
    fan = Image.open((r"Images\CpuFans\Black\{}.png".format(num)))
    return fan
def getBlackCpuFanFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/CpuFans/Black'))
def getRandomBlackCpuFan():
    return randint(0,getBlackCpuFanFolderSize()-1)

def getWhiteCpufan(num):
    fan = Image.open((r"Images\CpuFans\White\{}.png".format(num)))
    return fan
def getWhiteCpuFanFolderSize():
    return len(os.listdir('C:/Users/Danny/Desktop/NFT/Images/CpuFans/White'))
def getRandomWhiteCpuFan():
    return randint(0,getWhiteCpuFanFolderSize()-1)
#generation function

def exists(list,param):
    
    for i in list:
        
        if(collections.Counter(param) == collections.Counter(i)):
            print("duped", i)
            return True
    
    print(param)
    
    return False
#save
def save(img, count):
    img.save(r"Outputs\{}.png".format(count))

def savePerfect(img,count):
    img.save(r"Perfect\{}.png".format(count))

def saveBitfenix(img,count):
    img.save(r"Outputs\Bitfenix\{}.png".format(count))
def saveNzxt(img,count):
    img.save(r"Outputs\NZXT\{}.png".format(count))
def savePhanteks(img,count):
    img.save(r"Outputs\Phanteks\{}.png".format(count))

def writeListPhanteks(list):
    list = [str(list[0]),str(list[1]),str(list[2]),str(list[3]),str(list[4]),str(list[5]),str(list[6]),str(list[7]),str(list[8]),str(list[9]),str(list[10])]
    text =  open("Lists/phanteksList.txt","a")
    text.write(','.join(list) + "=")
    text.close()

def writeListBitfenix(list):
    list = [str(list[0]),str(list[1]),str(list[2]),str(list[3]),str(list[4]),str(list[5]),str(list[6]),str(list[7]),str(list[8]),str(list[9]),str(list[10])]
    text =  open("Lists/bitfenixList.txt","a")
    text.write(','.join(list) + "=")
    text.close()

def writeListNzxt(list):
    list = [str(list[0]),str(list[1]),str(list[2]),str(list[3]),str(list[4]),str(list[5]),str(list[6]),str(list[7]),str(list[8]),str(list[9]),str(list[10])]
    text =  open("Lists/nzxtList.txt","a")
    text.write(','.join(list) + "=")
    text.close()

def clenseList():
    text1= open("Lists/nzxtList.txt","w")
    text2= open("Lists/bitfenixList.txt","w")
    text3= open("Lists/phanteksList.txt","w")
    text1.write('')
    text2.write('')
    text3.write('')
    text1.close()
    text2.close()
    text3.close()


#List  0=case 1=cpu 2=gpu 3=motherboard 4=ram 5=psu 

#generateImageATX([2,1,2,2,1,0]).show()


#save(generateImageATX([0,3,3,2,3,0]),"test")

#
#generateImageATX([0,3,3,2,3,0]).show()


#Get Random Build
#generateRamdomAtx().show()


#gpu corssfire
#multiple rams
#ATX/MicroATX/miniITX