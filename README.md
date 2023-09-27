END to END ML model for the binary prediction of TBK-1 inhibitors using python script. 

*****

After installing the requirements in an Virtual Environment
just open the command prompt or Terminal in the above created virtual environment
run the command given below

### If you have manually generated fingerprints using Padel Software and saved as .csv file,
### You can use below script by supplying the .csv file in argument
python predict_mlp_fp_based.py testfp.csv


### If you have PadelPy installed, You can use below scripts to make prediction without generating descriptors
### Pubchem descriptors based prediction using MLP model
python predict_mlp_pubchem_based.py test.smi

### Pubchem descriptors based prediction using XGBoost model
python predict_xgb_pubchem.py test.smi


### If you have rdkit descriptors and unable to install PadelPy, 
### You can use below script without generating descriptors 
### Rdkits descriptors based prediction using MLP model
python predict_mlp_pubchem_based.py test.smi

similarly, for any unknown molecule when just use the command by specifying the path
of "*.smi" file.

python predict_name_of_algorithm.py [specify_path]*.smi


The result will be displayed in the terminal as Molecule to be active or Inactive.
The supplied test molecule namely "test.smi" in an inactive molecule.

 
