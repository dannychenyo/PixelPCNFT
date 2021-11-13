from Script import *

background = {  
'0':    'Pink 1'  ,     
'1':    'Purple 1' ,     
'2':    'Green 1',   
'3':    'Green 2',
'4':    'Yellow 1',
'5':    'Pink 2',
'6':    'Red 1',
'7':    'Purple 2',
'8':    'Blue 1',
'9':    'Blue 2',
'10':   'Blue 3',
'11':   'Purple 3',
'12':   'Blue 4',
'13':   'Orange 1',
'14':   'Yellow 2',
'15':   'Red 2',
'16':   'Green 4',
'17':   'Yellow 3',
'18':   'Green 3',
'19':   'Solid Green',
'20':   'Sky',
'21':   'Ocean',
'22':   'Copper',
'23':   'Sea FLoor',
'24':   'Fracture',
'25':   'Ethereal' ,
'26':   'Solid Red'
}

caseItx = { 
'0':	'White ITX',
'1':	'Orange ITX',
'2':	'Green ITX',
'3':	'Blue ITX',
'4':	'Black ITX',
'5':	'Red ITX'

}

caseAtx = {
'0':	'White ATX',
'1':	'Black ATX',
'2':	'Cream ATX',
'3':	'Pink ATX',
'4':	'Red ATX'
}

caseMatx={
'0':	'Gray MATX',
'1':	'Black MATX',
'2':	'White MATX',
'3':	'Blue MATX',
'4':	'Red MATX'
}

caseFan = {
'0':	'Black-Black',
'1':	'White-Gray',
'2':	'Black-RGB',
'3':	'White-RGB',
'4':	'Gray-Gray',
'5':	'Black-Silver', 
'6':	'Bronze',
'7':	'White-RGB-Strip', 
'8':	'Black-RGB-Strip',
'9':	'Black-Red-Strip',
'10':	'White-Red-Strip',
'11':	'Blue-Blue',
'12':	'Black-Blue',
'13':	'White-Blue'
}

cpuCooler ={
'0':	'Square Black',
'1':	'Circular RGB ',
'2':	'Circular Red ',
'3':	'Circular White ',
'4':	'Circular Black ',
'5':	'Square RGB ',
'6':	'Square Gray ',
'7':	'Square Red ',
'8':	'Black Circular AIO', 
'9':	'RGB AIO ',
'10':	'White Circular AIO ',
'11':	'White AIO ',
'12':	'White Large Air ',
'13':	'Black Large Air '
}

graphicsCard = {
'0':	'Chenyo', 
'1':	'Hadron',
'2':	'Reaver', 
'3':	'MOK', 
'4':	'KSI ',
'5':	'White ',
'6':	'Slytify ',
'7':	'Phat ',
'8':	'Astro ',
'9':    'Archon',
'10':   'Rave',
'11':   'Black RGB',
'12':   'Pheonix'
}

motherboardAtx = {
'0':	'Black-Red DIX ATX',
'1':	'White DIX ATX',
'2':	'White MOK ATX',
'3':	'Striped Anus ATX',
'4':	'Strike MOK ATX'
}

motherboardItx = {
'0':	'Black-Red ITX',
'1':	'White ITX'
}

motherboardMatx = {
'0':	'Black-Red DIX MATX',
'1':	'Striped-Anus MATX',
'2':	'White DIX MATX',
'3':	'Black Assrock MATX',
'4':	'White Assrock MATX'
}
powerSupply={
'0':	'MOK' ,
'1':	'Slytify',
'2':	'Phat',
'3':	'Watts',
'4':	'Chenyo',
'5':	'Reaver',
'6':	'Banana',
'7':	'Argeebee',
'8':    'GX Pow'
}
ram={
'0':	'Red Saber',
'1':	'Black Titaniam',
'2':	'Titaniam',
'3':	'Pink-White Saber',
'4':	'RGB Saber',
'5':	'Gray Titanium',
'6':	'Frostbite',
'7':	'Blue Hyper',
'8':	'RGB Hyper',
'9':	'White Hyper',
'10':	'Red Hyper',
'11':	'Yellow Saber',
'12':	'Green Saber',
'13':	'Blue Saber'
}

phanteksFile = open("Lists\phanteksList.txt","r")
phanteksToConvert = phanteksFile.read()
phanteksFile.close()

phanteksList = phanteksToConvert.split('=')
phanteksList.pop()

phanteksComplete = []
for i in phanteksList:
    temp = i.split(',')
    phanteksComplete.append(temp)

