from Functions import *

def generateImagePhanteksPerfect(list):

    backgroundVar = getRandomBackground()
    background = getBackground(backgroundVar)
    case = getCasePhanteks(list[0])
    cpu = getCPU(list[1])
    gpu = getGPU(list[2])
    motherboard = getMotherboardMATX(list[3])
    
    ram = getRam(list[4])
    glass = getPhanteksGlass(list[0])
    
    psu = getPSU(list[5])

    caseFanVar = getRandomCaseFan()
    caseFanLeft = getCaseFanLeft(caseFanVar)
    caseFanRight = getCaseFanRight(caseFanVar)
    caseFanTop = getCaseFanTop(caseFanVar)

    caseX = 23
    caseY = 36
    motherboardX = caseX + 14
    motherboardY = caseY + 22
    ramIndent = 6
    caseFanIndent = 54
    aio = 0
    gpuIndent = 22

    background.paste(case, (caseX,caseY), mask = case)

    stickerVar = randint(1,5)
    if(stickerVar == 1):
        sticker = getSticker(getRandomSticker())
        sticker.thumbnail((45,45))

        heightVar = randint(20,115)
        widthVar = randint(120,130)

        background.paste(sticker, (caseX+widthVar,caseY+heightVar), mask = sticker)
        
        if(heightVar <=40):
            sticker2 = getSticker(getRandomSticker())
            sticker2.thumbnail((50,50))

            widthVar = randint(120,130)
            heightVar = randint(60,115)
            background.paste(sticker2,(caseX + widthVar , caseY + heightVar), mask = sticker2)

            if(heightVar <=80):
                sticker3 = getSticker(getRandomSticker())
                sticker3.thumbnail((50,50))

                widthVar = randint(120,130)
                heightVar = randint(100,115)
                background.paste(sticker3,(caseX + widthVar , caseY + heightVar), mask = sticker3)
        
    background.paste(motherboard, (motherboardX,motherboardY), mask = motherboard)

    if list[1] >= 12:
        fanVariable = getRandomCaseFan()
        fan = getCaseFanLeft(fanVariable)
        background.paste(fan, (motherboardX +35, motherboardY+8 ),mask = fan)

    background.paste(cpu, (motherboardX + 20 , motherboardY + 8), mask = cpu) #change param
    background.paste(psu,(caseX + 11,caseY + 127), mask = psu)

  

    gpuVariable = randint(0,10) 
    if gpuVariable < 1:
        background.paste(gpu,(motherboardX ,caseY + 81 + gpuIndent), mask = gpu)
        background.paste(gpu, (motherboardX  ,caseY+ 81), mask = gpu)
    background.paste(gpu, (motherboardX  ,caseY+ 81), mask = gpu) 

    background.paste(caseFanLeft, (caseX+14,caseY+25), mask = caseFanLeft)
    background.paste(caseFanTop, (caseX+30 ,caseY+16), mask = caseFanTop)    
    background.paste(caseFanTop, (caseX+30 + caseFanIndent,caseY+16), mask = caseFanTop)
    background.paste(caseFanRight, (caseX+152,caseY+18), mask = caseFanRight)
    background.paste(caseFanRight, (caseX+152,caseY+18 + caseFanIndent), mask = caseFanRight)
    
    if list[1] == 12:
        fanVariable = getRandomWhiteCpuFan()
        fan = getWhiteCpufan(fanVariable)
        background.paste(fan, (motherboardX +60, motherboardY+8 ),mask = fan)
        background.paste(cpu, (motherboardX + 25 , motherboardY + 8), mask = cpu)

    if list[1] == 13:
        fanVariable = getRandomBlackCpuFan()
        fan = getBlackCpufan(fanVariable)
        background.paste(fan, (motherboardX +60, motherboardY+8 ),mask = fan)
        background.paste(cpu, (motherboardX + 25 , motherboardY + 8), mask = cpu)

    background.paste(ram, (motherboardX+ 73,motherboardY +8), mask = ram) #change param
    background.paste(ram, (motherboardX + 73 + ramIndent,motherboardY +8), mask = ram)
    background.paste(ram, (motherboardX + 73 + ramIndent*2,motherboardY +8), mask = ram)
    background.paste(ram, (motherboardX + 73 + ramIndent*3,motherboardY +8), mask = ram)

    if list[1] <=11 and list[1] >=8:
        aioVariable = getRandomAIO()
        AIO = getAIO(aioVariable)
        background.paste(AIO, (motherboardX , motherboardY ),mask = AIO)

    background.paste(glass, (caseX+3, caseY+9), mask = glass)

    writeListPhanteks([backgroundVar,list[0],caseFanVar,list[1],list[2],list[3],list[5],list[4]])

    return background
    
