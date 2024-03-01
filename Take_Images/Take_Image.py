import cv2.cv2 as cv2
from re import split
from datetime import datetime
from os import mkdir,getcwd,listdir


def Image_Taker():
    U_Camera = cv2.VideoCapture(0)
    if "Image Folder" not in listdir(getcwd()):
        mkdir('Image Folder')
    Current_Path = getcwd() + "\\Image Folder"

    for u in range(100): # ten Images
        Flag, Image = U_Camera.read()
        # cv2.imshow('Image',Image)
        Time_Now = str(datetime.now())
        File_Name = Current_Path+ "\\"+ ''.join(split(r'[-:. ]', Time_Now))+'.jpg'
        cv2.imwrite(File_Name,  Image)
        cv2.waitKey(1)

    print(len(listdir(Current_Path))) # total Images

    U_Camera.release()
    cv2.destroyAllWindows()


#-----------------------------------Delete Folder Function---------
def Delete_Folder():
    import shutil
    if "Image Folder" in listdir(getcwd()):
        shutil.rmtree('Image Folder')
    else:
        print("There is no 'Image Folder'")

if __name__ == '__main__':
    Delete_Folder()
    # Image_Taker()
