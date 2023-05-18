import os
####################################################
# how use this ?
# from another file import this library 
# test.savetotxt('messi','goat.txt') # add messi in goat.txt
# test.removefromtxt('messi','goat.txt') # remove messi in goat.txt
####################################################
def savetotxt(savelineintxt,nametxtfile): # add line to text file
    with open(nametxtfile, "a") as afile:
        afile.write(savelineintxt + '\n')
        afile.close()
        return savelineintxt,nametxtfile
    
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
