from PIL import Image
image = Image.open("gorge.png")
image2 = Image.open("secret.png")
image3 = Image.open("encoded_image.png")

def main():
    # gray_scale(image)
    # invertcolors(image)
    # mirrorTopToBottom(image)
    steganography()
    # pixelate(image)
    # frame(image)

    
def gray_scale(img):
    global get_rbg, average, tuple
    width, height = img.size
    for x in range(width) :
        for y in range(height):
            get_rbg = img.getpixel((x,y))
            average = (get_rbg[0] + get_rbg[1] + get_rbg[2])//3
            tuple = (average,average,average)
            img.putpixel((x,y) , (tuple))
    img.save("grayscale.png")

def mirrorTopToBottom(img):
    global get_rbg, tuple, new_y
    width, height = img.size
    for x in range(width):
        for y in range(height//2):
            get_rbg = img.getpixel((x,y))
            new_y = height - 1 - y
            img.putpixel((x,new_y) , (get_rbg))
    img.save("mirror.png")
             
def invertcolors(img):
    global get_rbg, inverted, tuple
    width, height = img.size
    for x in range(width) :
        for y in range(height):
            get_rbg = img.getpixel((x,y))
            inverted = (255 - get_rbg[0], 255 - get_rbg[1], 255 - get_rbg[2])
            img.putpixel((x,y) , (inverted))
    img.save("inverted.png")

def encoding(img1, img2):
    global get_rbg, get_rbg2, red, blue, green, red2, blue2, green2
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            get_rbg = img1.getpixel((x,y))
            red = (get_rbg[0])
            blue = (get_rbg[1])
            green = (get_rbg[2])
            get_rbg2 = img2.getpixel((x,y))
            red2 = (get_rbg2[0])
            blue2 = (get_rbg2[1])
            green2 = (get_rbg2[2])
            if (red2<15) and (blue2<15) and (green2<15):
                if (red%2) != 0:
                    red = red - 1
                    img1.putpixel((x,y),(red,blue,green))
            else:
                if (red%2) == 0:
                    red = red + 1
                    img1.putpixel((x,y), (red,blue,green))
    img1.save("encoded.png")
    
def decoding(img):
    global get_rbg, red, blue, green
    width, height = img.size
    for x in range(width):
        for y in range(height):
            get_rbg = img.getpixel((x,y))
            red = int(get_rbg[0])
            blue = int(get_rbg[1])
            green = int(get_rbg[2])
            if (red%2) == 0:
                get_rbg = (0,0,0)
                img.putpixel((x,y), get_rbg)
            else:
                get_rbg = (255,255,255)
                img.putpixel((x,y), get_rbg)
    img.save("decodedddd.png")

def steganography():
    encoding(image,image2)
    decoding(image3)

def pixelate(img):
    global get_rbg, red_total, blue_total, green_total, final_rbg
    width, height = img.size
    red_total = 0
    blue_total = 0
    green_total = 0
    for y in range(0,height,10):
        for x in range(0,width,10):
            ten_ten(img,x,y)
    img.save("pixel.png")

def ten_ten(img,x,y): #one 10x10 block pixelated
    global get_rbg, red_total, blue_total, green_total, final_rbg
    red_total = 0
    blue_total = 0
    green_total = 0
    for i in range(10):
        for j  in range(10):
            get_rbg = img.getpixel((i+x,j+y))
            red_total = int(red_total + get_rbg[0])
            blue_total = int(blue_total + get_rbg[1])
            green_total = int(green_total + get_rbg[2])
    final_rbg = (red_total//100, blue_total//100, green_total//100)
    for h in range(10):
        for w in range(10):    
            img.putpixel((w+x,h+y), (final_rbg))

def frame(img):
    global color, get_color, tup, red, blue, green
    width, height = img.size
    get_color = input("White or Black, or other color frame? (Black, White, other) ")
    if (get_color == "White") or (get_color == "white"):
        color = 255
        tup = (color,color,color)
    if (get_color == "other"):
        red = int(input("Enter red amount (0-255): "))
        blue = int(input("Enter blue amount (0-255): "))
        green = int(input("Enter green amount (0-255): "))
        tup = (red,blue,green) 
    else:
        color = 0
        tup = (color,color,color)
    for y1 in range(0,height,10):
        for h in range(10):
            for w in range(10):
                img.putpixel((w,h+y1), (tup))
    for y2 in range(0,height,10):
        for h in range(10):
            for w in range(10):  
                img.putpixel((-w,h+y2), (tup))
    for x1 in range(0,width,10):
        for h in range(10):
            for w in range(10):
                img.putpixel((x1+w,h), (tup))
    for x2 in range(0,width,10):
        for h in range(10):
            for w in range(10):
                img.putpixel((x2+w,-h), (tup))
    img.save("gorge_frame.png")


    

main()

