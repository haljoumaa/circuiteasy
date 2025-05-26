⚡Circuiteasy

Fast, exam-friendly Python utilities for circuit analysis and electronics students.

circuiteasy is a Python library that helps you quickly solve, analyze, and visualize common electrical engineering problems with minimal code.
It is designed to save time during exams and assignments, letting you focus on circuit logic, not boilerplate math.

🚀 Features

📏 DC & AC Calculations: Voltage/current dividers, parallel/series resistors, complex impedance, BJT parameters/Q-point plotter.
⚡ Power Analysis: DC/AC power, apparent/reactive/real power, dB conversions, SI formatting.
🔄 Signal & Laplace Utilities: RMS, peak-to-peak, frequency conversions, Laplace/inverse Laplace.
🧑‍🔬 Solver Tools: Symbolic and numeric solvers for node/mesh analysis and more.
🛠 Designed for Students: Simple syntax, readable output, exam-optimized.
📦 Installation

Install with pip:

pip install circuiteasy
Either in your VS Code environment or using the terminal.
(Advantage: have it in your Python path for instant access during exams!)

📚 Modules and Usage

dc.py – DC circuit tools (series, parallel, voltage/current divider, Wheatstone bridge)
ac.py – AC circuit tools (impedance, admittance, frequency response)
bjt.py – BJT analysis (gm, re, rpi, current conversions)
power.py – DC/AC power, dB, SI formatting
signal_utils.py – Peak, RMS, frequency conversions
laplace.py – Laplace and inverse Laplace transforms
complex_utils.py – Complex/polar conversion, printing
✨ Example

from circuiteasy.dc import series, parallel, voltage_divider
from circuiteasy.ac import impedance_c
from circuiteasy.bjt import find_gm

# DC calculations
R_total = series(10, 20, 30)           # 60 Ω
R_parallel = parallel(100, 200, 300)   # 54.55 Ω
V_out = voltage_divider(12, 10, 20)    # 8.0 V

# AC impedance
Zc = impedance_c(1e-6, 2*3.14*50)      # -j3183 Ω at 50 Hz

# BJT transconductance
gm = find_gm(Ic=0.002)                 # 0.077 S
📖 Documentation

Full function reference coming soon!
For now, see code and docstrings in each module.

🤝 Contributing

Pull requests and issues welcome!
Help us make circuit analysis even easier for students everywhere.

📄 License

MIT

👤 Author

Hareth Aljomaa (haljoumaa)

