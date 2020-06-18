import glob, os


dataset_path = '/content/yolotinyv3_medmask_demo/obj'

# Percentage of images to be used for the test set
percentage_test = 10;

# # Create and/or truncate train.txt and test.txt
# file_train = open('train.txt', 'w')  
# file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
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