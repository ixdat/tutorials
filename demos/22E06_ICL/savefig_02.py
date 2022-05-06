from pathlib import Path
from ixdat import Measurement

data_dir = Path("../../data/02")

sec_meas = Measurement.read(
    data_dir / "test-7SEC.csv",
    path_to_ref_spec_file=data_dir / "WL.csv",
    path_to_U_J_file=data_dir / "test-7_JV.csv",
    scan_rate=1,
    tstamp=1,
    reader="msrh_sec",
)

sec_meas.calibrate_RE(RE_vs_RHE=0.2)
sec_meas.set_reference_spectrum(V_ref=0.6)

ax = sec_meas.plot_waterfall()

ax.get_figure().savefig("demo_02.png")
