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

##  Class #2 Gauss View Interface, Molecules construction and Gauss Calculation Configuration 23/09/2020

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

##  Class #3 electric energy of correlation (Practice #1 finished) 28/09/2020

### Results treatment

After to finish the calculation por F2 and F by both methods HF and B3LYP ,we procede to get the enthalpy of the reaction.
To get this we use the Hess law this express that the enthalpy of reaction is the proportional to the difference between the enthalpy products less reactives.

### _enthalpy of products - enthalpy of reactives_

In our case this is the following test

### _enthalpy of F2 - 2(enthalpy of F)_

This is getting in log file and is called the sum of energy thermodynamic enthalpy and is in Hartrees units 

We get the current energy enthalpy for reacción in both cases using B3LYP and HF and we will compare them

To convert the value to KgCal/mol you use the convertor factor which is 627.51

**To get the error you need find the experimental value**

Make a table and compare the importance of the electric correlation energy which is considered in method DFT but not in HF

#### DFT is not a method, B3LYP yes.

### HOMEWORK

- Make a summary of class ✔️
- Make a layout for report
- Search information for the report 
- Do another method extra 
- Make a report
- Send a report 

### Topics
- _enthalpy reaction_
- _electric energy correlation_
- _error percentage_
- _differences HF Vs DFT_

##  Class #4 Energy correlation 30/09/2020

### Methods   

- LC-WPBE-> General calculus acceptable
- M062X -> Good functional for kinetic calculus 
- B3LYP -> Good functional for thermodynamics calculus
- CC (cupper cluster is The best, but very expensive)

### Computational chemistry 

Modeling all aspects of chemistry instead of experimentation 

The theoretical chemistry includes quantum chemistry 

Exist two types the molecular mechanics and the quantum mechanics, using the partition function you can calculate the thermodynamics properties.

With *molecular dynamics* you can see conformations, are based in classic, and consider interactions of force fields, distance between bodies, bond angle, dihedral angle, electric charges and van der wals interactions.

In the *quantum mechanics* are based in Schrödinger equation, the energy usgin HF obtained is bigger than real energy for this reason is necessary consider a correlation energy which make a better aproximation.

when the set bases is big the correlation energy is better and the calculus will be more approximate, but the contribution is more important by the methods. 

We build a part of the system of atmospheric reaction

##  Class #5 atmospheric reaction 05/10/2020

### Transition state

We build methane and connect with a hydroxyl radical, we adjust the bond distance to 1.2A between C-H and 1.3A between H-O

and was run with the following configuration, because we are running a transition state 

      # opt=(calcfc,ts,noeigen) freq=(noraman) B3LYP/6-31+g(d,p)

*calcfc* is calculate force constants.
*ts* calculate the transition state this means that you dont look form the minimizartion of system

*noeigen* this is when you can have a imaginery vibrations, when calculate a transition state you are loking for a imaginary freq.

*noraman* you dont calculate raman spectro and save time.

this calculations are made for HF,M062X and B3LYP and basis set 6-31+g(d,p) and 6-311++g(d,p) with m062X.

### Reactives 

hydroxyl radical and methane and we run with normal configuration 

### Products 

the products was a water and methyl radical.

all of this were run with the following configuration were don't calculate constente force and ts.

      #opt freq *methods*/6-31+g(d,p)

To re run because the minification was not finished you use this configuration 

      #opt(readfc,noeigen,ts) freq=noraman guess *methods*/6-31+g(d,p)

*guess* read the .chk file 

check for negative frequency if are negative you got the transition state

### objetives

- make a profile reaction 
- and compare the rate constant 

### HOMEWORK

-run calculus and get all Hess calculus 
-save all calculations in excel sheet 

##  Class #6 reaction profile 07/10/2020

### Building the reaction profile

With the data obtained of ZPE, ΔG and ΔH we calculate the Δ for each one and the diferences were convert to Kcal/mol and graph, getteing just 3 points and set as 0 the first point to get 4 points 

with this you are plot the ΔG of reactions vs reaction coordenate and you can see the behavior of the reaction.

make the same for each method and plot with all values PE, ΔG and ΔH

### fix problem of iteration 

when calculation is not finish you can do steps more small using 

      iop(1/8=2)

### HOMEWORK

-Build a profile plot 

##  Class #7 rate constant 12/10/2020

### Rate constant

We calculate the rate constant using the value the ΔG of transition state, and compare with the experimental value 4x10^6, this help us to confirm wich method is better in kinetics.

also compare how many times is more faster or lower CTE Teo/CTE Exp

The calculus if multiplu by the number of posibles conformations because the ways to make a reaction can be many in the methane case can be in 4 directions this why is multypli by simetry

### HOMEWORK 

-check transition state teory
-calculate the rate constant and with tunel and without tunnel

##  Class #8 rate constant 26/10/2020

## Transition state teory (TST)

