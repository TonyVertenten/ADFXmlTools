import os
import re
from lxml import etree as ET
import sys


def searchDuplicatesInXML(xmlfile, modify=False):
    isxmlchanged = False
    parser = ET.XMLParser(remove_blank_text=True)
    print("Starting searchDuplicates", file=f)
    tree = ET.parse(xmlfile, parser=parser)
    root = tree.getroot()
    elements = {}
    isxmlchanged = searchDuplicateNodes(modify, elements, root, "Method")
    # search for duplicate SortCriteria
    print("Looking for duplicate SortCriteria", file=f)
    pos = 1
    for sortnode in root.findall(".//{http://xmlns.oracle.com/bc4j}SortCriteria"):
        print(ET.tostring(sortnode), file=f)
        if pos == 1:
            e1 = sortnode
            pos += 1
        else:
            pos += 1
            e2 = sortnode
            if (elements_equal(e1, e2)):
                print("SortCriteria are equal", file=f)
                if modify:
                    sortnode.getparent().remove(sortnode)
                    isxmlchanged = True
            else:
                print("SortCriteria are not equal", file=f)

    if isxmlchanged:
        newfilename = xmlfile + '.org'
        os.rename(xmlfile, newfilename)
        file = open(xmlfile, "wb")
        file.write(ET.tostring(tree, pretty_print=True, xml_declaration=True))
        file.close()


def searchDuplicateNodes(modify, elements, root, nodename):
    print("SearchDuplicateNodes {}".format(nodename), file=f)
    xmlchanged = False
    xpexpr = ".//{http://xmlns.oracle.com/bc4j}" + nodename
    for method in root.findall(xpexpr):
        name = method.get('Name')
        # print(name)
        if not (name in elements.keys()):
            elements[name] = 1
        else:
            val = elements[name] + 1
            elements[name] = val
    for name in elements:
        if elements[name] > 1:
            print("Name: {} .. {}".format(name, elements[name]), file=f)
            xpe = ".//{http://xmlns.oracle.com/bc4j}" + nodename + "[@Name='" + name + "']"
            ipos = 1
            methodscollection = root.findall(xpe)
            for method in methodscollection:
                print(ET.tostring(method), file=f)
                if (ipos == 1):
                    e1 = method
                    ipos += 1
                else:
                    e2 = method
                    ipos += 1
                    if (elements_equal(e1, e2)):
                        print("Elements are equal", file=f)
                        if modify:
                            method.getparent().remove(method)
                            xmlchanged = True
                    else:
                        print("Elements are not equal", file=f)
    return xmlchanged


def elements_equal(e1, e2):
    if e1.tag != e2.tag:
        return False
    if e1.text != e2.text:
        return False
    if e1.tail != e2.tail:
        return False
    if e1.attrib != e2.attrib:
        return False
    if len(e1) != len(e2):
        return False
    return all(elements_equal(c1, c2) for c1, c2 in zip(e1, e2))


# 2 options check and modify
# read folderlist in variable
# replace \ with /
# open in lxml ltree
# check for duplicate methods <Method> and <SortCriteria>
# and if found print to logging file with name xxxModuleModel.log
print(sys.argv)
n = len(sys.argv)
print("total args:",n)

upd = False

if len(sys.argv) > 1:
    x = sys.argv[1]
    print("arg is {}".format(x))
    if x in ("u", "Update"):
        upd = True
    else:
        print("Use 'u' or 'Update' if you want to update the xml")

try:
    with open("folderlist.txt", 'r') as fin:
        for line in fin:
            folder3 = re.sub(r"\\", "/", line).strip()
            print(folder3)
            if not os.path.exists(folder3):
                print("Directory: {} does not exist!".format(folder3))
                continue
            ls = folder3.split("/")
            print(ls)
            matches = [match for match in ls if "ModuleModel" in match]
            print(matches)
            logfile = matches[0] + ls[-1] + ".log"
            print(logfile)
            xmlfiles = [name for name in os.listdir(folder3) if name.endswith('.xml')]
            with open(logfile, "wt") as f:
                print("Starting logfile = " + f.name)
                for n in xmlfiles:
                    fn = folder3 + '/' + n
                    print("Processing file: " + fn, file=f)
                    searchDuplicatesInXML(fn, upd)
            f.close()
except FileExistsError:
    print("Error reading folderlist.txt")
