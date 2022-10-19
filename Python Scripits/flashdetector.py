from PIL import Image, ImageGrab
import time

list = [[405, 303], [1260, 305], [975, 430], [1830 , 366]]




pix1, pix2, pix3, pix4 = [], [], [], []
global blind_status, name1, name2, name3, name4
name1, name2, name3, name4 = None, None, None, None
times = 0

blind_status = 'nope'

# write to txt for connecting to the phone
def write(var):
    print(var + "=var")
    tmp = open('text.txt', 'w')
    tmp.write(var)
    tmp.close()
    time.sleep(1)
    tmp = open('text.txt', 'r')
    print(tmp.read() + "= tmp")
    tmp.close()


def skye(pix1, pix2, pix3, pix4):
    global blind_status, name1, name2, name3, name4

    #if pix1[0] >= 45 and pix1[1] >= 94 and pix1[2] >= 75 and pix1[0] <= 70 and pix1[1] <= 100 and pix1[2] <= 95:
    if pix1[0] >= 45 and pix1[1] >= 94 and pix1[2] >= 75 and pix1[0] <= 80 and pix1[1] <= 100 and pix1[2] <= 95:
        print('name1 = skye')
        name1 = "Skye" 
    # if pix2[0] >= 44 and pix2[1] == 94 and pix2[2] >= 75:    
    if pix2[0] >= 45 and pix2[1] >= 94 and pix2[2] >= 75 and pix2[0] <= 80 and pix2[1] <= 100 and pix2[2] <= 95:
        print('name2 = skye')
        name2 = "Skye"
    if pix3[0] >= 45 and pix3[1] >= 94 and pix3[2] >= 75 and pix3[0] <= 80 and pix3[1] <= 100 and pix3[2] <= 95:
        print('name3 = skye')
        name3 = "Skye"
    if pix4[0] >= 45 and pix4[1] >= 94 and pix4[2] >= 75 and pix4[0] <= 80 and pix4[1] <= 100 and pix4[2] <= 95:
        print('name4 = skye')
        name4 = "Skye"
    if name1 and name2 == "Skye" or name1 and name3 == "Skye" or name1 and name4 == "Skye" or name2 and name3 == "Skye" or name2 and name4 == True or name3 and name4 == "Skye":
        print('Skye')
        blind_status = 'skye'
        return "Skye"

while True:
    name1 = None
    name2 = None
    name3 = None
    name4 = None


    cap = ImageGrab.grab(bbox = None) 

    #cap = Image.open('2.png')
    pix = cap.load()

    var = 1
    for lst in list:
        
        rgb = pix[lst[0],lst[1]]  # Get the RGBA Value of the a pixel of an image
        if var == 1:
            pix1 = [rgb[0], rgb[1], rgb[2]]
        elif var == 2:
            pix2 = [rgb[0], rgb[1], rgb[2]]
        elif var == 3:
            pix3 = [rgb[0], rgb[1], rgb[2]]
        elif var == 4:
            pix4 = [rgb[0], rgb[1], rgb[2]]
        var = var + 1

        
        

    if var == 5:
        if (skye(pix1, pix2, pix3, pix4) == "Skye"):
            var = var + 1
            cap.save('blinded' + str(times) + '.png')
            times = times + 1
            write(blind_status)
            print('skye if')
        else:
            var = 7
        
    ### 95 85 56 -  Skye


    if var == 6:
        print('var  6')
        
        var = 1
        pix1 = []
        pix2 = []
        pix3 = []
        pix4 = []
        blind_status = 'none'
            
            
    elif var == 7:
        blind_status = 'none'
        write(blind_status)
        print(blind_status)




