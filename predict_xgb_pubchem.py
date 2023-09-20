import argparse
import pandas as pd

import joblib
import numpy as np
import pandas as pd
from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, PandasTools, Descriptors
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
import os, sys
import argparse
import configparser
import time
import re
from padelpy import from_sdf
import argparse
from padelpy import padeldescriptor
from padelpy import from_smiles

df = []

def read_smi_file(file_path):
    try:
        with open(file_path, 'r') as smi_file:
            lines = smi_file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def smi_to_dataframe(file_path):
    smi_data = read_smi_file(file_path)
    if not smi_data:
        return None
    
    data = {'SMILES': smi_data}
    df = pd.DataFrame(data)
    return df

def main():
    parser = argparse.ArgumentParser(description="Convert a .smi file to a pandas DataFrame.")
    parser.add_argument('input_file', type=str, help='Path to the .smi file')

    args = parser.parse_args()
    input_file = args.input_file

    df = smi_to_dataframe(input_file)

    if df is not None:
        print("DataFrame created successfully:")
        print(df.head())
        PandasTools.AddMoleculeColumnToFrame(df, 'SMILES')
        PandasTools.WriteSDF(df, 'pp_out.sdf')
        fp_query = from_sdf('pp_out.sdf', fingerprints=True, descriptors=False, output_csv='des-query.csv')
        df_query = pd.read_csv('des-query.csv')
        X = df_query.drop('Name', axis=1)
        filename = './asset/my_model_xgb-pubchem.joblib'
        # load the model from disk
        loaded_model = joblib.load(filename)

        y_train=pd.read_csv('./asset/tbk1_Y_train-pubchem.csv')
        X_train=pd.read_csv('./asset/tbk1_X_train-pubchem.csv')
        result = loaded_model.fit(X_train, y_train)
        y_predicted = loaded_model.predict(X)
        
        if y_predicted==1:
            print("Molecule is predicted to be Active")
        elif y_predicted==0:
            print("Molecule is predicted to be Inctive")

    else:
        print("DataFrame creation failed.")


if __name__ == "__main__":
    main()



