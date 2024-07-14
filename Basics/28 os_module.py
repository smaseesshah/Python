import os
import time

# 1) getcwd(get current working directory)
print("Directory Before Changing :",os.getcwd())

# 2) chdir(change directory to work)
print(os.chdir("Basics"))
print("Directory After Changing :",os.getcwd())

# 3) mkdir(make a directory)
if not os.path.exists("28_os_module_tutorial"): # it will only create the directory if it does not exist
    os.mkdir("28_os_module_tutorial")
for i in range(0,10):
    if not os.path.exists(f"28_os_module_tutorial/dir-{i+1}"):
        os.mkdir(f"28_os_module_tutorial/dir-{i+1}")

# 4) makedirs(make directory also intermediate directories)
os.makedirs("28_os_module_tutorial/asees/syed",exist_ok=True)#can make multiple directories and have built in function if the directory does not exist

# 5) listdir(To list all the directories of the provided directory)
print("Before rename : ",os.listdir("28_os_module_tutorial"))

# 6) rename(To rename a directory)
print("Wait 5 seconds")
for i in range(5,0,-1):
    print(i,"sec")
    time.sleep(1)
for i in range(0,10):
    os.rename(f"28_os_module_tutorial/dir-{i+1}",f"28_os_module_tutorial/re_dir-{i+1}")
print("After Rename :",os.listdir("28_os_module_tutorial"))

# 7) rmdir(To remove a directory)
print("Wait 5 seconds")
for i in range(5,0,-1):
    print(i,"sec")
    time.sleep(1)
for i in range(0,10):
    if not os.path.exists(f"28_os_module_tutorial/dir-{i+1}"):
        os.rmdir(f"28_os_module_tutorial/re_dir-{i+1}")

# 8) getsize(To get size in bytes)
print("Size of the file 28_os_module_tutorial is ",os.path.getsize("28_os_module_tutorial"),"Bytes")