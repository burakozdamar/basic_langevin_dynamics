#!/usr/bin/env python3
import os
import math
import numpy as np

# some constants
Avogadro = 6.02214076e23 # g/mol
kB = 1.380649e-23 #Boltzmann constant JK^−1

#simulation box
BOXDIM = np.ones(3)*1e-10 #Angstrom
MASS = {'H': 1.00794,'C':12.0107,'O':15.9994,'Si':28.0855,'Cl':35.4527,'K':39.0983,'Al':26.981539}

class LD:
    def __init__(self, filename):
        self.input_file = filename
        path, ext = os.path.splitext(self.input_file)
        
        if not ext == ".xyz":
            e = f"only .xyz files are supported, you provided {ext}"
            raise Exception(e)

        self.natoms, self.atomtypes, self.coordinates = self.read_coords()
        shp = self.coordinates.shape
        self.velocities = np.random.rand(shp[0], shp[1]) 
        self.mass = np.array([MASS[atom] for atom in self.atomtypes])/Avogadro
        self.mass = self.mass[:,np.newaxis].T

    def read_coords(self):
        with open(self.input_file) as f:
            natoms = int(f.readline())
            comment = f.readline()
            sym_and_coords = f.readlines()
            sym_and_coords = [line.split() for line in sym_and_coords]
            sym_and_coords = np.array(sym_and_coords)
            atomtypes, coordinates = sym_and_coords[:,0], sym_and_coords[:, 1:].astype(np.float32)

        return natoms, atomtypes, coordinates

    def calculate_F(self):

       #print(f"{self.mass.T.shape=}")
       self.F = - self.velocities * self.mass.T

       return self.F


    def run(self, *args):
        while steps <= nsteps:
            force = calculate_F(self)

xyz = LD("OTS8_1step.xyz")
print(xyz.calculate_F())
