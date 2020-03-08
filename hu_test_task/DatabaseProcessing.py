import sqlite3
import config
from os import path

class DatabaseProcess(object):
    def __init__(self):
        self.connection = sqlite3.connect(path.abspath(config.databaseName))
        self.c = self.connection.cursor()

    def createTableFileCount(self):
        try:
            self.c.execute('CREATE TABLE %s(FilesProcessed int, FilesDeleted int, AllFiles int)' % config.tableFileCount)
            self.c.execute('INSERT INTO %s(FilesProcessed, FilesDeleted, AllFiles) VALUES (0,0,0)' % config.tableFileCount)
            self.connection.commit()
            print 'Table "%s" created.' % config.tableFileCount
        except:
            print 'Table "%s" is already created. Try to another one if it need.' % config.databaseName

    def createTableUsers(self):
        try:
            self.c.execute('CREATE TABLE %s(RegistredUsers varchar(255))' % config.tableRegistredUsers)
            self.connection.commit()
            print 'Table "%s" created.' % config.tableRegistredUsers
        except:
            print 'Table "%s" is already created. Try to another one if it need.' % config.tableRegistredUsers

    def createTableFileProcessing(self):
        try:
            self.c.execute('CREATE TABLE %s(User varchar(50), Method varchar(10), ID varchar(8), Date varchar(10))' % config.tableFileProcessing)
            self.connection.commit()
            print 'Table "%s" created.' % config.tableFileProcessing
        except:
            print 'Table "%s" is already created. Try to another one if it need.' % config.tableFileProcessing

    def isUserRegistered(self, user):
        currentusers = []
        self.c.execute('SELECT RegistredUsers from users')
        for element in self.c.fetchall():
            currentusers.append(element[0])
        return True if user in currentusers else False

    def addRegistredUsers(self, users):
        for user in users:
            if not self.isUserRegistered(user):
                self.c.execute('INSERT INTO %s(RegistredUsers) VALUES ("%s")' % (config.tableRegistredUsers, user))
                print 'User "%s" added.' % user
            else:
                    print 'User "%s" already registered.' % user
        self.connection.commit()

    def deleteRegistredUsers(self, users):
        for user in users:
            if self.isUserRegistered(user):
                self.c.execute('DELETE FROM %s WHERE RegistredUsers="%s"' % (config.tableRegistredUsers, user))
                print 'User "%s" deleted.' % user
            else:
                    print 'There is no user "%s" in database.' % user
        self.connection.commit()

    def updateFileProcessedAndAllFiles(self):
        self.c.execute('UPDATE filecount SET FilesProcessed = FilesProcessed + 1')
        self.c.execute('UPDATE filecount SET AllFiles = AllFiles + 1')
        self.connection.commit()

    def updateFileDeletedAndAllFiles(self):
        self.c.execute('UPDATE filecount SET FilesDeleted = FilesDeleted + 1')
        self.c.execute('UPDATE filecount SET AllFiles = AllFiles - 1')
        self.connection.commit()

    def updateProcessTable(self, user, method, id, process_date):
        self.c.execute('INSERT INTO %s(User, Method, ID, Date) VALUES ("%s", "%s", "%s", "%s")' % (config.tableFileProcessing,
                                                                                                   user,
                                                                                                   method,
                                                                                                   id,
                                                                                                   process_date))
        self.connection.commit()

    def cleanHistory(self, table):
        self.c.execute('DELETE FROM %s' % table)
        self.connection.commit()
        print 'Table "%s" cleaned.' % table

    def displayTable(self, tableName):
        self.c.execute('SELECT * FROM %s' % tableName)
        field_names = [i[0] for i in self.c.description]
        print field_names
        for element in self.c.fetchall():
            print element

    def connectToDatabase(self, databaseName):
        self.connection = sqlite3.connect(path.abspath(databaseName))
        self.c = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

if __name__ == '__main__':
    database = DatabaseProcess()
    database.createTableFileProcessing()
    database.createTableFileCount()
    database.createTableUsers()
    database.addRegistredUsers(['DLA', 'VAV'])
    database.displayTable(config.tableFileProcessing)
    database.displayTable(config.tableRegistredUsers)
    database.displayTable(config.tableFileCount)
    database.closeConnection()
