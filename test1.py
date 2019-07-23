from rdkit import Chem
from mordred import Calculator,descriptors
import numpy as np

mols = [ mol for mol in Chem.SDMolSupplier( "cdk_cp.sdf", removeHs=False ) ]

calc=Calculator(descriptors,ignore_3D=False)

#print(mol)
mol=calc.pandas(mols).astype('float').dropna(axis=1)
mol=np.array(mol,dtype=np.float32)
print(mol)

