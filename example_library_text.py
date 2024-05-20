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
            if SRC.check_name_exists(line):
                return False
            else:
                with open(list_users, "a") as f:
                    f.write(line + '\n')
                return True
        except:
            return False

    @staticmethod
    def remove_from_txt(line):
        try:
            if not SRC.check_name_exists(line):
                return False
            else:
                lines_to_keep = []
                with open(list_users, "r") as f:
                    lines = f.readlines()
                    for l in lines:
                        if l.strip() != line:
                            lines_to_keep.append(l)
                with open(list_users, "w") as f:
                    f.writelines(lines_to_keep)
                return True
        except:
            return False

    @staticmethod
    def check_name_exists(line): 
        try:
            return line in open(list_users, "r").read()
        except:
            return False
