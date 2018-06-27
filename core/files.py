from core.logs import Logs
import sys
class Files:
    def get_file(file_name,check):
        file = open(file_name)
        list = []
        for line in open(file_name): 
            list.append(line.strip())
        if (check):
            if (len(list) < 1):
                Logs.error(file_name + " empty")
                sys.exit()
            else:
                return list
       
        