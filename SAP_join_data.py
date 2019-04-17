# -*- coding: utf-8 -*-
"""
Created on Wed Mar 06 17:13

@author: Ehsan Hosseini
Firma: RATIONAL AG
Projekt: Masterarbeit
Arbeitspacket: 08
Task: Join SAP excel Data
"""


# supress warnings message
import warnings;

warnings.simplefilter("ignore");
warnings.filterwarnings("ignore")

import inspect
import math
import sys
import h5py # HDF5 Data format

print(sys.path)
sys.path.extend('C:\ProgramData\Anaconda3\pythonw.exe')

# Regulare expression
import re

# file name pattern matching
import glob

import os

#  calculate importing progress
import time
from datetime import datetime
from threading import Thread

import pandas as pd
import numpy as np

# replace inf values with 0
math.inf

from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

# Define default Paths
#data_path = 'J:/_Datatransfer/hoeh/'
#input_path = 'J:/_Datatransfer/hoeh/SAP_input_Data/xlsx_input_Data/'
#output_path = 'J:/_Datatransfer/hoeh/SAP_output_Data/'
#input_data_to_json_converted_path = 'J:/_Datatransfer/hoeh/SAP_input_Data/JSON_converted_from_xlsx_input_Data/'

#Run in command prompt: python C:\Users\hoeh\PycharmProjects\SAP_import_daten\pack\SAP_join_data.py J:\_Datatransfer\hoeh\SAP_input_Dat
#a\xlsx_input_Data\ -d J:\_Datatransfer\hoeh\SAP_output_Data\ -f joint_Thomas_10-05 -j J:\_Datatransfer\hoeh\SAP_input_Data\JSON_converted_from_xlsx_input
#_Data\ -e -v 1



# TODO: Argument Parser
''' Argument Parser to work with Command Prompt args '''
parser = ArgumentParser(
    description=" Import Excel Data and Join them to one Pandas Dataframe and export as JSON and xlsx format \n ",
    formatter_class=RawTextHelpFormatter)
parser.add_argument('source', help="The complete path of the input folder source with the origin SAP Tables in form of xlsx : \n \
                                    as an example -> \n \
                                    J:\\_Datatransfer\\hoeh\\SAP_input_Data\\xlsx_input_Data\\ \n ")
parser.add_argument('-d', '--destination', help="The complete path of the output folder destination to save joint SAP tables in form of xlsx and JSON \n \
                                                As an Example -> \n \
                                                Fix path : J:\\_Datatransfer\\hoeh\\SAP_output_Data\\ \n \
                                                Relative path: ../../SAP_output_Data/ \n", default='./SAP_output_Data/')
parser.add_argument('-f', "--filename_output", help="The output Joint Data filename -> \
                                                    As an Example: 'joint_Data' " \
                    , default="JOINT_SAP_Data", type=str)
parser.add_argument('-c', '--converting', help="To convert all xlsx Data to HDF5 -> '.h5' format.", action='store_true')
parser.add_argument('-hd', '--hdf5', help="If HDF5 Data files are available, read from HDF5 from destination path is possible and very faster than JSON importing!", action='store_true')
parser.add_argument('-j', '--json', help="If JSON Data files are available, raed from JSON from destination path is possible and very faster than xlsx importing !", action='store_true')
parser.add_argument('-cs', '--to_csv', help=("convering Data to '.CSV' format in destination path."), action='store_true')
parser.add_argument('-en', '--encoding', help="Encoding String values to integer from ISO codes SAP Tables ", action='store_true')
parser.add_argument('-e', '--echo', help="Echo Author and Document", action='store_true')
parser.add_argument('-v', '--verbosity', type=int, \
                    help="echo information Data during compile -> between 0 to 2 \n" \
                         "0 = Document information for each Data (details)... \n " \
                         "1 = Data-name for each file... \n " \
                         "2 = Data-name of output by succesfully complete... \n" \
                    , choices=[0, 1, 2], default=0)

args = parser.parse_args()
input_path = args.source
# Destination path is optional
if args.destination:
    try:
        output_path = args.destination
    except NameError as e:
        print("Destination folder '{}' does not found!".format(args.destination))
        pass

# Assign output filename
output_filename = args.filename_output

if args.json:
    try:
        input_data_to_json_converted_path = args.destination
        print("Read from JSON is activate, path is :{}".format(args.destination))
    except NameError as e:
        print("JSON path does not found in or path {} is empty".format(args.destination))
        pass
else:
    input_data_to_json_converted_path = output_path

if args.echo:
    print('echo is on \n')

if args.verbosity >= 2:
    print("Running file '{}' ".format(__file__))
elif args.verbosity == 0:
    print("Compiling file '{}' , \n current Document is '{}' ".format(__file__, __doc__))

