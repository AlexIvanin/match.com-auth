from core.logs import Logs
import os

class Config:
    def start():
        Logs.start()
        Logs.info('Check settings')
        Config.get_proxy()
        Config.get_passwords()
        Config.get_accs()
        Config.get_good()
    def get_proxy():
        file_name = 'config/proxy.txt'
        if os.path.exists(file_name):
            file = open(file_name)
            file.read()
            Logs.info(file_name + " finded")
        else:
            Logs.error(file_name + " not created")
            file=open(file_name, "w")
            Logs.info(file_name + " Created Succesfully")
    def get_passwords():
        file_name ='config/pass.txt'
        if os.path.exists(file_name):
            file = open(file_name)
            file.read()
            Logs.info(file_name + " finded")
        else:
            Logs.error(file_name + " not created")
            file=open(file_name, "w")
            Logs.info(file_name + " Created Succesfully")
    def get_accs():
        file_name = 'config/emails.txt'
        if os.path.exists(file_name):
            file = open(file_name)
            file.read()
            Logs.info(file_name + " finded")
        else:
            Logs.error(file_name + " not created")
            file=open(file_name, "w")
            Logs.info(file_name + " Created Succesfully")
    def get_good():
        file_name = 'config/good.txt'
        if os.path.exists(file_name):
            file = open(file_name)
            file.read()
            Logs.info(file_name + " finded")
        else:
            Logs.error(file_name + " not created")
            file=open(file_name, "w")
            Logs.info(file_name + " Created Succesfully")
       
    