phanteksFinal =[]
for i in phanteksComplete:
    backgroundvar = background[i[0]]
    casevar = caseMatx[i[1]]
    casefanvar = caseFan[i[2]]
    cpuvar = cpuCooler[i[3]]
    gpuvar = graphicsCard[i[4]]
    motherboardvar = motherboardMatx[i[5]]
    psuvar = powerSupply[i[6]]
    ramvar = ram[i[7]]  
    gpuCount = i[8]
    fanCount = i[9]
    ramCount = i[10]

    phanteksFinal.append([backgroundvar,casevar,casefanvar,cpuvar,gpuvar,motherboardvar,psuvar,ramvar,gpuCount,fanCount,ramCount])

phanteksFile = open("Lists\phanteksProperties.txt",'w')

count = 2
for i in phanteksFinal:
    phanteksFile.write('Pixel PC #'+str(count)+'\n')
    count+=3
    phanteksFile.write('    Background         '+ i[0]+'\n')
    phanteksFile.write('    Case               '+ i[1]+'\n')
    phanteksFile.write('    Case Fan Type      '+ i[2]+'\n')
    phanteksFile.write('    Cpu Cooler         '+ i[3]+'\n')
    phanteksFile.write('    Graphics card      '+ i[4]+'\n')
    phanteksFile.write('    Motherboard        '+ i[5]+'\n')
    phanteksFile.write('    Power Supply       '+ i[6]+'\n')
    phanteksFile.write('    Ram                '+ i[7]+'\n')
    phanteksFile.write('    # of Graphics cards'+ i[8]+'\n')
    phanteksFile.write('    # of Case fans     '+ i[9]+'\n')
    phanteksFile.write('    # of Ram sticks    '+ i[10]+'\n')

phanteksFile.close()

nzxtFile = open("Lists/nzxtList.txt","r")
nzxtToConvert = nzxtFile.read()
nzxtFile.close()

nzxtList = nzxtToConvert.split('=')
nzxtList.pop()

nzxtComplete = []
for i in nzxtList:
    temp = i.split(',')
    nzxtComplete.append(temp)

nzxtFinal =[]
for i in nzxtComplete:
    backgroundvar = background[i[0]]
    casevar = caseAtx[i[1]]
    casefanvar = caseFan[i[2]]
    cpuvar = cpuCooler[i[3]]
    gpuvar = graphicsCard[i[4]]
    motherboardvar = motherboardAtx[i[5]]
    psuvar = powerSupply[i[6]]
    ramvar = ram[i[7]]  
    gpuCount = i[8]
    fanCount = i[9]
    ramCount = i[10]
    nzxtFinal.append([backgroundvar,casevar,casefanvar,cpuvar,gpuvar,motherboardvar,psuvar,ramvar,gpuCount,fanCount,ramCount])
    

nzxtFile = open("Lists/nzxtProperties.txt",'w')

count = 3
for i in nzxtFinal:
    nzxtFile.write('Pixel PC #'+str(count)+'\n')
    count+=3
    nzxtFile.write('    Background         '+ i[0]+'\n')
    nzxtFile.write('    Case               '+ i[1]+'\n')
    nzxtFile.write('    Case Fan           '+ i[2]+'\n')
    nzxtFile.write('    Cpu Cooler         '+ i[3]+'\n')
    nzxtFile.write('    Graphics card      '+ i[4]+'\n')
    nzxtFile.write('    Motherboard        '+ i[5]+'\n')
    nzxtFile.write('    Power Supply       '+ i[6]+'\n')
    nzxtFile.write('    Ram                '+ i[7]+'\n')
    nzxtFile.write('    # of Graphics cards:'+ i[8]+'\n')
    nzxtFile.write('    # of Case fans     '+ i[9]+'\n')
    nzxtFile.write('    # of Ram sticks    '+ i[10]+'\n')

nzxtFile.close()

bitfenixFile = open("Lists/bitfenixList.txt","r")
bitfenixToConvert = bitfenixFile.read()
bitfenixFile.close()

bitfenixList = bitfenixToConvert.split('=')
bitfenixList.pop()

bitfenixComplete = []
for i in bitfenixList:
    temp = i.split(',')
    bitfenixComplete.append(temp)

bitfenixFinal =[]
for i in bitfenixComplete:
    backgroundvar = background[i[0]]
    casevar = caseItx[i[1]]
    casefanvar = caseFan[i[2]]
    cpuvar = cpuCooler[i[3]]
    gpuvar = graphicsCard[i[4]]
    motherboardvar = motherboardItx[i[5]]
    psuvar = powerSupply[i[6]]
    ramvar = ram[i[7]]  
    gpuCount = i[8]
    fanCount = i[9]
    ramCount = i[10]
    bitfenixFinal.append([backgroundvar,casevar,casefanvar,cpuvar,gpuvar,motherboardvar,psuvar,ramvar,gpuCount,fanCount,ramCount])
    