Using the Arrhenius equation you can calculate the rate constant, but you need know the pre exponential factor.

In TST using the partitin functions and the gibs ecuations to get another ecuation to be able to calculate the rate constant only using the ΔG for reaction of first order, and also in reaction of second order.

### NOTES

In unimolecular reaction ΔH~ΔZPE(energy electronic in 0k)~ΔG, but in bimolecular reactions this are not true.

In unimolecular reactions the tipic error are aprox 1.5kcal/mol almost always use ΔG instead ZPE only in a few cases you use ZPE.

In fluor practice we use ΔH because in literature the heat of reaction is avalible but no the ΔGreaction.

If consider ΔG~ΔH~ZPE the error will incress to 6-7 kcal/mol

to convert the TST equation in bimolecular reaction we multiply for the factor (RT/p)

The tunnelaje constant are only considered when the tranference is of small atom like H, more bigger are despreciable.
(energy variation electronic in 0k) ~ΔE(variation of electronic energy)

*The max value of rate constant is when ΔG is cero!!!*

#### gaussinan don't make diference between kp and kc

**NIST chemical kinetics database**

##  Class #9 adition reaction 28/10/2020

### Objetive 

- considerar ahora una reaction with distintive number o mol.

### System 

Reaction of adition of radical hidroxyl and ethene

### Transition state 

CH2-CH2 binding with OH radical, set a distance of 2A between C-O and rotate the H in alternate conformartion with the carbon join with O.

We use the following configuration 
    
      # opt=(calcfc,ts,noeigen) freq=noraman 6-31+g(d,p) iop(1/8=3) b3lyp

**iop** step small to get the divergence of 4 values.

**noeigen** work with imaginary numbers.

Error of max of ciclees link 9999 can be generated by these actions
-imaginary numbers (solve with noeigen)
-number max of cicles to converged execed(solve when you read an run again)
-4 dihedros not defines 

if you need re run because are not divergend use this configuration.

      # opt=(readfc,ts,noeigen) geom=check guess=check freq=noraman 6-31+g(d,p) iop(1/8=3) b3lyp

**readfc** read force constans of .chk file.

**geom=check** use the positions saved in .chk

**guess=check** used to check info in .chk file

### syntax 


Title card

x y 

x is the charge and y is the multiplicity(singulet, duplet)


### Calculus

RECOMEND NO MORE THAN 12 ATOMS!(takes to much time)


### Reactives

ethene and hidroxyl with the following configuration

### Product

etenol radical 

      # opt freq=noraman 6-31+g(d,p) m052x

##  Class #10 profile reaction reaction 04/11/2020

### Conclusion 

- Over calculate the energy HF
- B3LYP subestim the energy
- M062X and M052X are good for cinetic 

In profile reaction compare the ΔH and ΔG with practice 2 because change the behaviour 

Disminución del número de moles cuando se forma el estado de transición, si son un producto las rectas se hacen paralelas, esto implica una dismunción de la entropia y eso cambia el ΔG

Al formar solo 1 producto se pierden grados de libertad y por lo tanto hay una disminución de la entropia.

La reacción es mas exergonica, pero exotermica, es decir que hay mas ganacia de energía libre que de calor al generar los prodcutos.

Max vibration is negative(atracction of atoms indicate a formation of bond) in transition state, 

script tuneling ΔH es ΔZPE, vibration is in absolute value, temperature 298.15K kappa=tunneling constant

### HOMEWORK 

- make calculations
- pass data to sheet excel 
- make calculations
- make graphs 
- make report

##  Class #11 profile reaction reaction 09/11/2020

### Solvent effect 

The contribution of solvent is aprox 100kcal/mol (max 110kcal/mol H3O), this influence affect without thinking if is polar or not

### Solvent models 

- Isolated molucule, this is consider a molecule without other thing (gas phase)

- Super molecule, molecule make a interacctions especific with a molecules of solvent

- continuum model, consider the dielectric constant to consider the charge consideration with a specific solvent.

-full model or periodic, solvate and calculate cosider each interaction(very expensive)

### Model Cramer and Truler

### Pka calculation

### System 

We use the most basic acid, formic acid CH3COOH with is desprotonated in water 

### Reactive

Formic acid, water,

### Products

Formeate, hidrium H3O

### Procedure 

0) products 

H3O+ move dihedral angles from 180 to 140, specify charge in 1+

1 First make a model continue 

      #opt freq 6-31+g(d,p) scrf=smd m062x

*scrf=smd* this make a solvatation with model continuum, solvatation blink SMD default 

after re run with super model, the log config use to join water molecules with distance of 1.7A, afeter run both you get a mix model 

### isodesmic reaction

reaction which the number of bond in reactives and products are the same 

### Pka indirective calculus

calculate a Pka using a acid of reference 

NOTA **YOU CAN'T KNOW BOND ORDER (-,=,≡) this is a human convention which is not really exist!**

























