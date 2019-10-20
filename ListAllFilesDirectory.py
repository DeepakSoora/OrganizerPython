import os
import re
import shutil

Unique_Main_Dict = {}

def ListAllFiles(inpath):
    # fList = []
    # for root, directories, files in os.walk(location):
    #     for filename in files:
    #         fList.append(filename)
    fList = [f for f in os.listdir(inpath) if os.path.isfile(os.path.join(inpath, f))]
    print(fList)
    return fList

def getUniqueFolderNames(fNames, loc):
    InvalidFiles = []

    for item in fNames:
        modi = item.replace("_"," ")
        numlist = [s for s in re.findall(r'\b\d+\b', modi)]
        try:
            year = numlist[0][0:4]
            Month = numlist[0][4:6]
            Day = numlist[0][6:8]
        except:
            continue
        MD = str(Month+"_"+Day)
        if year in Unique_Main_Dict.keys():
            pass
        else:
            Unique_Main_Dict[year] = {}
            Unique_Main_Dict[year]["yyyyPath"] = str(loc + '/' + year )

        if MD in Unique_Main_Dict[year].keys():
            pass
        else:
            Unique_Main_Dict[year][MD] = {}
            Unique_Main_Dict[year][MD]["filelist"] = []
            Unique_Main_Dict[year][MD]["mmddPath"] = str(loc + '/' + year +'/' + MD )

        Unique_Main_Dict[year][MD]["filelist"].append(item)
    pass

def CreateNewFolders(loc):
    for item in Unique_Main_Dict:
        try:
            os.mkdir(loc + '/' + item )
        except FileExistsError:
            print("Folder already exists at -> " + loc + "/" + item)
        for fold in Unique_Main_Dict[item]:
            try:
                os.mkdir(loc + '/' + item +'/' + fold)
            except FileExistsError:
                print("Sub Folder already exists -> " + loc + '/' + item +'/' + fold )
    pass

def moveFilesToFolders(loc):
    #shutil.move("E:/songs/images/IMG_20190817_171506.jpg","E:/songs/images/2019/08_17/IMG_20190817_171506.jpg")
    for item in Unique_Main_Dict:
        for ent in Unique_Main_Dict[item]:
            if "filelist" in Unique_Main_Dict[item][ent]:
                for key in Unique_Main_Dict[item][ent]["filelist"]:
                    FR = str(loc + '/' + key )
                    DS = str(loc + '/' + item + '/' + ent + '/' + key)
                    shutil.move(FR,DS)
            else:
                pass
    pass

if __name__ == "__main__":
    path = 'E:/songs/images'
    files_List = ListAllFiles(path)
    getUniqueFolderNames(files_List, path)
    CreateNewFolders(path)
    print(Unique_Main_Dict)
    moveFilesToFolders(path)
    