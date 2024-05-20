# user_management.py
import os

list_users = 'xusers.txt'
open(list_users, 'a').close()

class SRC:
    @staticmethod
    def save(line):
        return SRC.save_to_txt(line)

    @staticmethod
    def remove(line):
        return SRC.remove_from_txt(line)

    @staticmethod
    def check(line):
        return SRC.check_name_exists(line)
    
    ###########################################
    @staticmethod
    def save_to_txt(line):
        try:
            if SRC.check_name_exists(line) == 'found':
                return "found"
            else:
                with open(list_users, "a") as f:
                    f.write(line + '\n')
                return line
        except:
            return None

    @staticmethod
    def remove_from_txt(line):
        try:
            if SRC.check_name_exists(line) == 'notfound':
                return "notfound"
            else:
                lines_to_keep = []
                with open(list_users, "r") as f:
                    lines = f.readlines()
                    for l in lines:
                        if l.strip() != line:
                            lines_to_keep.append(l)
                with open(list_users, "w") as f:
                    f.writelines(lines_to_keep)
                return line
        except:
            return None

    @staticmethod
    def check_name_exists(line): 
        try:
            return "found" if line in open(list_users, "r").read() else "notfound"
        except:
            return None