print(sys.argv)

if (args.converting and args.json) or (args.converting and args.hdf5) or (args.json and args.hdf5):
    print("\n Warning!!! Halt Programm beacause of conflicting input keys parameter,  \n " \
          "converting is '{}' \n json is '{}' \n hdf5 is '{}', \n " \
          " please try again to run program and use one of them".format(args.converting, args.json, args.hdf5))
    sys.exit(1)


''' End of Argument Parser'''


# To use Argumnet Parser:
# python SAP_join_data.py J:\_Datatransfer\hoeh\SAP_input_Data\xlsx_input_Data\ -d J:\_Datatransfer\hoeh\SAP_output_Data\
# or
# python SAP_join_data.py J:\_Datatransfer\hoeh\SAP_input_Data\xlsx_input_Data\ -d ./SAP_output_Data/

# C:\ProgramData\Anaconda3>python C:\Users\hoeh\PycharmProjects\SAP_import_daten\pack\SAP_join_data.py J:\_Datatransfer\hoeh\SAP_input_
# Data\xlsx_input_Data\ -d J:\_Datatransfer\hoeh\SAP_output_Data\ -e -v 1 -hd -cs -de

# import warnings filters try Exception warnings ignoring
np.seterr(divide='ignore')

global current_year
current_year = datetime.now().year
sheet_name = list(range(2009,current_year+1)) # in range 2009 to current year

#%%
print("Idle Block")
#file_name_Punktediagramm = '2019_02_27_Punktediagramm_2009-2018_inkl._RSP.xlsx'
#file_name_Installationsdatum_customer = 'SAP_Meldungsnummer_Installationsdatum_Customer.xlsx'
#file_name_Meldung_Beginn_Ende = 'Meldungsnummer Beginn Ende.xlsx'
#file_name_kundeninfo = 'Kundeninfos v1.xlsx'
#%%

