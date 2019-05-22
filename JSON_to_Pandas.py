# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:30:16 2019

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 07
JSON to Pandas
"""


from argparse import ArgumentParser
import numpy as np
import pandas as pd
import json
import re
import inspect
import os
from os import listdir
from os.path import isfile, join
from os import walk
import glob # split filename from path
import sys
from argparse import RawTextHelpFormatter



''' Argument Parser'''
#   '--'   mean that argument define as optional Arg
parser = ArgumentParser(description="Reading each JSON Datei from Source and writing to Destination in Format JSON (all in one)"\
                        , formatter_class = RawTextHelpFormatter)

# groups allows to specify options that conflict with each other.
#groups = parser.add_mutually_exclusive_group()

parser.add_argument('quellpfad', help='The complete path of the folder with the origin service.txt : as an Example -> \
                    J:\_Datatransfer\hoeh\TxT_to_JSON\Output\\') # extra '\' am ende der code line beacause of EOL->End Of Line

parser.add_argument('-d', '--zielpfad', help='The complete path of the folder for Output converted service.txt to JSON : as an Example -> \
                    J:\_Datatransfer\hoeh\TxT_to_JSON\Output\JSON\\  \t or \t .\JSON\\', \
                    type=str, default="./JSON/")

parser.add_argument('-f', "--filename_output", help="The Output Filename an example -> \
                    'All_JSON_in_one' ", type =str, default="All_JSON_in_one")

# , action="store_true" -> action means that, this is True, if the options is specified
parser.add_argument('-e', "--echo", help = 'echo Author and document', action='store_true')

# verbosity -> python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ -d .\Output\ --echo -v 1
parser.add_argument('-v', "--verbosity", type=int\
                    , help="write txt filenames after compile-> between 0 to 2 \n "\
                    "0 = Dokumenteninformation fuer jedes Dokument (ausfuehrlich) \n " \
                    "1 = Dateinamen fuer jedes Dokument \n "\
                    "2 = Dateiname der Ausgabe bei erfolgreichem Abschluss", choices=[0,1,2], default=0)




    
''' End of Argument Parser'''

# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\Output\ -d J:\_Datatransfer\hoeh\TxT_to_JSON\Output\JSON\
# or
# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\Output\ -d .\JSON\
# and\or
# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\Output\ -d .\JSON\new_name_ -> at the Start of filenames come new name

# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\Output -e
# or
# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\Output --echo

args = parser.parse_args()
print(args)
print(args.echo)

print(sys.argv)

if args.quellpfad is None:
    print('Define the Source path')
    pass

# Destination path is optional
if args.zielpfad:
    print('zielpfad ist %r' % args.zielpfad)
    # Destination path from Argument parser:
    try:
        output_path = args.zielpfad
    except NameError as e:
        print("Zielpfad {} is not found".format(args.zielpfad))
    pass
else:
    output_path='./JSON/'

if args.filename_output:
    filename_out = args.filename_output

if args.echo:
    print("echo is on \n")
else:
    print("echo is off \n")

if args.verbosity is None:
    print("verbosity is off")

# code Block
# to run only code Block press Ctrl+Enter, or run a cell and advance with Shift+Enter
'''
#%%
print("Press Shift+Enter to advance running the Code")
print("to run the code in Linux or Anaconda command prompt -> python J:\_Datatransfer\hoeh\TxT_to_JSON\Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ J:\_Datatransfer\hoeh\TxT_to_JSON\Output\")
#%%
'''
##
print("Idle Block")
##

#path = r'\\_Datatransfer\hoeh\TxT_to_JSON' #   relative path
#path = 'J:/_Datatransfer/hoeh/TxT_to_JSON' #   fix Path
#path = './'
path = args.quellpfad
    

# Destination path from Argument parser
#output_path = './Output/'
#output_path = args.zielpfad


if args.verbosity >=2 :
    print("Running file is '{}'".format(__file__))
elif args.verbosity == 0:
    print("Document is '{}'".format(__doc__))
    

'''
relativ_path = os.path.abspath(__file__)
rel_dir_path = os.path.dirname(relativ_path)
sys.path.append(rel_dir_path)


#os.path.join('J:\_Datatransfer\hoeh\TxT_to_JSON\\')
os.path.join('J:/_Datatransfer/hoeh/TxT_to_JSON/')
from Txt2JSON_automatisierung import Txt2JSON
# make an object of class Txt2JSON
txt2json = Txt2JSON(path)
'''



class JSON2JSON(object):
    def __init__(self, path, file_name=None):
        self.call_libraries()
        if file_name is not None:
            # use '\' to continue Code at next line
            self.file_name \
            = file_name
        self.path = path
        #self.conv_obj_2_JSON()
        #group = self.parse_service_txt()
        #self.convert_to_JSON(group)
        
    def call_libraries(self):
        import json
        # Regular expression libraries
        import re
        import glob
        import inspect
        print("libraries imported")
        return
    
    def import_json_files(self, path = None):
        if path is None :
            path = self.path
        filenames = glob.glob(path+"/*.JSON") # return an Array -> all .txt filenames in directory of relative path
        print('importing completed \n')
        return filenames
        
    
    # Write dataframes to JSON file which from Excel loaded
    Vars_func_write_df_to_JSON={}
    def func_write_df_to_JSON(self, df, file_name):
        global Vars_func_write_df_to_JSON
        try:
            df.to_json(output_path + file_name+'.JSON')
            if args.verbosity == 1:
                print("converting JSON to Pandas -> all in one for %s Erfoglreich" % file_name)
        except Exception as e:
            print("filename {} cannot be write in destination {}".format(file_name, output_path))
        Vars_func_write_df_to_JSON = inspect.currentframe().f_locals
        return True
        

    


def main():
    '''
    # make an object of class
    # json2json is self
    '''
    json2json = JSON2JSON(path) # make an object
    filenames = json2json.import_json_files() # import all txt filenames
    # create dataframe
    df = pd.DataFrame()
    #df_service_txt = pd.DataFrame()
    for item in range(len(filenames)):
        (dir_path, filename) = os.path.split(filenames[item]) # split filename from directory path
        df_service_txt = pd.read_json(path + filename) # read df from JSON file
        df_service_txt = df_service_txt.transpose() # transpose df to append to Dataframe
        df = df.append(df_service_txt, sort=False) # append df to Dataframe
        if args.verbosity ==1:
            print("converting to JSON for %s Erfolgreich" % filename)
        '''
        print(df_service_txt.head())
        '''
    df = df.fillna(0)            
    # write all JSON in One
    json2json.func_write_df_to_JSON(df, filename_out)
    return df

if __name__ == '__main__' :
    df = main()
    describe_1 = df.describe()
    
