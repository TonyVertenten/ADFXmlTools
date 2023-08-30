import os
import re
try:
    with open("folderlist.txt", 'r') as fin:
        for line in fin:
            folder3 = re.sub(r"\\", "/", line).strip()
            print(folder3)
            if not os.path.exists(folder3):
                print("Directory: {} does not exist!".format(folder3))
                continue
            orgfiles = [name for name in os.listdir(folder3) if name.endswith('.org')]
            for n in orgfiles:
                fn = folder3 + '/' + n
                newname = fn.replace('.org','')
                if os.path.exists(newname):
                    print("found original xml file removing modified one")
                    os.remove(newname)
                    print("Renaming file: " + fn)
                    os.rename(fn, newname)
except FileExistsError:
    print("Error reading folderlist.txt")
