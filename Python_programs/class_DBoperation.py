# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:49:50 2023

@author: Administrator
"""

class DBOpertion:
    def __init__(self,host,port,user,password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        
    def connectDB(self):
        ##
    def displayOutout(self):
        ##
        
        
if __name__ == "__main__":
    db1 = DBOpertion('127.0.0.1',3306,'root','Password@1')
    db1.connectDB()
    db1.displayOutput()


