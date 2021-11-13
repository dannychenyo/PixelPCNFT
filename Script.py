
from Generation import *

#List 0=background 1=case 2=cpu 3=gpu 4=motherboard 5=ram 6=psu 
# getBackground(num):
# getCase(num):
# getSticker(num):
# getCPU(num)
# getGPU(num)
# getMotherboard(num)
# getRam(num)
# getPSU(num)
# getBackgroundFolderSize()
# getCaseFolderSize():
# getStickerFolderSize():
# getCPUFolderSize()
# getGPUFolderSize() 
# getMotherboardFolderSize():
# getRamFolderSize():  
# getPSUFolderSize():



#gen1
#for case in range(getCaseFolderSize()):
 #   for motherboard in range(getMotherboardFolderSize()):
    #    for gpu in range(getGPUFolderSize()):
       #    for cpu in range(getCPUFolderSize()):
            #    for ram in range(getRamFolderSize()):
               #    for psu in range(getPSUFolderSize()):
                        
                     #   generate = randint(0,2)

                    #    save(generateImageBitFenix)
                     #   save(generateImagePhanteks())
                     #   save(generateImagePhanteks([case,cpu,gpu,motherboard,ram,psu]),count)
                        
                     #   count+=1


# #Generate ALL Bitfenix
# for gpu in range(getGPUFolderSize()):
#     for cpu in range(getCPUFolderSize()):
#         for ram in range(getRamFolderSize()):
#             for psu in range(getPSUFolderSize()):
#                 save(generateImageBitFenix([getRandomCaseBitFenix(),cpu,gpu,getRandomMotherBoardITX(),getRamdomRam(),getRandomPSU()]),count)
#                 print(count)
#                 count+=1



# #generateImagePhanteks([getRandomCasePhanteks(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]).show()

# #generateImageNZXT([getRandomCaseNzxt(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardATX(),getRamdomRam(),getRandomPSU()]).show()
# for gpu in range(getGPUFolderSize()):
#     for cpu in range(getCPUFolderSize()):
#         for ram in range(getRamFolderSize()):
#             for psu in range(getPSUFolderSize()):
#                 save(generateImagePhanteks([getRandomCasePhanteks(),cpu,gpu,getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#                 print(count)
#                 count+=1

# for gpu in range(getGPUFolderSize()):
#     for cpu in range(getCPUFolderSize()):
#         for ram in range(getRamFolderSize()):
#             save(generateImageNZXT([getRandomCaseNzxt(),cpu,gpu,getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#             print(count)
#             count+=1

#Generate ALL Bitfenix



#generateImagePhanteks([getRandomCasePhanteks(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]).show()

#generateImageNZXT([getRandomCaseNzxt(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardATX(),getRamdomRam(),getRandomPSU()]).show()


# for gpu in range(getGPUFolderSize()):
#     for cpu in range(getCPUFolderSize()):
#         for ram in range(getRamFolderSize()):
#             save(generateImageNZXT([getRandomCaseNzxt(),cpu,gpu,getRandomMotherBoardMATX(),ram,getRandomPSU()]),count)
#             count+=1
#             save(generateImageBitFenix([getRandomCaseBitFenix(),cpu,gpu,getRandomMotherBoardITX(),ram,getRandomPSU()]),count)
#             count+=1
#             save(generateImagePhanteks([getRandomCasePhanteks(),cpu,gpu,getRandomMotherBoardMATX(),ram,getRandomPSU()]),count)
#             count+=1
#             print(count)



# for random in range(446):
    
#     bitfenixSeed = [getRandomCaseBitFenix(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardITX(),getRamdomRam(),getRandomPSU()]

#     for i in bitfenixList:
#         if(collections.Counter(bitfenixSeed) == collections.Counter(i)):
#             break

#     savePerfect(generateImageBitFenix(bitfenixSeed),count)
#     variable = randint(0,6)
#     count+=1
#     if(variable == 5):
#         savePerfect(generateImagePhanteksPerfect([getRandomCasePhanteks(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
#         savePerfect(generateImageNZXTPerfect([getRandomCaseNzxt(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
#     else:
#         savePerfect(generateImagePhanteks([getRandomCasePhanteks(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
#         savePerfect(generateImageNZXT([getRandomCaseNzxt(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
    
#     print(count)

# for random in range(446):
#     variable = randint(0,6)
#     save(generateImageBitFenix([getRandomCaseBitFenix(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardITX(),getRamdomRam(),getRandomPSU()]),count)
#     count+=1
#     if(variable == 5):
#         save(generateImagePhanteksPerfect([getRandomCasePhanteks(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
#         save(generateImageNZXTPerfect([getRandomCaseNzxt(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
#     else:
#         save(generateImagePhanteks([getRandomCasePhanteks(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
#         save(generateImageNZXT([getRandomCaseNzxt(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]),count)
#         count+=1
    
#     print(count)
clenseList()

bitfenixList = []
phanteksList = []
nzxtList = []

count = 1
while count <= 5000:
    bitfenixSeed = [getRandomCaseBitFenix(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardITX(),getRamdomRam(),getRandomPSU()]

    if(exists(bitfenixList,bitfenixSeed) == False):
        bitfenixList.append(bitfenixSeed)
        saveBitfenix(generateImageBitFenix(bitfenixSeed),count)
        count+=3
count = 2
while count <= 5000:
    phanteksSeed = [getRandomCasePhanteks(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardMATX(),getRamdomRam(),getRandomPSU()]

    if(exists(phanteksList,phanteksSeed) == False):
        variable = randint(0,6)
        if(variable == 0):
            phanteksList.append(phanteksSeed)
            savePhanteks(generateImagePhanteksPerfect(phanteksSeed),count)
            count+=3
        else:
            phanteksList.append(phanteksSeed)
            savePhanteks(generateImagePhanteks(phanteksSeed),count)
            count+=3
count = 3
while count <= 5000:
    nzxtSeed = [getRandomCaseNzxt(),getRandomCPU(),getRandomGPU(),getRandomMotherBoardATX(),getRamdomRam(),getRandomPSU()]

    if(exists(nzxtList,nzxtSeed) == False):
        variable = randint(0,6)
        if(variable == 2):
            nzxtList.append(nzxtSeed)
            saveNzxt(generateImageNZXTPerfect(nzxtSeed),count)
            count+=3
        else:
            nzxtList.append(nzxtSeed)
            saveNzxt(generateImageNZXT(nzxtSeed),count)
            count+=3