class JoinSapData(object):
    import multiprocessing as mp
    def __init__(self, path, filenames=None):
        self.call_lib()
        if filenames is not None:
            self.filenames = filenames

        assert isinstance(path, object)
        # Pycharm now know that path is type object -str
        self.path = path
        self.output_queue = self.mp.Queue()

    def call_lib(self):
        import re
        import glob
        import h5py
        print('Libraries imported')
        return

    def encoding_pack(self, df):
        # encoding Land to iso code
        try:
            df_laender_iso_code = self.laender_code()  # call func to get df iso codes from xlsx
            if df_laender_iso_code.empty is False:
                df = self.encoding_values(df=df, decode_fieldname='Land' , df_iso_code=df_laender_iso_code, iso_code_fieldname='iso_code_land')
                if args.verbosity == 1:
                    print("Encoding Land successfull***")
        except NameError as e:
            if args.verbosity==1:
                print("Sorry! Encoding Land was wrong!!!")

        # encoding Ketten to iso code
        try:
            df_ketten_iso_code = self.ketten_code() # call func to get df iso codes from xlsx
            if df_ketten_iso_code.empty is False:
                df = self.encoding_values(df=df, decode_fieldname='ketten_zeich', df_iso_code=df_ketten_iso_code, iso_code_fieldname='iso_code_ketten')
                if args.verbosity==1:
                    print("Encoding Ketten auch successfull***")
        except NameError as e:
            if args.verbosity==1:
                print("Sorry! Encoding Ketten was wrong!!! aber ist nicht schlimm mach dir darueber keine gedanken :) !!!!")

        return df

    def encoding_values(self, df, decode_fieldname, df_iso_code, iso_code_fieldname):
        #df_laender_iso_code = self.laender_code() # call func to get df iso codes from xlsx
        #TODO umformatieren Laender mit ISO code -> zwei Ansatz: 1. Join , 2. ersetzung durch Loopschleife


        df = df.reset_index(drop=True) # reset indexes to set this from 0 to end beacause of for loop
        '''# 1. Ansatz:
        for item in range(len(df)):
            df[str(decode_fieldname)][item] = [df_iso_code[str(iso_code_fieldname)][x] for x in
                                    df_iso_code[(df_iso_code[str(decode_fieldname)] == str(df[str(decode_fieldname)][item]))].index]

        df[str(decode_fieldname)] = df[str(decode_fieldname)].str.get(0) #  convert each columns value to value remove square bracket [] from values

        '''# 2. Ansatz:
        df = df.join(df_iso_code.set_index(str(decode_fieldname)), on=str(decode_fieldname), how='left', rsuffix='_iso')
        '''
        if df['AB_Land']:
            try:
                df = df.drop(columns='AB_Land') # drop Laender Abkurzung
            except NameError as e:
                print("Column name 'AB_Land' does not found to drop that ?!!!! ")
        '''
        df[str(decode_fieldname)] = df[str(iso_code_fieldname)] # Ersetzung 'Land' durch 'iso_code_land'
        df = df.drop(columns=str(iso_code_fieldname)) # drop 'iso_code_land'
        # Ende 2. Ansatz '''
        return df

    def ketten_code(self):
        ls_filenames = self.import_files() # detect filenames in input path from xlsx Data
        if ls_filenames:
            file_name_kettencode = self.pattern_recognize(ls_filenames, 'Ketten') # recognize filename from all filenames to import xlsx data
            if file_name_kettencode:
                df_ketten_code = self.load_excelFile_all_sheets(filename=input_path +'\\' +file_name_kettencode, reset_index=True) # read Ketten codes from xlsx file
                print("Importing laender code successfull***")
            else:
                print("Sorry! Importing was wrong!!!")
                return False
        else:
            return False
        df_iso_code = pd.DataFrame()
        df_iso_code['ketten_zeich'] = df_ketten_code['Kurzbeschreibung']
        df_iso_code['iso_code_ketten'] = df_ketten_code['MAT_6_7']
        # save iso_codes to xlsx:
        self.write_to_excel(df_iso_code, output_path, 'Ketten_iso_code')
        return df_iso_code

    def laender_code(self):
        ls_filenames = self.import_files()
        if ls_filenames:
            file_name_laendercode = self.pattern_recognize(ls_filenames, 'Laendercodes')  # recognize filename
            if file_name_laendercode:
                df_laender_code = self.load_excelFile_all_sheets(filename=input_path+ '\\' + file_name_laendercode, reset_index=False)
                print("Importing laender code successfull***")
            else:
                print("Sorry! Importing Laendercodes was wrong!!!")
                return False
        else:
            print("Sorry! Importing laendercodes cannot find filename!!!")
            return False
        df_iso_code = pd.DataFrame()
        df_iso_code['Land'] = df_laender_code['LANDX']
        df_iso_code['iso_code_land'] = df_laender_code['INTCN3']
        #df_iso_code['AB_Land'] = df_laender_code['INTCA']
        # save iso_codes to xlsx:
        self.write_to_excel(df_iso_code, output_path, 'Laender_iso_code')
        return df_iso_code

    def import_files(self, path=None, ext=None):
        # ext is file extension
        #progress.join()
        import os
        import glob
        if path is None:
            path = self.path
        if ext is None:
            ext = 'xlsx'
        ls_filenames = list()
        try:
            filenames = glob.glob(input_path + '*[*a-z*A-Z0-9*_]*' + '.' + ext)
            ls_filenames = list()
            for data in range(len(filenames)):
                #progress.__reduce__()
                (dir_path, filename) = os.path.split(filenames[data])
                ls_filenames.append(filename)
                if args.verbosity == 1:
                    print("Detected Excel data: \n '{}' \n in input path: \n '{}' ".format(filename, path))
        except NameError as e:
            print("Destination {} or extension {} does not found".format(path, ext))
            return False
        print("Filenames importing completed!")
        return ls_filenames

    def pattern_recognize(self, ls_filenames, pattern):
        #progress.join()
        find_string=''
        for filename in range(len(ls_filenames)):
            reg_exp = re.compile(r'(.*)'+pattern+r'(.*)')
            find_string = re.search(reg_exp, ls_filenames[filename])
            if find_string:
                return find_string.string
        if find_string is None:
            print("Pattern '{}' or filename '{}' does not found!".format(pattern, pattern))
            return False

    # load df from excel method 1 -- load is slowly
    def load_from_excel(self, data_path, filename, sheet_name):
        #progress.join()
        path_name = data_path + filename
        Excel_file = pd.ExcelFile(path_name)
        df = Excel_file.parse(sheet_name)
        return df

    #   load df from excel File(use method 2(fast load method)) with all sheets
    def load_excelFile_all_sheets(self, filename, reset_index):
        #progress.join()
        first_timer = datetime.now()
        df = pd.DataFrame()
        data = pd.ExcelFile(filename)
        for i in range(len(data.sheet_names)):
            df_temp = data.parse(sheet_name=data.sheet_names[i])
            df = df.append(df_temp)
        if (reset_index != False):
            df.reset_index(inplace=True, drop=True)

        second_timer = datetime.now()
        running_time = second_timer - first_timer
        print("read xlsx '%s' in %s time successful!, reset_index : %r" % (filename, running_time , reset_index))
        return df

    def write_to_excel(self, df, data_path, filename, sheet_name=None):
        #progress.join()
        if sheet_name is None:
            sheet_name= 'standard'

        try:
            writer = pd.ExcelWriter(data_path + filename + '.xlsx')  # file name and path
            df.to_excel(writer, sheet_name)  # writer and sheet name
            writer.save()
            print("Writing dataFrame '{}' in path '{}' with filename '{}' and sheetname '{}' successfull!".format(df, data_path, filename, sheet_name))
        except Exception as e:
            print("Sorry, writing dataFrame '{}' in path '{}' with filename '{}' and sheetname '{}' was wrong!".format(df, data_path, filename, sheet_name))
        return True

    # input data from excel to dataframes and merge all sheet names
    Vars_func_prepare_data = {}
    def func_prepare_data(self, data_path, file_name_Punktediagramm, sheet_name):
        #progress.join()
        global Vars_func_prepare_data
        df_main_data = df_temp = pd.DataFrame()  # declare und initialize multiple df in single line
        for i in sheet_name:
            df_temp = self.load_from_excel(data_path, file_name_Punktediagramm, sheet_name=str(i))
            df_main_data = df_main_data.append(df_temp)

        del df_temp  # release memory df_temp
        # reset indexes before write to JSON is necessary
        df_main_data = df_main_data.reset_index(inplace=True,
                                                drop=True)  # reset indexes after vertical join to avoid same indexes
        print("prepration successful")
        Vars_func_prepare_data = inspect.currentframe().f_locals
        return df_main_data

    # Write dataframes to JSON file which from Excel loaded
    Vars_func_write_df_to_JSON = {}
    def func_write_df_to_JSON(self, df, filename):
        #progress.join()
        global Vars_func_write_df_to_JSON
        df.to_json(filename + '.JSON')
        Vars_func_write_df_to_JSON = inspect.currentframe().f_locals
        return True

    # read dataframe from JSON file
    Vars_func_read_df_from_json = {}
    def func_read_df_from_json(self, filename):
        #progress.join()
        global Vars_func_read_df_from_json
        first_timer = datetime.now()

        df = pd.read_json(filename + '.JSON')
        second_timer = datetime.now()
        print("read JSON '%s' successful in %s time" % ( filename, second_timer - first_timer))
        Vars_func_read_df_from_json = inspect.currentframe().f_locals
        return df

    # join dataframes and drop useless fields and take new df to give appropriate df parameters for MTFF
    Vars_func_join_dfs = {}
    def func_join_dfs(self, df_1, df_2, df_3):
        #progress.join()
        global Vars_func_join_dfs

        #   df_1 = df_punktediagram
        #   df_2 = df_installationsdatum_customer
        #   df_3 = df_Meldung_Beginn_Ende

        df = pd.DataFrame()
        df['Service-Meldung'] = df_1['Service-Meldung']
        df['Equipment'] = df_1['Equipment']
        df['Src_meldung_Ursachencode'] = df_1['Servicemeldung Ursachencode']
        df['Baugruppe'] = df_1['Baugruppe']
        df['Bau_Gr_kennz'] = df_1['Unnamed: 3']
        ##df = df.groupby(['Service-Meldung', 'Equipment', 'Src_meldung_Ursachencode', 'Baugruppe', 'Bau_Gr_kennz' ]).size().reset_index(name='count')
        df['Land'] = df_1['Länderschlüssel (SMC']
        df['Germat Elektro/Gas ('] = df_1['Germat Elektro/Gas (']
        df['ketten_zeich'] = df_1['OEM-/Kettenkennzeichen']
        df['mat_Spannung'] = df_1['Germat Spannung (0MA']
        df['Anw-Status'] = df_1['Anw-Status']
        df['Invt_Nr'] = df_1['InventarNr']
        df['Fertigungsdatum'] = df_1['Fertigungsdatum']
        df['Störungsbeginn (Dat)_punkt'] = df_1['Störungsbeginn (Dat)']

        df_temp = pd.DataFrame()
        df_temp['Service-Meldung'] = df_2['Service-Meldung']
        df_temp['GewährlBeginn Datum'] = df_2['GewährlBeginn Datum']
        # df_temp['Fertigungsdatum']      =   df_2['Fertigungsdatum']
        df_temp['Störungsbeginn (Dat)'] = df_2['Störungsbeginn (Dat)']
        # join must be on same lenght
        df = df.set_index('Service-Meldung').join(df_temp.set_index('Service-Meldung'), on='Service-Meldung',
                                                  how='left', rsuffix='_')
        #   release memory
        del df_temp
        df_temp = pd.DataFrame()
        df_temp['Service-Meldung'] = df_3['Meldung']
        df_temp['Meldungsart'] = df_3['Meldungsart']
        df_temp['Meldungsdatum'] = df_3['Meldungsdatum']
        df_temp['StörBeginn'] = df_3['StörBeginn']
        df_temp['Störungsende'] = df_3['Störungsende']

        # df = df.join(df_temp, how='left', rsuffix='_M')   # richtig funktioniert - Anzahl der Datensätze = caller

        df = df.join(df_temp.set_index('Service-Meldung'), on='Service-Meldung', how='left', rsuffix='_M')
        df = df.fillna(
            0)  # remove null values after join with df_Meldungen because of records which there is not in df_Meldungen
        # df = df.join(df_temp, how='left', rsuffix='_WebID')
        # df_new = df_new.drop(columns=)

        #   release memory
        del df_temp

        #   Aggregate
        df = df.groupby(
            ['Service-Meldung', 'Equipment', 'Src_meldung_Ursachencode', 'Baugruppe', 'Bau_Gr_kennz', 'Land',
             'Germat Elektro/Gas (', 'ketten_zeich', 'mat_Spannung', 'Anw-Status', 'Invt_Nr', 'Fertigungsdatum',
             'GewährlBeginn Datum', 'Störungsbeginn (Dat)_punkt', 'Störungsbeginn (Dat)', 'Meldungsart',
             'Meldungsdatum', 'StörBeginn', 'Störungsende']).size().reset_index(name='count')

        #   df manipulation -> ganze df Records wo nan Values gibt auf null umschreiben
        # df [ pd.isna(df['StörBeginn']) ] = 0

        Vars_func_join_dfs = inspect.currentframe().f_locals
        return df

    # join a df to anderen df with selected columns
    Var_func_join_to_df = {}
    def func_join_to_df(self, *dfs, **fields):
        #progress.join()
        global Var_func_join_to_df

        #   fields = { 'f3':'Kettenkunde', 'f4':'Unnamed: 6', 'f5':'Kunde', 'f6':'Unnamed: 8' , 'f7':'RSP-Nummer'} #    df_kundeninfo columns

        df_caller = dfs[0]  # df_joint 3 dfs
        df_other = dfs[1]  # df_kundeninfo

        df_caller = df_caller.drop(columns='count')  # remove last column 'count' exsitence in df_caller

        df_temp = pd.DataFrame()
        df_temp['Service-Meldung'] = df_other['Meldung']
        df_temp['Equipment'] = df_other['Equipment']
        df_temp['ketten_zeich'] = df_other['Unnamed: 6']
        df_temp['InvtNr'] = df_other['InventarNr']

        # manipulate field value  'Walmart' -> 'Walmalrt (WA)'
        df_temp.ketten_zeich[df_temp['ketten_zeich'] == 'Walmart'] = str('Walmalrt (WA)')

        #   join df_temp to df_caller
        df = df_caller.join(df_temp.set_index('Service-Meldung'), on='Service-Meldung', how='left',
                            rsuffix='_K')  # join df_caller and df_temp
        df = df.fillna(0)  # remove NaN values

        ls_other_fields = list()  # field(columns) names of df_kundeninfo
        for value in sorted(fields):
            ls_other_fields.append(fields[value])

        df_other = df_other.iloc[:,
                   :10]  # remove last 4 columns of df_kundeninfo or take only first 10 columns with rows
        df_other = df_other.rename(index=str,
                                   columns={"Meldung": "Service-Meldung"})  # rename column name of df_kundeninfo

        df = df_caller.join(df_other.set_index('Service-Meldung'), on='Service-Meldung', how='left',
                            rsuffix='_K')  # join df_caller and df_kundeninfo
        df = df.fillna(0)  # remove NaN values

        ls_caller_columns = list()  # take columns name of df_caller
        for item in df_caller.columns:
            ls_caller_columns.append(item)

        for item in ls_other_fields:  # append some df_kundeninfo columns to df_caller columns
            ls_caller_columns.append(item)

        # df = df.drop(columns='count') # remove last column 'count' exsitence in df_caller
        df = df.groupby(ls_caller_columns).size().reset_index(name='count')

        #  release memory
        del df_temp
        #del df_other
        #del df_caller

        # decoding Land and Ketten values to integer
        if args.encoding:
            try:
                df = self.encoding_pack(df=df)
                print("***Encoding successfull***")
            except Exception as e:
                print("Sorry!!! Encoding was wrong!!!")

        Var_func_join_to_df = inspect.currentframe().f_locals
        return df

    # manipulate df such as falsch values
    Vars_func_maintain_df = {}
    def func_maintain_df(self, df_1, df_2):
        #progress.join()
        global Vars_func_maintain_df

        df_Meldung_Beginn_Ende = df_1.copy(deep=True)
        df_Meldung_Beginn_Ende_json = df_2.copy(deep=True)

        #   df datetime format ändern
        df_Meldung_Beginn_Ende['Meldungsdatum'] = [datetime.strftime(x, "%d.%m.%Y") if not pd.isnull(x) else '' for x in
                                                   df_Meldung_Beginn_Ende['Meldungsdatum']]
        df_Meldung_Beginn_Ende['StörBeginn'] = [datetime.strftime(x, "%d.%m.%Y") if not pd.isnull(x) else '' for x in
                                                df_Meldung_Beginn_Ende['StörBeginn']]
        df_Meldung_Beginn_Ende['Störungsende'] = [datetime.strftime(x, "%d.%m.%Y") if not pd.isnull(x) else '' for x in
                                                  df_Meldung_Beginn_Ende['Störungsende']]

        df_Meldung_Beginn_Ende_json['Meldungsdatum'] = df_Meldung_Beginn_Ende['Meldungsdatum']
        df_Meldung_Beginn_Ende_json['StörBeginn'] = df_Meldung_Beginn_Ende['StörBeginn']
        df_Meldung_Beginn_Ende_json['Störungsende'] = df_Meldung_Beginn_Ende['Störungsende']

        df_Meldung_Beginn_Ende[(df_Meldung_Beginn_Ende['Meldung'] == 373257)]  # show Meldung Nr Records

        Vars_func_maintain_df = inspect.currentframe().f_locals
        return df_Meldung_Beginn_Ende, df_Meldung_Beginn_Ende_json

    def write_df_to_HDF5(self, df, filename ,output_path=None, mode=None):
        first_timer = datetime.now()
        if mode is None:
            mode='w'
        if output_path is None:
            output_path = args.destination
        try:
            df.to_hdf(output_path +'HDF5_'+ str(filename) + '.h5', key='hdf5_' + str(filename),
                      mode=mode)  # write dataframe to HDF5 format with '.h5' Extenssion
            second_timer = datetime.now()
            running_time = second_timer - first_timer
            print("Convert dataframe '{}' to HDF5 as filename '{}.h5' Format \n in path '{}' with '{}' time succesfull completed!".format(df, filename, output_path, running_time))
            return True
        except NameError as e:
            print("Sorry! converting dataframe '{}' to HDF5 as filename '{}.h5' Format \n in path '{}' was wrong! Check output path and dataframe".format(df, filename, output_path))
            return False

    def load_HDF5(self, filename, input_path=None, mode=None):
        first_timer = datetime.now()
        if mode is None:
            mode = 'r'
        if input_path is None:
            input_path = args.destination
        try:
            hdf5 = h5py.File(str(input_path) + 'HDF5_'+str(filename)+'.h5', mode=mode)
            second_timer = datetime.now()
            running_time = second_timer - first_timer
            print("Reading HDF5 as filename 'HDF5_{}.h5' format \n in path '{}' with '{}' time succesfull completed!".format(
                    filename, input_path, running_time))
            return hdf5
        except NameError as e:
            print(
                "Sorry! read HDF5 as filename 'HDF5_{}.h5' format \n in path '{}' was wrong! Check input path and HDF5 existence".format(
                    filename, output_path))
            return False

    def read_HDF(self, filename, input_path=None, key=None , mode=None):
        first_timer = datetime.now()
        if mode is None:
            mode = 'r'
        if input_path is None:
            input_path = args.destination
        try:
            hdf = pd.read_hdf(str(input_path)+ '\\' + 'HDF5_' + str(filename) + '.h5', key=key, mode=mode)
            second_timer = datetime.now()
            running_time = second_timer - first_timer
            print(
                "Reading HDF as filename 'HDF5_{}.h5' format \n in path '{}' with '{}' time succesfull completed!".format(
                    filename, input_path, running_time))
            return hdf
        except NameError as e:
            print(
                "Sorry! read HDF5 as filename 'HDF5_{}.h5' format \n in path '{}' was wrong! Check input path and HDF5 existence".format(
                    filename, input_path))
            return False

    def release_memory(self, hdf):
        try:
            os.remove(hdf)
            return True
        except NameError as e:
            return False

    def multi_proc(self, queue, func, **param):
        # e.g. -> param = {'f1': 'Kettenkunde', 'f2': 'Unnamed: 6', 'f3': 'Kunde', 'f4': 'Unnamed: 8', 'f5': 'RSP-Nummer'}
        try:
            from setuptools import setup
            from setuptools import Extension
        except ImportError:
            from distutils.core import setup
            from distutils.extension import Extension


        pool = self.mp.Pool(processes=4)
        processes = [self.mp.Process(target=func, args=(param, queue)) for parameter in param]

        queue.put(self.output)

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        results = [queue.get() for p in processes]

        return processes

    def run_processes(self, processes):
        for p in processes:
            p.start()

        for p in processes:
            p.join()






