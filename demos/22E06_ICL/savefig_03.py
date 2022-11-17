from ixdat import Measurement

ms = Measurement.read(
    "../../data/03/2022-04-28 23_25_58 Ruti.tsv", reader="zilien", technique="MS"
)

ec_1 = Measurement.read_set("../../data/03/01",  reader="biologic", suffix=".mpt")
ecms_1 = ec_1 + ms

O2_M32 = ecms_1.ecms_calibration_curve(
    mol="O2",
    mass="M32",
    n_el=4,
    tspan_list=[(1300, 1350), (1900, 1950), (2500, 2550)],
    tspan_bg=(950, 1000)
)

ec_2 = Measurement.read_set("../../data/03/06",  reader="biologic", suffix=".mpt")
ecms_2 = ec_2 + ms
ecms_2.calibrate(ms_cal_results=[O2_M32], RE_vs_RHE=0, A_el=0.196)

axes = ecms_2.plot(mol_list=["O2"], tspan=[0, 300], logplot=False, unit="nmol/s")
axes[0].get_figure().savefig("demo_03.png")
