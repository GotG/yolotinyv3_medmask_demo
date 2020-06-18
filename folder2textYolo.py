import glob, os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('test_pct',help="percentage of images to be used for testing, the rest are used for training",
                    type=int)
args = parser.parse_args()
dataset_path = 'obj'

number_of_images=len([name for name in os.listdir(dataset_path)])/2
# Percentage of images to be used for the test set
print('Number of images:',number_of_images)


counter = 1  
index_test = round(number_of_images*args.test_pct/100)  

testfiles=[]
trainfiles=[]
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))


    if counter <= index_test:
        # counter = 1
        testfiles.append("data/obj/"+ title + '.jpg')
        counter += 1
    else:
        # file_train.write("data/obj/" + "/" + title + '.jpg' + "\n")
        trainfiles.append("data/obj/"+ title + '.jpg')
        # counter = counter + 1

with open('train.txt', mode='w') as f:
    for item in trainfiles:
        f.write(item + "\n")

with open('test.txt', mode='w') as f:
    for item in testfiles:
        f.write(item + "\n")
print('Number of images used for training',str(len(trainfiles)))
print('Number of images used for testing',str(len(testfiles)))