class WorkerThread(Thread):
    def __init__(self, value=0):
        super(WorkerThread, self).__init__()

        self.value = value

    def run(self):
        while self.value < 2000:
            self.value += 1
            time.sleep(0.01)  # milli seconds


class ProgressThread(Thread):
    def __init__(self, worker):
        super(ProgressThread, self).__init__()

        self.worker = worker

    def run(self):
        while True:
            if not self.worker.is_alive():
                print("****************** Join Data is completed! *******************")
                return True

            print("Join Data is running still {}% ".format(self.worker.value * 100 / 2000))
            time.sleep(1.0)  # one milli second waiting delay
            # TODO: run a task of Class




if __name__ == '__main__':
    worker = WorkerThread()
    progress = ProgressThread(worker)

    # start workers and progress
    worker.start()
    progress.start()

    join_SAP_data = JoinSapData(input_path)
    ls_filenames = join_SAP_data.import_files()

    #input_data_to_json_converted_path = 'J:/_Datatransfer/hoeh/SAP_input_Data/JSON_converted_from_xlsx_input_Data/' # default path
    # Fast mode importing Data from JSON Format
    file_name_Punktediagramm = join_SAP_data.pattern_recognize(ls_filenames, 'Punktediagramm')  # recognize filename
    if file_name_Punktediagramm:
        if args.hdf5:
            hdf_punktediagram = join_SAP_data.read_HDF(filename=file_name_Punktediagramm)
        elif args.json:
            df_punktediagram_json = join_SAP_data.func_read_df_from_json(input_data_to_json_converted_path + file_name_Punktediagramm )  # read dataframes 'Punktediagramm' from JSON files
        else:
            df_punktediagram = join_SAP_data.load_excelFile_all_sheets(input_path + file_name_Punktediagramm,
                                                                   reset_index=True)  # read from excel method_2
            join_SAP_data.func_write_df_to_JSON(df_punktediagram,
                                            output_path + file_name_Punktediagramm)  # Write dataframes to JSON



    file_name_Installationsdatum_customer = join_SAP_data.pattern_recognize(ls_filenames,
                                                                            'Installationsdatum')  # recognize filename
    if file_name_Installationsdatum_customer :
        if args.hdf5:
            hdf_Installationsdatum = join_SAP_data.read_HDF(filename=file_name_Installationsdatum_customer)
        elif args.json:
            df_installationsdatum_customer_json = join_SAP_data.func_read_df_from_json(
                input_data_to_json_converted_path + file_name_Installationsdatum_customer )  # read dataframes 'Installationsdatum' from JSON files
        else:
            df_installationsdatum_customer = join_SAP_data.load_excelFile_all_sheets(input_path +file_name_Installationsdatum_customer,
                                                               reset_index=True)  # read from excel method_2
            join_SAP_data.func_write_df_to_JSON(df_installationsdatum_customer,
                          output_path + file_name_Installationsdatum_customer)  # Write dataframes to JSON

    file_name_Meldung_Beginn_Ende = join_SAP_data.pattern_recognize(ls_filenames, 'Beginn Ende')  # recognize filename
    if file_name_Meldung_Beginn_Ende :
        if args.hdf5:
            hdf_Meldung_Beginn_Ende = join_SAP_data.read_HDF(file_name_Meldung_Beginn_Ende)
        else:
            df_Meldung_Beginn_Ende = join_SAP_data.load_excelFile_all_sheets(input_path + file_name_Meldung_Beginn_Ende,
                                                       reset_index=True)  # read from excel method_2
            join_SAP_data.func_write_df_to_JSON(df_Meldung_Beginn_Ende, output_path + file_name_Meldung_Beginn_Ende)  # Write dataframes to JSON
            #   read dataframes 'Beginn Ende' from JSON files
            df_Meldung_Beginn_Ende_json = join_SAP_data.func_read_df_from_json(output_path +
                                                                               file_name_Meldung_Beginn_Ende)  # Equipment ab sheet 2011 während der laden von Excel Datei hat sich geändert und in JSON Datei auch die Datum


    file_name_kundeninfo = join_SAP_data.pattern_recognize(ls_filenames, 'Kundeninfos')  # recognize filename
    if file_name_kundeninfo :
        if args.hdf5:
            hdf_kundeninfos = join_SAP_data.read_HDF(filename=file_name_kundeninfo)
        elif args.json:
            df_kundeninfo_json = join_SAP_data.func_read_df_from_json(
                input_data_to_json_converted_path + file_name_kundeninfo )  # read dataframes from JSON files
        else:
            df_kundeninfo = join_SAP_data.load_excelFile_all_sheets(input_path + file_name_kundeninfo, reset_index=True)
            join_SAP_data.func_write_df_to_JSON(df_kundeninfo, output_path + file_name_kundeninfo)


    if args.hdf5 is False:
        #       manipulate df such as falsche values
        #       df_Meldung_Beginn_Ende_json Dates correction and gleich convert to standard format "%d.%m.%Y"
        df_Meldung_Beginn_Ende, df_Meldung_Beginn_Ende_json = join_SAP_data.func_maintain_df(df_Meldung_Beginn_Ende,
                                                                           df_Meldung_Beginn_Ende_json)

        #   write df_Meldung_Beginn_Ende to JSON after write corrected Values
        join_SAP_data.func_write_df_to_JSON(df_Meldung_Beginn_Ende_json, input_data_to_json_converted_path + file_name_Meldung_Beginn_Ende)

    if args.json is False and args.hdf5 is False:
        df_installationsdatum_customer_json = df_installationsdatum_customer
        df_punktediagram_json = df_punktediagram
        df_kundeninfo_json = df_kundeninfo
        df_Meldung_Beginn_Ende_json = df_Meldung_Beginn_Ende

    # Define output filename after Join all Datas
    file_name_joint_df = output_filename


    fields = {'f3': 'Kettenkunde', 'f4': 'Unnamed: 6', 'f5': 'Kunde', 'f6': 'Unnamed: 8',
              'f7': 'RSP-Nummer'}  # df_kundeninfo columns
    if args.hdf5:
        #   call func_join_dfs to create main df
        hdf = join_SAP_data.func_join_dfs(hdf_punktediagram, hdf_Installationsdatum,
                                         hdf_Meldung_Beginn_Ende)
        #   join df_kundeninfo to df
        hdf = join_SAP_data.func_join_to_df(*[hdf, hdf_kundeninfos], **fields)



        # save hdf5 as .csv:
        if args.to_csv:
            hdf.to_csv(output_path + file_name_joint_df + '.csv')
            print("Saved filename '{}.csv' in path '{}' as CSV format complete successfully!".format(file_name_joint_df,
                                                                                                     output_path))
    elif args.json:
        #   call func_join_dfs to create main df
        df = join_SAP_data.func_join_dfs(df_punktediagram_json, df_installationsdatum_customer_json, df_Meldung_Beginn_Ende_json)

        #   join df_kundeninfo to df
        df = join_SAP_data.func_join_to_df(*[df, df_kundeninfo_json], **fields)

        # save df as .csv:
        if args.to_csv:

            df.to_csv(output_path + file_name_joint_df + '.csv')
            print("Saved filename '{}.csv' in path '{}' as CSV format complete successfully!".format(file_name_joint_df,
                                                                                                     output_path))
    else:
        #   call func_join_dfs to create main df
        df = join_SAP_data.func_join_dfs(df_punktediagram, df_installationsdatum_customer, df_Meldung_Beginn_Ende)

        #   join df_kundeninfo to df
        df = join_SAP_data.func_join_to_df(*[df, df_kundeninfo], **fields)

        # save df as .csv:
        if args.to_csv:

            df.to_csv(output_path + file_name_joint_df + '.csv')
            print("Saved filename '{}.csv' in path '{}' as CSV format complete successfully!".format(file_name_joint_df,
                                                                                                     output_path))

    #   write df result of join of 3 df to excel and to json or hdf5
    if args.hdf5:

        join_SAP_data.write_df_to_HDF5(df = hdf, filename= file_name_joint_df)
    else:

        join_SAP_data.write_to_excel(df, output_path , file_name_joint_df, sheet_name='2009-' + str(current_year)) # output_path + '\\'
        join_SAP_data.func_write_df_to_JSON(df, output_path + file_name_joint_df)


    if args.converting:
        # Converting xlsx to HDF5:
        join_SAP_data.write_df_to_HDF5(df_punktediagram, file_name_Punktediagramm, output_path,  mode='w')
        join_SAP_data.write_df_to_HDF5(df_installationsdatum_customer, file_name_Installationsdatum_customer, output_path, mode='w')
        join_SAP_data.write_df_to_HDF5(df_Meldung_Beginn_Ende, file_name_Meldung_Beginn_Ende, output_path,  mode='w')
        join_SAP_data.write_df_to_HDF5(df_kundeninfo, file_name_kundeninfo, output_path,  mode='w')


    print("second timer", datetime.now())  # second timer

    # 06.12.2018 haupt df ist hier
    #df = join_SAP_data.func_read_df_from_json(output_path + file_name_joint_df)

    #release memory :
    #hdf_punktediagram.close()
    #hdf_Installationsdatum.close()
    #hdf_Meldung_Beginn_Ende.close()
    #hdf_kundeninfos.close()
    #hdf.close()




