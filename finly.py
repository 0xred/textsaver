import os
list_users = 'xusers.txt'
open(list_users, 'a').close()

def SRC(action, line):
    if action == 'save':
        return save_to_txt(line)
    elif action == 'remove':
        return remove_from_txt(line)
    elif action == 'check':
        return check_name_exists(line)
    else:
        return None
###########################################
def save_to_txt(line):
    try:
        if check_name_exists(line) == 'found':
            return "found"
        else:
            with open(list_users, "a") as f:
                f.write(line + '\n')
            return line
    except:None

def remove_from_txt(line):
    try:
        if check_name_exists(line) == 'notfound':
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
    except:None

def check_name_exists(line): 
    try:
        return "found" if line in open(list_users, "r").read() else "notfound"
    except:None
