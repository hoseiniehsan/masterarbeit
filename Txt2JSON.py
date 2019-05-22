# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:43:20 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 03
Convert Service.txt to JSON
"""

import numpy as np
import pandas as pd
import json
import re
import inspect

class Txt2JSON(object):
    def __init__(self, file_name):
        self.call_libraries
        self.file_name = file_name
        self.conv_obj_2_JSON()
        group = self.parse_service_txt()
        self.convert_to_JSON(group)
        
    def call_libraries():
        import json
        # Regular expression libraries
        import re
        
        import inspect
        
    def parse_service_txt(self):
        # file_name = "Service.txt"
        file_name = self.file_name
        file_input = open(str(file_name) , 'r') # read Service txt file as input read only mode
        text = file_input.read() # content text of input Service txt file
        file_out = open("string.txt", 'w') #    create new txt file to convert convent of service txt
        content = text.splitlines(True) #   split all lines in text
        
        # write structured content to output file
        file_out.write(json.dumps(content, indent=4, sort_keys=True))
        
        # close input and output opened files
        file_out.close()
        file_out.closed
        file_input.close() #  close txt input file
        file_input.closed # check if closed return True
        
        # read structured files and convert to data dict
        with open("string.txt", 'r') as file_input:
            data = list()
            group = dict()
            #for key, value in re.findall(r'(.*):\s*([\dE+-.]+)', file_input.read()):
            for key, value in re.findall(r'(.*):\s*([\dE+-.]+)', file_input.read()):
                if key in group:
                    data.append(group)
                    group = dict()
                group[key] = value
            data.append(group)
        
        # close input and output opened files
        file_out.close()
        file_out.closed
        file_input.close() #  close txt input file
        file_input.closed # check if closed return True
        
        
        return group
        
        
    def convert_to_JSON(self, group):
        # convert data dictionary to dataframe
        df_datadict = pd.DataFrame(sorted(group.items()))
        
        for item in range(len(df_datadict)):
            item_value = df_datadict[0][item]
            item_value = re.sub(r'["+.]','',item_value) #   remove Regulare expresion all " and .
            item_value = item_value.strip() #   remove leading and trailing whitespaces
            df_datadict[0][item] = item_value
        
        # save df to JSON
        self.func_write_df_to_JSON(df_datadict, "df_datadict")
        df_service_txt = pd.read_json("df_datadict.JSON")
        print("importieren Erfolgreich")
        return df_service_txt
    
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
        df.to_json(file_name+'.JSON')
        Vars_func_write_df_to_JSON = inspect.currentframe().f_locals
        return True

text2json = Txt2JSON("Service.txt")
group = Txt2JSON.parse_service_txt(text2json)
df_service_txt = Txt2JSON.convert_to_JSON(text2json, group)