#generateImageNZXT  #List  0=case 1=cpu 2=gpu 3=motherboard 4=ram 5=psu

def generateImageNZXTPerfect(list):

    backgroundvar = getRandomBackground()
    background = getBackground(backgroundvar)
    case = getCaseNzxt(list[0])
    cpu = getCPU(list[1])
    gpu = getGPU(list[2])
    motherboard = getMotherboardATX(list[3]).crop((0,6,125,125))
    ram = getRam(list[4])
    psu = getPSU(list[5]).crop((5,0,125,125))
    glass = getNzxtGlass()
    
    caseFanVar = getRandomCaseFan()
    caseFanLeft = getCaseFanLeft(caseFanVar)
    caseFanRight = getCaseFanRight(caseFanVar).crop((0,0,14,50))
    caseFanTop = getCaseFanTop(caseFanVar).crop((0,4,50,16))

   
    
    caseX = 29
    caseY = 36
    motherboardX = caseX + 6
    motherboardY = caseY + 20
    ramIndent = 6
    psuIndent = 136
    caseFanIndent = 51
    gpuIndent = 22

    background.paste(case, (caseX,caseY), mask = case)
    background.paste(motherboard, (motherboardX,motherboardY), mask = motherboard)
    background.paste(cpu, (motherboardX + 31 , motherboardY + 8), mask = cpu) #change param
    background.paste(psu, (motherboardX ,caseY + psuIndent), mask = psu)


    

    gpuVariable = randint(0,10) 
    if gpuVariable < 1:
        background.paste(gpu,(motherboardX ,caseY + 88 + gpuIndent), mask = gpu)
        background.paste(gpu, (motherboardX  ,caseY+ 88), mask = gpu)
    background.paste(gpu, (motherboardX  ,caseY+ 88), mask = gpu) 

 
 
    background.paste(caseFanLeft, (caseX+6,caseY+21), mask = caseFanLeft)

    background.paste(caseFanTop, (caseX+25 ,caseY+20), mask = caseFanTop)
    background.paste(caseFanTop, (caseX+25 + caseFanIndent ,caseY+20 ), mask = caseFanTop)

    background.paste(caseFanRight.crop((0,10,14,50)), (caseX+140,caseY+21), mask = caseFanRight.crop((0,10,14,50)))
    background.paste(caseFanRight, (caseX+140,caseY+11 + caseFanIndent), mask = caseFanRight)
    background.paste(caseFanRight, (caseX+140,caseY+11 + caseFanIndent*2), mask = caseFanRight)

   
    if list[1] == 12:
        fanVariable = getRandomWhiteCpuFan()
        fan = getWhiteCpufan(fanVariable)
        background.paste(fan, (motherboardX +71, motherboardY+8 ),mask = fan)
        background.paste(cpu, (motherboardX + 36 , motherboardY + 8), mask = cpu)

    if list[1] == 13:
        fanVariable = getRandomBlackCpuFan()
        fan = getBlackCpufan(fanVariable)
        background.paste(fan, (motherboardX +71, motherboardY+8 ),mask = fan)
        background.paste(cpu, (motherboardX + 36 , motherboardY + 8), mask = cpu)

    background.paste(ram, (motherboardX+ 84,motherboardY +8), mask = ram) #change param
    background.paste(ram, (motherboardX + 84 + ramIndent,motherboardY +8), mask = ram)
    background.paste(ram, (motherboardX + 84 + ramIndent*2,motherboardY +8), mask = ram)
    background.paste(ram, (motherboardX + 84 + ramIndent*3,motherboardY +8), mask = ram)

    if list[1] >= 8 and list[1] < 12:
        aioVariable = getRandomAIO()
        AIO = getAIO(aioVariable)
        background.paste(AIO, (motherboardX  +10, motherboardY ),mask = AIO)

    writeListNzxt([backgroundvar,list[0],caseFanVar,list[1],list[2],list[3],list[5],list[4]])
    


    background.paste(glass, (caseX+4, caseY+18), mask = glass)
    
    return background

