import os
import sys
import shutil

class File(object):
    def __init__(self, filePath):
        separatedByDot = filePath.split('.')
        self.type = separatedByDot[len(separatedByDot) - 1]
        self.path = filePath

    def __str__(self):
        return 'Tipo: %s - Caminho: %s' % (self.type, self.path) 

class FilesOrganizer:

    def __init__(self, mainPath):
        self.mainPath = mainPath 
        self.__paths = [os.path.join(self.mainPath, name) for name in os.listdir(self.mainPath)]
        self.__filesPaths = [file for file in self.__paths if os.path.isfile(file)]
        self.files = list()
        self.types = list()
        self.__toFiles()
        self.__putTypesPresents()

    def __toFiles(self):
        for filePath in self.__filesPaths:
            file = File(filePath)
            self.files.append(file)

    def __putTypesPresents(self):
        for f in self.files:
            if f.type in self.types:
                continue
            else:
                self.types.append(f.type)

    def __createFolders(self):
        for t in self.types:
            pathCompleted = "%s/%s" % (self.mainPath, t)

            if not os.path.exists(pathCompleted):
                os.makedirs(pathCompleted)

    def moveFiles(self):
        try:
            self.__createFolders()

            for f in self.files:
                pathCompleted = "%s/%s" % (self.mainPath, f.type)
                shutil.move(f.path, pathCompleted)
                
            return True
            
        except:
            return False


mainPath = os.getcwd() # Path of your folder here
filesOrganizer = FilesOrganizer(mainPath)

if filesOrganizer.moveFiles():
    print('Files moved with success!')
else:
    print('Failed to move files.')



# By: Lucas Emanuel. September 2019.
# Github url: https://github.com/lucasemn1 