bitfenixFile = open("Lists/bitfenixProperties.txt",'w')

count = 1
for i in bitfenixFinal:
    bitfenixFile.write('Pixel PC #'+str(count)+'\n')
    count+=3
    bitfenixFile.write('    Background         '+ i[0]+'\n')
    bitfenixFile.write('    Case               '+ i[1]+'\n')
    bitfenixFile.write('    Case Fan           '+ i[2]+'\n')
    bitfenixFile.write('    Cpu Cooler         '+ i[3]+'\n')
    bitfenixFile.write('    Graphics card      '+ i[4]+'\n')
    bitfenixFile.write('    Motherboard        '+ i[5]+'\n')
    bitfenixFile.write('    Power Supply       '+ i[6]+'\n')
    bitfenixFile.write('    Ram                '+ i[7]+'\n')
    bitfenixFile.write('    # of Graphics cards'+ i[8]+'\n')
    bitfenixFile.write('    # of Case fans     '+ i[9]+'\n')
    bitfenixFile.write('    # of Ram sticks    '+ i[10]+'\n')

bitfenixFile.close()

CompleteFile = open("Lists/zComplete.txt","w")

count = 1
for i in range(5000):
        CompleteFile.write('Pixel PC #'+str(count)+'\n')
        CompleteFile.write('    Background         '+ bitfenixFinal[i][0]+'\n')
        CompleteFile.write('    Case               '+ bitfenixFinal[i][1]+'\n')
        CompleteFile.write('    Case Fan           '+ bitfenixFinal[i][2]+'\n')
        CompleteFile.write('    Cpu Cooler         '+ bitfenixFinal[i][3]+'\n')
        CompleteFile.write('    Graphics card      '+ bitfenixFinal[i][4]+'\n')
        CompleteFile.write('    Motherboard        '+ bitfenixFinal[i][5]+'\n')
        CompleteFile.write('    Power Supply       '+ bitfenixFinal[i][6]+'\n')
        CompleteFile.write('    Ram                '+ bitfenixFinal[i][7]+'\n')
        CompleteFile.write('    # of Graphics cards'+ bitfenixFinal[i][8]+'\n')
        CompleteFile.write('    # of Case fans     '+ bitfenixFinal[i][9]+'\n')
        CompleteFile.write('    # of Ram sticks    '+ bitfenixFinal[i][10]+'\n')
        count+=1
        CompleteFile.write('Pixel PC #'+str(count)+'\n')
        CompleteFile.write('    Background         '+ phanteksFinal[i][0]+'\n')
        CompleteFile.write('    Case               '+ phanteksFinal[i][1]+'\n')
        CompleteFile.write('    Case Fan           '+ phanteksFinal[i][2]+'\n')
        CompleteFile.write('    Cpu Cooler         '+ phanteksFinal[i][3]+'\n')
        CompleteFile.write('    Graphics card      '+ phanteksFinal[i][4]+'\n')
        CompleteFile.write('    Motherboard        '+ phanteksFinal[i][5]+'\n')
        CompleteFile.write('    Power Supply       '+ phanteksFinal[i][6]+'\n')
        CompleteFile.write('    Ram                '+ phanteksFinal[i][7]+'\n')
        CompleteFile.write('    # of Graphics cards'+ phanteksFinal[i][8]+'\n')
        CompleteFile.write('    # of Case fans     '+ phanteksFinal[i][9]+'\n')
        CompleteFile.write('    # of Ram sticks    '+ phanteksFinal[i][10]+'\n')
        count+=1
        CompleteFile.write('Pixel PC #'+str(count)+'\n')
        CompleteFile.write('    Background:        '+ nzxtFinal[i][0]+'\n')
        CompleteFile.write('    Case:              '+ nzxtFinal[i][1]+'\n')
        CompleteFile.write('    Case Fan:          '+ nzxtFinal[i][2]+'\n')
        CompleteFile.write('    Cpu Cooler:        '+ nzxtFinal[i][3]+'\n')
        CompleteFile.write('    Graphics card:     '+ nzxtFinal[i][4]+'\n')
        CompleteFile.write('    Motherboard:       '+ nzxtFinal[i][5]+'\n')
        CompleteFile.write('    Power Supply:      '+ nzxtFinal[i][6]+'\n')
        CompleteFile.write('    Ram:               '+ nzxtFinal[i][7]+'\n')
        CompleteFile.write('    # of Graphics cards'+ nzxtFinal[i][8]+'\n')
        CompleteFile.write('    # of Case fans     '+ nzxtFinal[i][9]+'\n')
        CompleteFile.write('    # of Ram sticks    '+ nzxtFinal[i][10]+'\n')
        count+=1