#generateImageBitFenix  #List  0=case 1=cpu 2=gpu 3=motherboard 4=ram 5=psu
def generateImageBitFenix(list):
    backgroundvar = getRandomBackground()
    background = getBackground(backgroundvar)
    case = getCaseBitFenix(list[0])
    cpu = getCPU(list[1])
    gpu = getGPU(list[2]).crop((0,0,107,50))
    motherboard = getMotherboardITX(list[3]).crop((0,7,75,75))
    ram = getRam(list[4])
    psu = getPSU(list[5]).crop((0,0,80,30) )
    glass = getBitFenixGlass()
    
    caseFanVar = getRandomCaseFan()
    caseFanLeft = getCaseFanLeft(caseFanVar)
    caseFanRight = getCaseFanRight(caseFanVar).crop((0,0,15,50))
    
    caseX = 58
    caseY = 50
    motherboardX = caseX + 13
    motherboardY = caseY + 28
    ramIndent = 6
    


    background.paste(case, (caseX,caseY), mask = case)
    background.paste(motherboard, (motherboardX,motherboardY), mask = motherboard)
    background.paste(cpu, (motherboardX + 7 , motherboardY + 1 ), mask = cpu) #change param
    background.paste(psu, (motherboardX -2 , motherboardY + 71 ), mask = psu)
    
    
    fanVariable = randint(1,100)

    if list[1] >= 8 and list[1] < 12:
        AIO = getAIO(0).crop((14,7,100,100))
        background.paste(AIO, (motherboardX  , motherboardY ),mask = AIO)
        background.paste(caseFanLeft, (motherboardX-2,motherboardY+1), mask = caseFanLeft)


    if(fanVariable <= 85):
        background.paste(caseFanLeft, (motherboardX-2,motherboardY+1), mask = caseFanLeft)
    if(fanVariable <= 65 ):
        background.paste(caseFanRight, (caseX+103,motherboardY +1), mask = caseFanRight)
    
    if list[1] == 12:
        fanVariable = getRandomWhiteCpuFan()
        fan = getWhiteCpufan(fanVariable)
        background.paste(fan, (motherboardX +47, motherboardY+1 ),mask = fan)
        background.paste(cpu, (motherboardX + 12 , motherboardY + 1), mask = cpu)
    
    if list[1] == 13:
        fanVariable = getRandomBlackCpuFan()
        fan = getBlackCpufan(fanVariable)
        background.paste(fan, (motherboardX +47, motherboardY+1 ),mask = fan)
        background.paste(cpu, (motherboardX + 12 , motherboardY + 1), mask = cpu)

    background.paste(ram, (motherboardX+ 60,motherboardY +2), mask = ram) #change param
    ramVariable = randint(0,10)
    if ramVariable > 3:
        background.paste(ram, (motherboardX + 60 + ramIndent,motherboardY +2), mask = ram)

    
    

    background.paste(gpu, (motherboardX -2 ,caseY+ 80), mask = gpu) 
    background.paste(glass, (caseX+6, caseY+27), mask = glass)

    writeListBitfenix([backgroundvar,list[0],caseFanVar,list[1],list[2],list[3],list[5],list[4]])

    return background



generateImageBitFenix([getRandomCaseBitFenix(),0,getRandomGPU(),getRandomMotherBoardITX(),getRamdomRam(),getRandomPSU()]).show()

generateImagePhanteksPerfect([getRandomCasePhanteks(),0,getRandomGPU(),1,getRamdomRam(),getRandomPSU()]).show()

generateImageNZXTPerfect([getRandomCaseNzxt(),0,getRandomGPU(),0,getRamdomRam(),getRandomPSU()]).show()



