import cv2

filename = input("Enter the input image name: ")
compression = int(input("Enter the compression factor (int): "))

img = cv2.imread(filename)

cv2.imshow("oldimg", img)

sizeX, sizeY, numChannels = img.shape

def avgOfNums(nums):
    size = len(nums)
    tot = 0
    for i in nums:
        tot += int(i)
    out = tot/size
    return int(out)

def imgAvger(img, x, y, avg):
    bvals = []
    gvals = []
    rvals = []
    if(avg == 1):
        (b, g, r) = img[x-1, y]
        bvals.append(b)
        gvals.append(g)
        rvals.append(r)
        (b, g, r) = img[x+1, y]
        bvals.append(b)
        gvals.append(g)
        rvals.append(r)
    else:
        for i in range(1, avg+1):
            (b, g, r) = img[x-i, y]
            bvals.append(b)
            gvals.append(g)
            rvals.append(r)
            (b, g, r) = img[x+i, y]
            bvals.append(b)
            gvals.append(g)
            rvals.append(r)
    avb = avgOfNums(bvals)
    avg = avgOfNums(gvals)
    avr = avgOfNums(rvals)
    return (avb, avg, avr)
    

for x in range(sizeX):
  for y in range(sizeY):
    if x <= 0+compression:
        pass
    elif x >= sizeX-(compression+1):
        pass
    elif y <= 0+compression:
        pass
    elif y >= sizeY-(compression+1):
        pass
    else:
        img[x, y] = imgAvger(img, x, y, compression)

cv2.imshow("newimg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()