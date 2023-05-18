Save ilne in text || remove line from txt || find line in text
<br />
how use this?
<br />
import textsaver 
<br />
<br />
nametxtfile = "goat.txt"
<br />
savelineintxt = "messi"
<br />
removeline = "messi"
<br />
findlineintxt = "cristiano"
<br />
xfind = "notfound"
<br />
textsaver.savetotxt(nametxtfile,savelineintxt)          <<<< this for add line <br />
textsaver.removefromtxt(nametxtfile,removeline)      <<<< this for remove line <br />
check = textsaver.check_name_exists(nametxtfile,findlineintxt,xfind) <<<<< this for find cristiano exist or not <br />
print(check) print ===> notfound or found
