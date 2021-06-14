#!/usr/bin/env python3
import math
import numpy as np

# some constants
Avogadro= 6.02214076e23 # g/mol
kB = 1.380649e-23 #Boltzmann constant JK^−1
print(kB)
parameters = {}

class LD:
    def __init__(self, filename):
        self.input_file = filename

    def read_coords(self):
        with open(self.input_file) as f:
            self.natoms = int(f.readline())
            self.comment = f.readline()
            sym_and_coords = f.readlines()
            sym_and_coords = [line.split() for line in sym_and_coords]
            #print(sym_and_coords)
            sym_and_coords = np.array(sym_and_coords)
            self.atomtypes, self.coordinates = sym_and_coords[:,0], sym_and_coords[:, 1:].astype(np.float32)
        return self.atomtypes, self.coordinates

xyz = LD("/Users/smol/brites-tmp/WL-SAM-length/OTS8_1step.xyz")
print(len(xyz.read_coords()[0]))
