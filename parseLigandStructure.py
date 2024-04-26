#!/opt/anaconda3/bin/python
#import modules
#to run do this python3 /Users/CarmenLaptop/Desktop/coding/predictingDrugBindingAffinities/parseLigandStructure.py
import sys
print("THIS IS THE PATH:::::")
#sys.path.append('/opt/anaconda3/lib/python3.11/site-packages')

import numpy as np
import pandas as pd
import pydock
from Bio.PDB import PDBParser
from Bio.PDB import Select



# A class to select only ligand atoms
class LigandSelector(Select):
    def accept_chain(self, chain):
        return chain.id == 'L'  # Adjust the chain ID if needed

# Load the AChE-ligand complex structure
parser = PDBParser()
structure = parser.get_structure('ache_donepezil', 'structures/ache_donepezil.pdb')

# Extract the ligand chains from the structure
ligand_chains = [chain for chain in structure.get_chains() if chain.id == 'A']  # Adjust the chain ID if needed

# Create separate Structure objects for each ligand chain
ligand_structures = []
for ligand_chain in ligand_chains:
    ligand_structure = parser.get_structure('DONEPEZIL', ligand_chain)
    ligand_structures.append(ligand_structure)

# Save ligand structures to PDB files
for i, ligand_structure in enumerate(ligand_structures):
    filename = f'ligand_{i+1}.pdb'
    ligand_structure.save(filename)
