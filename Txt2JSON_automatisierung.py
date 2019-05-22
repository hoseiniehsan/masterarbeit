# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:43:20 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 06
Automatisierung Convert Service.txt to JSON
"""

#%%
import argparse
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


#%%
''' Argument Parser'''
#   '--'   mean that argument define as optional Arg
parser = ArgumentParser(description="Reading service.txt-files from quellpfad and writing to zielpfad in Format JSON", formatter_class = RawTextHelpFormatter)

# groups allows to specify options that conflict with each other.
#groups = parser.add_mutually_exclusive_group()
#group.add_argument(new argument)

parser.add_argument('quellpfad', help='the complete path of the folder with the origin service.txt : as an Example -> \
                    J:\_Datatransfer\hoeh\TxT_to_JSON\\') # extra '\' am ende der code line beacause of EOL->End Of Line

parser.add_argument('-d', '--zielpfad', help='the complete path of the folder for Output converted service.txt to JSON : as an Example -> \
                    J:\_Datatransfer\hoeh\TxT_to_JSON\Output\\', type=str, default="./Output/")

# , action="store_true" -> action means that, this is True, if the options is specified
parser.add_argument('-e', "--echo", help = 'echo Author and document', action='store_true')

# verbosity -> python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ -d .\Output\ --echo -v 1
parser.add_argument('-v', "--verbosity", type=int\
                    , help="write txt filenames after compile-> between 0 to 2 \n "\
                    "0 = Dokumenteninformation fuer jedes Dokument (ausfuehrlich) \n " \
                    "1 = Dateinamen fuer jedes Dokument \n "\
                    "2 = Dateiname der Ausgabe bei erfolgreichem Abschluss", choices=[0,1,2], default=0)


    
''' End of Argument Parser'''

# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ -d J:\_Datatransfer\hoeh\TxT_to_JSON\Output\
# or
# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ -d .\Output\
# and\or
# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ -d .\Output_ -> at the Start of filenames come new name

# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ -e Ehsan
# or
# python Txt2JSON_automatisierung.py J:\_Datatransfer\hoeh\TxT_to_JSON\ --echo Ehsan

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
    except Exception as e:
        print("Zielpfad {} is not found".format(args.zielpfad))
    pass
else:
    output_path='./Output/'

if args.echo:
    print("echo is on \n")
else:
    print("echo is off \n")

if args.verbosity is None:
    print("verbosity is off")

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

class Txt2JSON(object):
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
    
    def import_txt_files(self, path = None):
        if path is None :
            path = self.path
        filenames = glob.glob(path+"/*.txt") # return an Array -> all .txt filenames in directory of relative path
        print('importing completed \n')
        return filenames
        
        
    def parse_service_txt(self, filename):
        # file_name = "Service.txt"
        #file_name = self.file_name
        file_name = filename
        file_input = open(str(file_name) , 'r') # read Service txt file as input read only mode
        text = file_input.read() # content text of input Service txt file
        '''file_out = open("string.txt", 'w') #    create new txt file to convert content of service txt'''
        content = text.splitlines(True) #   split all lines in text
        
        # write structured content to output file
        '''file_out.write(json.dumps(content, indent=4, sort_keys=True))
        # close output opened files
        file_out.close()
        file_out.closed
        '''
        
        # close input opened files
        file_input.close() #  close txt input file
        file_input.closed # check if closed return True
        context = json.dumps(content, indent=4, sort_keys=True)
        # read structured files and convert to data dict
        '''with open("string.txt", 'r') as file_input: # with open("file_name.type") as file_input -> don't need to file_input.close()'''
        data = list()
        group = dict()
        for key, value in re.findall(r'(.*):\s*([\dE+-.]+)', context):
        #for key, value in re.findall(r'(.*):\s*([\dE+-.]+)', file_input.read()):
            if key in group:
                data.append(group)
                group = dict()
            group[key] = value
        data.append(group)
        
        # close input opened files
        file_input.close() #  close txt input file
        file_input.closed # check if closed return True
        
        return group
        
    Var_convert_to_JSON={}
    def convert_to_JSON(self, group, filename):
        global Var_convert_to_JSON
        # convert data dictionary to dataframe
        df_datadict = pd.DataFrame(sorted(group.items()))
        
        for item in range(len(df_datadict)):
            item_value = df_datadict[0][item]
            item_value = re.sub(r'["+.]','',item_value) #   remove Regulare expresion all " and .
            item_value = item_value.strip() #   remove leading and trailing whitespaces
            df_datadict[0][item] = item_value
        
        # set columns names
        inventar_Nr = filename[4:20]
        data_full_names = filename[ :-4]
        df_datadict.columns = [ data_full_names, inventar_Nr]
        # set 'attribute' as index
        df_datadict = df_datadict.set_index(data_full_names)
        # save df to JSON
        self.func_write_df_to_JSON(df_datadict, data_full_names)
        #df_service_txt = pd.read_json(filename+".JSON")
        # bugfix: replace == with >=
        if args.verbosity ==1:
            print("converting to JSON for %s Erfolgreich" % filename)
    
        Var_convert_to_JSON = inspect.currentframe().f_locals
        return df_datadict
    
    def conv_obj_2_JSON(self):
        # Convert a Python object to JSON
        struct = {"Device size": "11",

            "Unit Serial number": "E11SH15032449501",
            "Software version": "SCC-07-00-08.5",
            "Startup Date and Time": "20180730214522",
            "Service Date and Time": "20181011125755",
            "Running Times":"7284h",
            "Energy type ": "E",
            
            "Diagnostic-Water-Norm-fill-calc":
            	{
            	"total": "5.50",
            	"correct": "5.49",
            	"current-status": "4,39",
            	"dim__": "litr"
                },
            "Diagnostic-Service":
                          {
                      	"Service-17":
                            	{
                             	"First-time": "20180730103458",
                                	"Quantity": "1"
                      		    },
                          },
            "Diagnostic-Running-Times-Componenets":
                          {
                            "Door-Openings-S3":
                            	{
                                	"count":"106"
                           	},
            		"Ball-Value-Opennings-S12":
                         		{
                        		"count":"172"
                         		},
            		"Clean-Jet-Pump-M6":
                         		{
                            	"count": "225",
                            	"Value": "63",
                            	"dim": "min"
                         		},   
                       	},
                }
        struct_to_text = json.dumps(struct)
        struct_to_JSON = json.dumps(struct, indent=4)   
        struct_to_JSON_sort_keys = json.dumps(struct, indent=4, sort_keys=True)
        return True
    
    # Write dataframes to JSON file which from Excel loaded
    Vars_func_write_df_to_JSON={}
    def func_write_df_to_JSON(self, df, file_name):
        global Vars_func_write_df_to_JSON
        try:
            df.to_json(output_path + file_name+'.JSON')
        except Exception as e:
            print("filename {} cannot be write in destination {}".format(file_name, output_path))
        Vars_func_write_df_to_JSON = inspect.currentframe().f_locals
        return True
#%%
def main():
    '''
    # make an object of class
    # text2json is self
    '''
    text2json = Txt2JSON(path) # make an object
    filenames = text2json.import_txt_files() # import all txt filenames
    # create dataframe
    df = pd.DataFrame()
    #df_service_txt = pd.DataFrame()
    for item in range(len(filenames)):
        print(filenames[item])
        (dir_path, filename) = os.path.split(filenames[item]) # split filename from directory path
        group = text2json.parse_service_txt(filenames[item]) # parse txt file
        df_service_txt = text2json.convert_to_JSON(group, filename) # create df from txt file
        '''
        df_service_txt = df_service_txt.transpose() # transpose df to append to Dataframe
        df = df.append(df_service_txt, sort=False) # append df to Dataframe
        
        #print(df_service_txt.head())
        
    df = df.fillna(0)
          
    text2json.func_write_df_to_JSON(df, 'converted_all_txt_to_json_format')
    '''
    #group = Txt2JSON.parse_service_txt(text2json)
    #df_service_txt = Txt2JSON.convert_to_JSON(text2json, group, filename)
    return df_service_txt
#%%
if __name__ == '__main__' :
    df = main()
    describe_1 = df.describe()
