import cmd
import os
import re
import fnmatch
import glob
import sys
import argparse
import re
import os

print ('VM Version:', sys.argv[1]);
print ('VM Version serial:', sys.argv[2]);
print ('TC tier:', sys.argv[3]);

#Hard coding the vm directory to save searching
path = "C:\VMSofts";

vmVersion = sys.argv[1];
serial = sys.argv[2];
tier = sys.argv[3];
regxE="tc"+vmVersion+serial+"_setup_"+tier+"t"+".bat";

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".bat") and regxE == os.path.basename(file):
            fullPath = os.path.join(root, file);
            path = '/'.join(fullPath.split('\\'))
            path = '/'.join(fullPath.split('\\'))
            rootPath = '/'.join(root.split('\\'))
            os.chdir(rootPath);
            tmp = os.popen("tasklist").read()  
            if "java.exe" in tmp:
                os.system("taskkill /im java.exe /f")
            print('Full Path of the *.bat script: ',fullPath);
            os.system(fullPath);
            # from subprocess import Popen
            # program = r'path';
            # p = Popen(regxE,cwd=rootPath);
            # stdout, stderr = p.communicate();
            # print (stdout);
            # print (stderr);
            #p.terminate();
            abspath = os.path.abspath(__file__);
            dname = os.path.dirname(abspath);
            os.chdir(dname);
            print("Script Location:", dname);
print ('NX is setup to run in Managed mode');

