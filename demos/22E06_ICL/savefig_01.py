from ixdat import Measurement


ec = Measurement.read(
    "../../data/01/iridium_butterfly_short_CVA.mpt", reader="biologic"
)

ec.calibrate(RE_vs_RHE=0.720, A_el=0.196)
cv = ec.as_cv()

cv.redefine_cycle(start_potential=0.3, redox=True)

ax = cv.plot_cycles()
ax.get_figure().savefig("demo_01.png")
