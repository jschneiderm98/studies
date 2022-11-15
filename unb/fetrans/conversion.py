#force
lbf_to_newton_ratio = 4.44822
#length
inch_to_meter_ratio = 0.0254
ft_to_meter_ratio = 0.3048
#mass
lb_to_kg_ratio = 0.453592
#energy
btu_to_j_ratio = 1055.06
j_to_btu_ratio = 1 / btu_to_j_ratio

def lbf_to_newton(force_in_lbf):
    return force_in_lbf * lbf_to_newton_ratio

def Inch_to_meter(length_in_In):
    return length_in_In * inch_to_meter_ratio

def squaredIn_to_squaredM(area_in_squaredIn):
    return area_in_squaredIn * inch_to_meter_ratio**2

def lbf_per_squaredIn_to_pascal(pressure_in_lbf_per_squaredIn):
    return pressure_in_lbf_per_squaredIn * lbf_to_newton_ratio / inch_to_meter_ratio**2

def ft_to_meter(length_in_ft):
    return length_in_ft * ft_to_meter_ratio

def lb_to_kg(weigth_in_lb):
    return weigth_in_lb * lb_to_kg_ratio

def cubicFt_per_lb_to_cubicMeter_per_kg(value_in_cubicFeet_per_lb):
    return value_in_cubicFeet_per_lb * ft_to_meter_ratio**3 / lb_to_kg_ratio

def btu_to_j (energy_in_btu):
    return energy_in_btu * btu_to_j_ratio

def btu_per_lb_to_j_per_kg(value_in_btu_per_lb):
    return value_in_btu_per_lb * btu_to_j_ratio / lb_to_kg_ratio

def j_to_btu(energy_in_j):
    return energy_in_j * j_to_btu_ratio