from morfeus import ConeAngle, read_geometry, SASA, BuriedVolume
from morfeus import Pyramidalization, Sterimol

#Ir2mphen catalyst
elements, coordinates = read_geometry("Ir2mphen.gjf")

cone_angle = ConeAngle(elements, coordinates, 61)
print("Ir2mphen cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 61, excluded_atoms=[1,3,4,5,16,6,8,10,11,15,13,12,83,11,
                                                             54,60,59,37,35,41,36,49,45,
                                                             53,58,57,31,18,17,19,23,27,
                                                             62,64,63,65,67,68,66,69,70])
bv.print_report()


pyr = Pyramidalization(coordinates, 61)
print("Ir2mphen Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Ir2mphen Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Ir2mphen SASA area", sasa.area)
print("Ir2mphen SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 61, 83)
print("Ir2mphen Sterimol L" , sterimol.L_value)
print("Ir2mphen Sterimol B1", sterimol.B_1_value)
print("Ir2mphen Sterimol B5", sterimol.B_5_value)

#Ir4mphen catalyst
elements, coordinates = read_geometry("Ir4mphen.gjf")

cone_angle = ConeAngle(elements, coordinates, 61)
print("Ir4mphen cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 61, excluded_atoms=[1,3,4,5,16,6,8,10,11,15,13,12,83,87,95,91,
                                                             54,60,59,37,35,41,36,49,45,
                                                             53,58,57,31,18,17,19,23,27,
                                                             62,64,63,65,67,68,66,69,70])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 61)
print("Ir4mphen Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Ir4mphen Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Ir4mphen SASA area", sasa.area)
print("Ir4mphen SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 61, 83)
print("Ir4mphen Sterimol L" , sterimol.L_value)
print("Ir4mphen Sterimol B1", sterimol.B_1_value)
print("Ir4mphen Sterimol B5", sterimol.B_5_value)



#Irdtpby catalyst
elements, coordinates = read_geometry("Irdtpby.gjf")

cone_angle = ConeAngle(elements, coordinates, 57)
print("Irdtpby cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 57, excluded_atoms=[1,3,4,5,12,11,6,7,8,9,83,97,105,101,84,85,93,89,
                                                             58,59,60,61,62,63,64,65,66,
                                                             49,53,54,13,15,19,14,27,23,
                                                             50,55,56,31,33,37,32,54,41])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 57)
print("Irdtpby Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Irdtpby Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Irdtpby SASA area", sasa.area)
print("Irdtpby SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 57, 93)
print("Irdtpby Sterimol L" , sterimol.L_value)
print("Irdtpby Sterimol B1", sterimol.B_1_value)
print("Irdtpby Sterimol B5", sterimol.B_5_value)



#Irdmpe catalyst
elements, coordinates = read_geometry("Irdmpe.gjf")

cone_angle = ConeAngle(elements, coordinates, 72)
print("Irdmpe cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 72, excluded_atoms=[85,81,65,69,73,77,
                                                             38,42,41,20,29,33,19,25,21,
                                                             37,39,40,1,2,3,7,11,15,
                                                             43,44,45,48,49,56,47,50,51])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 72)
print("Irdmpe Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Irdmpe Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Irdmpe SASA area", sasa.area)
print("Irdmpe SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 72, 85)
print("Irdmpe Sterimol L" , sterimol.L_value)
print("Irdmpe Sterimol B1", sterimol.B_1_value)
print("Irdmpe Sterimol B5", sterimol.B_5_value)

#Irdppe catalyst
elements, coordinates = read_geometry("Irdppe.gjf")

cone_angle = ConeAngle(elements, coordinates, 116)
print("Irdppe cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 116, excluded_atoms=[65,91,66,67,68,69,70,71,
                                                              72,73,74,75,76,77,
                                                              92,93,94,95,96,97,
                                                              38,41,42,20,19,33,29,25,21,
                                                              37,39,40,1,3,7,2,11,15,
                                                              43,44,45,47,50,51,46,48,49])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 116)
