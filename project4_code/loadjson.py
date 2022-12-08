import json
import os

dir_path = "C:\\Develop\\Project4\\mortgagefraud_json"

filelist = []
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        filelist.append(file_path)

textlist = []
for i, file in enumerate(filelist):
    with open (file, 'rt', encoding='UTF-8') as f:
        text = json.load(f)
        textlist.append((i, text))
        
textlist