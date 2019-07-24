from rdkit import Chem


from mordred import Calculator,descriptors
print("hello")
#mols = [ mol for mol in Chem.SDMolSupplier( "cdk_cp.sdf", removeHs=False ) ]
mols=Chem.MolFromSmiles('c1ccccc1')
AtomTypeEState(type='count',estate='sLi',fill=none)
calc=Calculator(descriptors,ignore_3D=True,flator={AtomTypeEState:{"fill",0}})

print(calc(mols)[:1825])