print("Irdppe Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("Irdppe Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("Irdppe SASA area", sasa.area)
print("Irdppe SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 116, 75)
print("Irdppe Sterimol L" , sterimol.L_value)
print("Irdppe Sterimol B1", sterimol.B_1_value)
print("Irdppe Sterimol B5", sterimol.B_5_value)

#IrmphenPh catalyst
elements, coordinates = read_geometry("IrmphenPh.gjf")

cone_angle = ConeAngle(elements, coordinates, 61)
print("IrmphenPh cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 61, excluded_atoms=[13,12,11,10,15,8,6,5,4,3,1,87,86,88,89,91,93,
                                                                  54,60,59,36,49,45,41,35,37,
                                                                  53,57,58,17,19,23,18,27,31,
                                                                  62,63,64,65,66,67,68,69,70])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 61)
print("IrmphenPh Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("IrmphenPh Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("IrmphenPh SASA area", sasa.area)
print("IrmphenPh SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 61, 93)
print("IrmphenPh Sterimol L" , sterimol.L_value)
print("IrmphenPh Sterimol B1", sterimol.B_1_value)
print("IrmphenPh Sterimol B5", sterimol.B_5_value)




#IrSMAP catalyst
elements, coordinates = read_geometry("IrSMAP.gjf")

cone_angle = ConeAngle(elements, coordinates, 43)
print("IrSMAP cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 43,excluded_atoms=[69,70,71,72,67,68,66,85,86,87,88,89,90,98,94,
                                                            44,45,46,47,48,49,50,51,52,
                                                            38,41,42,20,29,33,19,21,25,
                                                            37,39,40,1,2,3,7,11,15])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 43)
print("IrSMAP Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("IrSMAP Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("IrSMAP SASA area", sasa.area)
print("IrSMAP SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 43, 94)
print("IrSMAP Sterimol L" , sterimol.L_value)
print("IrSMAP Sterimol B1", sterimol.B_1_value)
print("IrSMAP Sterimol B5", sterimol.B_5_value)


#RuCpstar catalyst
elements, coordinates = read_geometry("RuCpstar.gjf")

cone_angle = ConeAngle(elements, coordinates, 89)
print("RuCpstar cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 89, excluded_atoms=[10,11,13,14,15,19,23,27,31,
                                                             7,1,2,35,36,37,41,49,45,
                                                             8,3,4,53,55,59,54,63,67,
                                                             9,5,6,71,73,77,72,81,85])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 89)
print("RuCpstar Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("RuCpstar Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("RuCpstar SASA area", sasa.area)
print("RuCpstar SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates,89, 15)
print("RuCpstar Sterimol L" , sterimol.L_value)
print("RuCpstar Sterimol B1", sterimol.B_1_value)
print("RuCpstar Sterimol B5", sterimol.B_5_value)

#RhCpstar catalyst
elements, coordinates = read_geometry("RhCpstar.gjf")

cone_angle = ConeAngle(elements, coordinates, 1)
print("RhCpstar cone angle", cone_angle.cone_angle)

bv = BuriedVolume(elements, coordinates, 1, excluded_atoms=[2,4,5,6,7,11,15,19,23,
                                                            79,83,70,69,71,75,87,88,89,
                                                            90,91,92,94,98,97,93,96,95,
                                                            48,49,50,51,53,54,52,56,55,
                                                            27,28,29,30,31,34,35,32,33])
bv.print_report()
#print("buried volume", bv)

pyr = Pyramidalization(coordinates, 1)
print("RhCpstar Pyramidalization By Agranat and Radhakrishnan", pyr.P)
print("RhCpstar Pyramidalization By Gavrish", pyr.P_angle)

sasa = SASA(elements, coordinates)
print("RhCpstar SASA area", sasa.area)
print("RhCpstar SASA voleume", sasa.volume)

sterimol = Sterimol(elements, coordinates, 1, 15)
print("RhCpstar Sterimol L" , sterimol.L_value)
print("RhCpstar Sterimol B1", sterimol.B_1_value)
print("RhCpstar Sterimol B5", sterimol.B_5_value)





