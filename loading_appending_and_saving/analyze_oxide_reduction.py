# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:13:38 2021

@author: scott
"""
from matplotlib import pyplot as plt
from ixdat.techniques import CyclicVoltammagram as CV

plt.close("all")

meas = CV.read("./oxide_reduction.csv", reader="ixdat")

meas.plot_measurement()
meas = meas.cut([340, 700])
meas.redefine_cycle(start_potential=1.05, redox=False)
meas.plot_measurement(J_str="cycle")

if True:  # Method 2
    Q_reduction_cycle = meas[1].integrate(
        "raw_current", vspan=[1.0, 0.5], ax="new",
    ) * 1e-3
    Q_base_cycle = meas[2].integrate(
        "raw_current", vspan=[1.0, 0.5], ax="new",
    ) * 1e-3
    Q_red = Q_reduction_cycle - Q_base_cycle
    
    print(f"----------\nreduced with {Q_red*1e6} uC passed.\n---------")

if True: # Method 3
    diff = meas[1].diff_with(meas[2])
    diff.plot()
    Q_red = diff.integrate("raw_current", tspan=[360, 380], ax="new") * 1e-3
    
    print(f"----------\nreduced with {Q_red*1e6} uC passed.\n---------")


