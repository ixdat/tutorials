# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:13:38 2021

@author: scott
"""
import numpy as np
from matplotlib import pyplot as plt
from ixdat.techniques import CyclicVoltammagram as CV

plt.close("all")

meas = CV.read("./oxide_reduction.csv", reader="ixdat")

meas.plot_measurement()

if True:  # Method 1
    tspan_red = [362, 377]
    t_red, I_red = meas.grab("raw_current", tspan=tspan_red)
    v_red = meas.grab_for_t("potential", t_red)

    tspan_base = [470, 485]
    t_base, I_base = meas.grab("raw_current", tspan=tspan_base)
    v_base = meas.grab_for_t("potential", t_base)

    fig, ax = plt.subplots()
    ax.plot(v_red, I_red, "g")
    ax.plot(v_base, I_base, "k")

    Q_red = np.trapz(I_red, t_red) * 1e-3
    Q_base = np.trapz(I_base, t_base) * 1e-3

    dQ_red = Q_red - Q_base
    print(f"----------\nreduced with {dQ_red*1e6} uC passed.\n---------")


#  this is used for both methods 2 and 3
meas = meas.cut([340, 700])
meas.redefine_cycle(start_potential=1.05, redox=False)
meas.plot_measurement(J_str="cycle")


if True:  # Method 2
    Q_reduction_cycle = (
        meas[1].integrate(
            "raw_current",
            vspan=[1.0, 0.5],
            ax="new",
        )
        * 1e-3
    )
    Q_base_cycle = (
        meas[2].integrate(
            "raw_current",
            vspan=[1.0, 0.5],
            ax="new",
        )
        * 1e-3
    )
    Q_red = Q_reduction_cycle - Q_base_cycle

    print(f"----------\nreduced with {Q_red*1e6} uC passed.\n---------")

if True:  # Method 3
    diff = meas[1].diff_with(meas[2])
    diff.plot()
    Q_red = diff.integrate("raw_current", tspan=[360, 380], ax="new") * 1e-3

    print(f"----------\nreduced with {Q_red*1e6} uC passed.\n---------")
