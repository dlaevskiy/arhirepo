import shutil
import os
import config
import uuid
import codecs
from datetime import datetime
import argparse
from sys import argv
from os import path

from DatabaseProcessing import DatabaseProcess
database = DatabaseProcess()

class FileProcess(object):
    def __init__(self):
        pass

    def createInFile(self, filenames):
        for filename in filenames:
            uniqid = str(uuid.uuid4())[:8]
            processedName = filename + '.' + uniqid + '.txt'
            whereCreateFile = (processedName, config.in_directory)
            print 'Trying to create new empty file "%s" in directory "%s"' % whereCreateFile
            path_to_file = path.join(path.abspath(config.in_directory), path.basename(processedName))
            if not os.path.isfile(path_to_file):
                open(path_to_file, 'w')
                database.updateFileProcessedAndAllFiles()
                print 'File "%s" created in directory "%s"' % whereCreateFile
            else:
                print 'File "%s" already exists in directory "%s"' % whereCreateFile
        return processedName

    def writeInfoInFile(self, fileName, *args):
        path_to_file = path.join(path.abspath(config.in_directory), path.basename(fileName))
        if os.path.isfile(path_to_file):
            for record in args:
                file = open(path_to_file, 'a')
                file.write(record + '\n')
                file.close()
            print 'New info has been added to the file: %s' % fileName
        else:
            print 'Try to add new info in file... No such file %s. You should create it first' % fileName

    def deleteFile(self, directory, fileName):
        path_to_file = path.join(path.abspath(directory), path.basename(fileName))
        if os.path.isfile(path_to_file):
            os.remove(path_to_file)
            database.updateFileDeletedAndAllFiles()
        else:
            print 'Try to delete file... No such file "%s" in directory "%s"' % (fileName, directory)

    def moveFile(self, fileName, directory1, directory2):
        path_to_file = path.join(path.abspath(directory1), path.basename(fileName))
        try:
            shutil.move(path_to_file, path.abspath(directory2))
            print 'File "%s" was moved from directory "%s" to directory "%s"' % (fileName, directory1, directory2)
        except:
            print 'Trying to move file "%s"... Nothing to move!' % fileName

    def zipFile(self, file):
        path_to_file = path.join(path.abspath(config.out_directory), path.basename(file))
        shutil.make_archive(path_to_file, 'zip',
                            path.abspath(config.out_directory), os.path.basename(file))
        self.deleteFile(config.out_directory, os.path.basename(file))
        print 'File "%s" zipped' % os.path.basename(file)

    def encodetoUTF8File(self, file):
        path_to_file = path.join(path.abspath(config.out_directory), path.basename(file))
        BLOCKSIZE = config.blocksize
        with codecs.open(path_to_file, "r", "Windows-1251") as sourceFile:
            with codecs.open(path_to_file, "w", "utf-8") as targetFile:
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)
        sourceFile.close()
        targetFile.close()
        print 'File "%s" encoded' % os.path.basename(file)

    def processInFiles(self):
        for file in os.listdir(path.abspath(config.in_directory)):
            filename = os.path.basename(file)
            splittedname = filename.split('.')
            user = splittedname[0]
            method = splittedname[1]
            id = splittedname[2]
            process_date = str(datetime.now().strftime('%Y-%m-%d'))
            if database.isUserRegistered(user):
                self.moveFile(os.path.basename(file), config.in_directory, config.out_directory)
                database.updateProcessTable(user, method, id, process_date)
                if method == 'ZIP':
                    self.zipFile(filename)
                elif method == 'ENCODE':
                    self.encodetoUTF8File(filename)
                else:
                    print "Incorrect method. Allowed types: ENCODE, ZIP. File was moved without processing"
            else:
                self.deleteFile(config.in_directory, filename)
                print 'File "%s" was deleted, because such user is not registered' % filename
        print '---All files was processed according system rules---'

def createParser():
    parser = argparse.ArgumentParser(prog='File Processing',
                                     description='This programm is using for file processing. To process file you have '
                                                 'to create them automatically or put manually in directory "%s".' % config.in_directory,
                                     epilog='(c) DLA 2016.'
                                     )
    parser.add_argument('-n', '--name', nargs='+',
                        help='Create empty files. Mask: USER.METHOD. METHOD=ZIP or ENCODE')
    parser.add_argument('-u', '--user', nargs='+',
                        help='Add registered users.')
    parser.add_argument('-du', '--delete_user', nargs='+',
                        help='Delete registered users.')
    parser.add_argument('-ms', '--main_statistics',
                        action='store_true',
                        default=False,
                        help='Show the main statistics.')
    parser.add_argument('-cs', '--counter_statistics',
                        action='store_true',
                        default=False,
                        help='Show counter statistics.')
    parser.add_argument('-ru', '--registered_users',
                        action='store_true',
                        default=False,
                        help='Show registered users')
    parser.add_argument('-ch', '--clean_history',
                        action='store_true',
                        default=False,
                        help='Clean main statistics.')
    parser.add_argument('-rp', '--run_process',
                        action='store_false',
                        default=True,
                        help='ON / OFF file processing. On default '
                             'file processing is ON. You can use False to OFF processing.')
    return parser

if __name__ == '__main__':
    file = FileProcess()
    database = DatabaseProcess()
    parser = createParser()
    namespace = parser.parse_args(argv[1:])
    database.connectToDatabase(config.databaseName)
    if namespace.name:
        file.createInFile(namespace.name)
    if namespace.user:
        database.addRegistredUsers(namespace.user)
    if namespace.delete_user:
        database.deleteRegistredUsers(namespace.delete_user)
    if namespace.main_statistics:
        database.displayTable(config.tableFileProcessing)
    if namespace.counter_statistics:
        database.displayTable(config.tableFileCount)
    if namespace.registered_users:
        database.displayTable(config.tableRegistredUsers)
    if namespace.clean_history:
        database.cleanHistory(config.tableFileProcessing)
    if namespace.run_process:
        file.processInFiles()
    database.closeConnection()

