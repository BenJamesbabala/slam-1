

import cv2
'''
input: file=str(filename), z(float axis magnitude)
return : [[x,y,z],....] , [pixels ,.... ]

'''
#res = []
def get_data(file, z):
    res = []
    pix = []
    imagen = cv2.imread(file,0)
    #print (len(imagen[0]))
    for y in range(len(imagen)):
        for x in  range(len(imagen[0])):
            pix.append([imagen[y,x]])
            temp = (y,x,z)
            res.append(temp) 
    #print (res)
    return res, pix

#get_data("but.jpg")