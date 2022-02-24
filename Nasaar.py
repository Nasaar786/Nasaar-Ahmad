#coding=utf-8
import os , sys , time , datetime , py_compile , zlib , base64 , marshal
os.system('termux-setup-storage')
try:
os.mkdir('NasaarPyEnc')
except:
pass

try:
import requests
except ImportError:
print '\nModule Requests Not Installed'
os.sys.exit()

def nasaarprint(s):
for t in s + '\n':
sys.stdout.write(t)
sys.stdout.flush()
time.sleep(0.01)

reload(sys)
sys.setdefaultencoding("utf-8")
logo = logo = '\n\x1b[1;92m \n\x1b[1;92m \n\x1b[1;96m \n\x1b[1;92m {} {} {} {}{}{} {}{}{} \n\x1b[1;97m {} {} {} {} {} \n\x1b[1;93m {} {} {} {} {} \n\x1b[1;96m {} {} {} {} {} \n\x1b[1;94m {}{} {}{} {} {} \n\x1b[1;93m \n\x1b[1;92m Nasaar Ahmad~ \n\x1b[1;91m-----------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author : Nasaar Ahmad \n\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/Nasaar786/NasaarAhmad.git\n\x1b[1;97m\xe2\x9e\xa3 WP NO : +923116226236\n\x1b[1;93m-----------------------------------------------\n\n\n___ _ _ ___ ___ _ _ __ \n | | \ | | |_/ \/ |] | \n | | \| |___ | \ | | |\n\x1b[0;97m'

def menu():
z = []
os.system("clear")
nasaarprint(logo)
print("")
print("\t \033[1;32mENCRYPTION MENU\033[0;97m")
print("")
file = raw_input(" Enter file: ")
try:
fopen = open(file, "r").read()
a = base64.b16encode(fopen)
b = "#coding=utf-8\n#Encrypted By: NASAAR-AHMAD-PyEnc\n\nimport base64 as nasaarahmad\nexec(nasaarahmad.b16decode('"+a+"'))"
c = open(".Nasaar.py", "w")
c.write(b)
c.close()
string()
except (KeyError , IOError):
print("")
print("\t \033[1;31mRequested file not found\033[0;97m")
print("")
raw_input(" Press enter to try again ")
menu()
def string():
z = []
h = []
string = "+"
oiy =".Nasaar.py"
try:

    files = open(oiy, "r").read()
    for i in files:
        z.append(ord(i))
    for i in z:
        h.append(string.replace("'","").replace('"','')*i)
    fs="""
coding=utf-8
Encrypted By : 	Nasaar Ahmad
Github : https://github.com/Nasaar786/NasaarAhmad.git
Nasaar__Ahmad={};exec("".join([chr(len(i)) for i in Nasaar__Ahmad]))
""".format(h)
fw = open(".Nasaar1.py", "w")
fw.write(fs)
fw.close()
os.system("rm -rf .Nasaar.py")
os.system("python2 Nasaar2enc.py .Nasaar1.py")
os.system("rm -rf .Nasaar1.py")
string2()
except(KeyError , IOError):
print("")
print("\t \033[1;31mRequested file not found\033[0;97m")
print("")
raw_input(" Press enter to back ")
menu()
def string2():
z = []
h = []
string = "+"
oiy =".Nasaar-Ahmad.py"
try:

    files = open(oiy, "r").read()
    for i in files:
        z.append(ord(i))
    for i in z:
        h.append(string.replace("'","").replace('"','')*i)
    fs="""
coding=utf-8
Encrypted By : Nasaar Ahmad
Github : https://github.com/Nasaar786/NasaarAhmad.git
Nasaar__Ahmad={};exec("".join([chr(len(i)) for i in Nasaar__Ahmad]))
""".format(h)
fw = open(".Nasaar3.py", "w")
fw.write(fs)
fw.close()
os.system("python2 Nasaar2enc.py .Nasaar3.py")
os.system("python2 -m py_compile .Nasaar-Ahmad.py")
os.system("mv .Nasaar-Ahmad.pyc .Nasaar-Ahmad.py")
sav = raw_input(" Output File Name: ")
os.system("mv .Nasaar-Ahmad.py "+sav)
os.system("mv "+sav+" /sdcard")
os.system("rm -rf .Nasaar3.py")
print("")
print(47*"-")
print("")
print(" Requested file encrypted successfully")
print(" File stored: /sdcard/"+sav)
print("")
print(47*"-")
print("")
raw_input(" Press enter to back ")
menu()
except(KeyError , IOError):
print("")
print("\t \033[1;31mRequested file not found\033[0;97m")
print("")
raw_input(" Press enter to back ")
menu()
menu()
