# Computational Chemistry 

##  Class #1 Presentation 21/09/2020

### Evaluation

80% Project
20% Homework

### Way of working 

1) Talk about topic
2) We made practice about the topic 
3) Write the report with the results and send the report

### *HOMEWORKS AND WORKS TO DO*:
- Install gaussian y gauss view before wednesday ✔️
- Start to think in the topic of the project
- Create a layout in latex for reports ✔️
- Update notes to git and books ✔️
- Read the agenda ✔️
- Read summary about chemical theoretical and quantum chemistry
- Change photo in google ✔️

### Bibliography

Computational chemistry 
Ed 1 https://www.dropbox.com/sh/b6av9sfb876ron3/AADX_El-MfGqXRplMrb2kbDLa?dl=0&preview=Lewars%2C+E+-+Computational+Chemistry+Introduction+To+The+Theory+And+Applications+Of+Molecular+And+Quantum+Mechanics+(Kluwer%2C+2003).pdf

Ed 2 http://www.qfa.uam.es/qcomp/libros/l2.pdf

**saveVideo? Yes ✔️ BUT ALL VIDEOS WILL BE SAVED IN GOOGLE DRIVE

**Dropbox :**

https://www.dropbox.com/sh/b6av9sfb876ron3/AADX_El-MfGqXRplMrb2kbDLa?dl=0

##  Class #2 Gauss View Interface, Molecules construction and Gauss Calculation Configuration  23/09/2020

### **Program Interface**

**Shortcuts**
- Drag : make rotation
- Ctrl+Drag : rotate with a plane fix 
- Shift+Drag : move over the current plane 
- Mouse Scroll : make zoom in and zoom out 
- Ctrl+G: open calculate menu

**Tools**
- _element fragment_: Display the periodic table and you can select a atom, functional group or termination(**NOTE! to display the window with the options you must click a twice**). 
- _ring fragment_: Display a common group of rings to chose.
- _biological fragment_: Display a amino acids and ADN fragments.
- _modify bond_: Select two atom bonded and you can select the type of bond sigma, pi, conjugated, etc., and change the distance between them. 
- _modify angle_: Select tree atoms which made a angle between them and you can change this angle, and select a state (fixed, rotate, etc.) for those atoms.
- _modify dihedral_: With this we can control the angle between 4 atoms over the different planes, click and select 4 atoms bounded, eg. using to make a better geometry in phenol because by default the H set is not over the same plane and we can optimize the geometry.
- _add valence_: Add a new atom bounded to the clicked atom (default H).
- _remove atom_: Remove the selected atom.
- _select atoms by clicking_: when you click over one atom this is selected and numbered with a number in the order that you click them.
- _select atoms by rubber band_: you can select multiple atoms dragging the cursor in the work space.
- _deselect all atoms_: all selected atoms will be deselect.
- _select all atoms_: select all atoms in the workspace.
- _delete_: delete all molecules from the workspace.

### **Calculation Configuration File**

This information is saved in the file with extension .gjf and contain the description of the molecule and atoms position, and also contain the information where has the instructions to made the calculation and the configuration about this.

**Structure of file and configuration**

 1. file location -> this is the directory with the absolute( or relative route) where the file with extension .chk **build or saved?** 
    - Eg. _%chk=absolteRouteOfFile.chk_
 2. number of processors used (**not threads**) -> here you tell how many processors will be used in the calculation.
    - Eg. _%nproc=4_
 3. amount of RAM-> indicate the quantity of RAM in **GB** will be use, also **the max RAM allowed is 1GB gaussian of 32bits**, in 64bits you can specify more.
    - Eg. _%mem=1gb_   
4. method / base / geometry option to use-> In this line you tell which method will be used to calculate the all properties from the system simulated (eg. HF,B3LYP, etc.), and the base to use for the selected method (3-21g,6-32+G,etc.), also can specify other characteristics as empty orbitals (s,p,d),and the option for the geometry of the system.
    - syntax. _% method/base/geometry_  
    - Eg. _% HF/3-31+g(d,p) opt_


### **HOMEWORK**
- get drive link class
- make simulation of F_2 and F with HF and B#LYP
- Read topics
- finish layout in TEX

#### **TOPICS TO CHECK**
- _electric energy_
- _thermodynamics corrections_
- _enthalpy_
- _entropy_
- _free energy_
- _calculus with open/close layer_
- _Hartree Fork_
- _DFT_
- _variationally method_
- _singlet,duplet and triplet_
- _spin_
- _electronic correlation_
- _lineal combination_
- _Hess law_
- _hartrees units_

##  Class #3 "" 28/09/2020
