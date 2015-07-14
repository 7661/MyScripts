import cmd
import os
import re
import fnmatch
import glob

import argparse
import re
import os


parser = argparse.ArgumentParser(description='The script is to run the batch script for Virtual Machine.')

parser.add_argument('vmversion', metavar='N', nargs='+',
                   help='an integer for the accumulator')

parser.add_argument('tier', metavar='P', nargs='+',
                   help='an integer for the accumulator')
				   
args = 	parser.parse_args();

print (args.vmversion);

print (args.tier);	   

#Hard coding the vm directory to save trouble
path = "C:\VMSofts";

vmVersion =args.vmversion[0];
tier = args.tier[0];
regxE="tc"+vmVersion+"_setup_"+tier+"t"+".bat";

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
            from subprocess import Popen
            program = r'path';
            p = Popen(regxE,cwd=rootPath);
            stdout, stderr = p.communicate();
            abspath = os.path.abspath(__file__);
            dname = os.path.dirname(abspath);
            os.chdir(dname);

