import numpy as np
from morfeus import read_geometry, SASA, BuriedVolume
from morfeus import Pyramidalization, Sterimol
import matplotlib.pyplot as plt

#Ir2mphen catalyst
elements, coordinates = read_geometry("Ir2mphen.gjf")

bv = BuriedVolume(elements, coordinates, 59, excluded_atoms=[51,55,56,15,16,17,21,25,29,
                                                             52,57,58,33,34,35,39,43,47,
                                                             60,61,62,63,64,65,66,67,68],
						             z_axis_atoms=[53,54])
bv.print_report()
bv.plot_steric_map(filename='Ir2mphen')

pyr = Pyramidalization(coordinates, 59)
print("Ir2mphen Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Ir2mphen Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Ir2mphen SASA area", sasa.area)
print("Ir2mphen SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 59, 81)
print("Ir2mphen Sterimol L" , sterimol.L_value)
print("Ir2mphen Sterimol B1", sterimol.B_1_value)
print("Ir2mphen Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried Ir2mphen Sterimol L" , sterimol.L_value)
print("Buried Ir2mphen Sterimol B1", sterimol.B_1_value)
print("Buried Ir2mphen Sterimol B5", sterimol.B_5_value)

#Irtmphen catalyst
elements, coordinates = read_geometry("Irtmphen.gjf")

bv = BuriedVolume(elements, coordinates, 61, excluded_atoms=[54,60,59,37,35,41,36,49,45,
                                                             53,58,57,31,18,17,19,23,27,
                                                             62,64,63,65,67,68,66,69,70],
						             z_axis_atoms=[56,55])
bv.print_report()
bv.plot_steric_map(filename='Ir4mphen')

pyr = Pyramidalization(coordinates, 61)
print("Irtmphen Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Irtmphen Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Irtmphen SASA area", sasa.area)
print("Irtmphen SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 61, 96)
print("Irtmphen Sterimol L" , sterimol.L_value)
print("Irtmphen Sterimol B1", sterimol.B_1_value)
print("Irtmphen Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried Irtmphen Sterimol L" , sterimol.L_value)
print("Buried Irtmphen Sterimol B1", sterimol.B_1_value)
print("Buried Irtmphen Sterimol B5", sterimol.B_5_value)

#Irdtpby catalyst
elements, coordinates = read_geometry("Irdtpby.gjf")

bv = BuriedVolume(elements, coordinates, 57, excluded_atoms=[58,59,60,61,62,63,64,65,66,
                                                             49,53,54,13,15,19,14,27,23,
                                                             50,55,56,31,33,37,32,45,41],
						             z_axis_atoms=[51,52])
bv.print_report()
bv.plot_steric_map(filename='Irdtpby')

pyr = Pyramidalization(coordinates, 57)
print("Irdtpby Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Irdtpby Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Irdtpby SASA area", sasa.area)
print("Irdtpby SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 57, 108)
print("Irdtpby Sterimol L" , sterimol.L_value)
print("Irdtpby Sterimol B1", sterimol.B_1_value)
print("Irdtpby Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried Irdtpby Sterimol L" , sterimol.L_value)
print("Buried Irdtpby Sterimol B1", sterimol.B_1_value)
print("Buried Irdtpby Sterimol B5", sterimol.B_5_value)

#Irdmpe catalyst
elements, coordinates = read_geometry("Irdmpe.gjf")

bv = BuriedVolume(elements, coordinates, 72, excluded_atoms=[38,42,41,20,29,33,19,25,21,
                                                             37,39,40,1,2,3,7,11,15,
                                                             43,44,45,48,49,56,47,50,51],
						             z_axis_atoms=[64,68])
bv.print_report()
bv.plot_steric_map(filename='Irdmpe')

pyr = Pyramidalization(coordinates, 72)
print("Irdmpe Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Irdmpe Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Irdmpe SASA area", sasa.area)
print("Irdmpe SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 72, 88)
print("Irdmpe Sterimol L" , sterimol.L_value)
print("Irdmpe Sterimol B1", sterimol.B_1_value)
print("Irdmpe Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried Irdmpe Sterimol L" , sterimol.L_value)
print("Buried Irdmpe Sterimol B1", sterimol.B_1_value)
print("BUried Irdmpe Sterimol B5", sterimol.B_5_value)

#Irdppe catalyst
elements, coordinates = read_geometry("Irdppe.gjf")

bv = BuriedVolume(elements, coordinates, 116, excluded_atoms=[38,41,42,20,19,33,29,25,21,
                                                              37,39,40,1,3,7,2,11,15,
                                                              43,44,45,47,50,51,46,48,49],
						             z_axis_atoms=[64,90])
bv.print_report()
bv.plot_steric_map(filename='Irdppe')

pyr = Pyramidalization(coordinates, 116)
print("Irdppe Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Irdppe Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Irdppe SASA area", sasa.area)
print("Irdppe SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 116, 108)
print("Irdppe Sterimol L" , sterimol.L_value)
print("Irdppe Sterimol B1", sterimol.B_1_value)
print("Irdppe Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried Irdppe Sterimol L" , sterimol.L_value)
print("Buried Irdppe Sterimol B1", sterimol.B_1_value)
print("Buried Irdppe Sterimol B5", sterimol.B_5_value)



#Ir5Phbpy catalyst
elements, coordinates = read_geometry("Ir5Phbpy.gjf")

bv = BuriedVolume(elements, coordinates, 57, excluded_atoms=[49,53,54,13,14,15,19,27,23,
                                                                  50,55,56,31,33,37,41,32,45,
                                                                  58,59,60,61,62,66,65,64,63],
						             z_axis_atoms=[51,52])
bv.print_report()
bv.plot_steric_map(filename='Ir5Phbpy')

pyr = Pyramidalization(coordinates, 57)
print("Ir5Phbpy Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Ir5Phbpy Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Ir5Phbpy SASA area", sasa.area)
print("Ir5Phbpy SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 57, 92)
print("Ir5Phbpy Sterimol L" , sterimol.L_value)
print("Ir5Phbpy Sterimol B1", sterimol.B_1_value)
print("Ir5Phbpy Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried Ir5Phbpy Sterimol L" , sterimol.L_value)
print("Buried Ir5Phbpy Sterimol B1", sterimol.B_1_value)
print("Buried Ir5Phbpy Sterimol B5", sterimol.B_5_value)


#IrSMAP catalyst
elements, coordinates = read_geometry("IrSMAP.gjf")

bv = BuriedVolume(elements, coordinates, 43,excluded_atoms=[44,45,46,47,48,49,50,51,52,
                                                            38,41,42,20,29,33,19,21,25,
                                                            37,39,40,1,2,3,7,11,15],
						             z_axis_atoms=[65,66])
bv.print_report()
bv.plot_steric_map(filename='IrSMAP')

pyr = Pyramidalization(coordinates, 43)
print("IrSMAP Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("IrSMAP Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("IrSMAP SASA area", sasa.area)
print("IrSMAP SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 43, 95)
print("IrSMAP Sterimol L" , sterimol.L_value)
print("IrSMAP Sterimol B1", sterimol.B_1_value)
print("IrSMAP Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried IrSMAP Sterimol L" , sterimol.L_value)
print("Buried IrSMAP Sterimol B1", sterimol.B_1_value)
print("Buried IrSMAP Sterimol B5", sterimol.B_5_value)

#RuCpstar catalyst
elements, coordinates = read_geometry("RuCpstar.gjf")

bv = BuriedVolume(elements, coordinates, 89, excluded_atoms=[7,1,2,35,36,37,41,49,45,
                                                             8,3,4,53,55,59,54,63,67,
                                                             9,5,6,71,73,77,72,81,85],
						             z_axis_atoms=[10,11,12])
bv.print_report()
bv.plot_steric_map(filename='RuCpstar')

pyr = Pyramidalization(coordinates, 89)
print("RuCpstar Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("RuCpstar Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("RuCpstar SASA area", sasa.area)
print("RuCpstar SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates,89, 24)
print("RuCpstar Sterimol L" , sterimol.L_value)
print("RuCpstar Sterimol B1", sterimol.B_1_value)
print("RuCpstar Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried RuCPstar Sterimol L" , sterimol.L_value)
print("Buried RuCPstar Sterimol B1", sterimol.B_1_value)
print("Buried RuCPstar Sterimol B5", sterimol.B_5_value)

#RhCpstar catalyst
elements, coordinates = read_geometry("RhCpstar.gjf")

bv = BuriedVolume(elements, coordinates, 1, excluded_atoms=[79,83,70,69,71,75,87,88,89,
                                                            90,91,92,94,98,97,93,96,95,
                                                            48,49,50,51,53,54,52,56,55,
                                                            27,28,29,30,31,34,35,32,33],
						             z_axis_atoms=[2,3,6])
bv.print_report()
bv.plot_steric_map(filename='RhCpstar')

pyr = Pyramidalization(coordinates, 1)
print("RhCpstar Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("RhCpstar Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("RhCpstar SASA area", sasa.area)
print("RhCpstar SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 1, 25)
print("RhCpstar Sterimol L" , sterimol.L_value)
print("RhCpstar Sterimol B1", sterimol.B_1_value)
print("RhCpstar Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried RhCpstar Sterimol L" , sterimol.L_value)
print("Buried RhCpstar Sterimol B1", sterimol.B_1_value)
print("Buried RhCpstar Sterimol B5", sterimol.B_5_value)

# catalyst
elements, coordinates = read_geometry("IrtAs.gjf")

bv = BuriedVolume(elements, coordinates, 108, excluded_atoms=[ 43, 44, 45, 46, 47,48, 49, 50, 51, 
							      37, 39, 40, 1,
                                                              2, 3, 7, 11, 15, 38, 42, 41, 20,
                                                              33, 29, 19, 25, 21],
						             z_axis_atoms=[131,132])
bv.print_report()
bv.plot_steric_map(filename='IrtAs')

pyr = Pyramidalization(coordinates, 108)
print("IrtAs Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("IrtAs Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("IrtAs SASA area", sasa.area)
print("IrtAs SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 108, 130)
print("IrtAs Sterimol L" , sterimol.L_value)
print("IrtAs Sterimol B1", sterimol.B_1_value)
print("IrtAs Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried IrtAs Sterimol L" , sterimol.L_value)
print("Buried IrtAs Sterimol B1", sterimol.B_1_value)
print("Buried IrtAs Sterimol B5", sterimol.B_5_value)

#1,10 phenanthroline catalyst
elements, coordinates = read_geometry("1_10_phen_Ir.gjf")

bv = BuriedVolume(elements, coordinates, 61, excluded_atoms=[54,60,59,37,35,41,36,49,45,
                                                             53,58,57,31,18,17,19,23,27,
                                                             62,64,63,65,67,68,66,69,70],
						             z_axis_atoms=[56,55])
bv.print_report()
bv.plot_steric_map(filename='Ir4mphen')

pyr = Pyramidalization(coordinates, 61)
print("1_10_phen_Ir Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("1_10_phen_Ir Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("1_10_phen_Ir SASA area", sasa.area)
print("1_10_phen_Ir SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 61, 7)
print("1_10_phen_Ir Sterimol L" , sterimol.L_value)
print("1_10_phen_Ir Sterimol B1", sterimol.B_1_value)
print("1_10_phen_Ir Sterimol B5", sterimol.B_5_value)

sterimol.bury(method="delete")
print("Buried 1_10_phen_Ir Sterimol L" , sterimol.L_value)
print("Buried 1_10_phen_Ir Sterimol B1", sterimol.B_1_value)
print("Buried 1_10_phen_Ir Sterimol B5", sterimol.B_5_value)

