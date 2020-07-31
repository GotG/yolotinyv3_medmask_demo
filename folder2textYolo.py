import glob, os
import argparse
import random
from collections import Counter
parser = argparse.ArgumentParser()
parser.add_argument('test_pct',help="percentage of images to be used for testing, the rest are used for training",
                    type=int)
parser.add_argument('yolodataset',help="path to directory with images and yolo annotations",
                    type=str)
args = parser.parse_args()
#dataset_path = '/home/leeroy/Documents/Datasets/yolotinyv3_medmask_demo/obj'

# Percentage of images to be used for the test set



counter = 1  


testfiles=[]
trainfiles=[]
extensions = []
images=[]
#check extension of files in folder:
for filename in os.scandir(args.yolodataset):
    title,ext = os.path.splitext(filename.name)
    if ext != ".txt":
       extensions.append(ext)
       
ext_dict=Counter(extensions)
extension = max(ext_dict,key=ext_dict.get)       
print("Your image file extension is: " + extension)

for filename in os.listdir(args.yolodataset):  
    _, ext = os.path.splitext(os.path.basename(filename))
    if ext == extension:
       images.append(os.path.join(args.yolodataset,filename))

number_of_images = len(images)
   
index_test = round(number_of_images*args.test_pct/100)
testfiles = random.sample(images,index_test)
trainfiles = list(set(images).difference(set(testfiles)))

print('Number of images:',number_of_images)


with open('train.txt', mode='w') as f:
    for item in trainfiles:
        f.write(item + "\n")

with open('test.txt', mode='w') as f:
    for item in testfiles:
        f.write(item + "\n")
print('Number of images used for training',str(len(trainfiles)))
print('Number of images used for testing',str(len(testfiles)))
