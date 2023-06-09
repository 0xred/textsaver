import os
###################################################################################
def savetotxt(savelineintxt,nametxtfile): # add line to text file
    with open(nametxtfile, "a") as afile:
        afile.write(savelineintxt + '\n')
        afile.close()
        return savelineintxt,nametxtfile
##################################################################################
def removefromtxt(removeline,nametxtfile): # remove line from text file
    lines_to_keep = []
    with open(nametxtfile, "r") as rfile:
        xlines = rfile.readlines()
        for xline in xlines:
            if xline.strip() != removeline:
                lines_to_keep.append(xline)
    with open(nametxtfile, "w") as rfile:
        rfile.writelines(lines_to_keep)
        rfile.close()
        return removeline,nametxtfile
###################################################################################
def check_name_in_file(nametxtfile, findlineintxt): # find line if exist or not
    with open(nametxtfile, "r") as f:
        return findlineintxt in f.read()
def check_name_exists(nametxtfile,findlineintxt,xfind):
    exists = check_name_in_file(nametxtfile, findlineintxt)
    if exists:
        xfind = "found"
    else:
        xfind = "notfound"
    return xfind
