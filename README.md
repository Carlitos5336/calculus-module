# calculus-module

An **experimental calculus module for Python** – calculate derivatives, integrals, and differential equations.\
Ideal for **students** and **researchers** who want to playtest symbolic and numerical calculus operations.

---

## Features

- Symbolic differentiation (derivatives of functions)
- Numerical integration methods (e.g., midpoint rule)
- Root finding and differential equations tools
- Fully modular – import only what you need
- Simple API for experimenting with calculus expressions

---

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

Clone the repo and install dependencies:

```bash
git clone https://github.com/Carlitos5336/calculus-module.git
cd calculus-module
poetry install
```

Alternatively, use pip in an existing environment:

```bash
pip install -e .
```

---

## Example Usage

Here’s how you can build a composite function, differentiate it, and calculate an integral:

```python
import calculus.base as calc
import calculus.integrals as it

# Define f(x) = log(x) / (x^n + e^x)
f = calc.Divission(
        calc.Logaritmic(),
        calc.Addition([calc.Polynomial(), calc.Exponential()])
    )

print(f)  # Print the symbolic representation of f(x)
print(f.differentiate())  # Print derivative f'(x)

# Approximate ∫[2,6] f(x) dx using the midpoint method
print(it.middlePoint_method(f, [2, 6]))
```

---

## Project Structure

```
calculus-module/
├── calculus/             # Main module with calculus classes & functions
│   ├── base.py           # Core function classes (Polynomial, Exponential, etc.)
│   ├── diff_eq.py        # Differential equations tools
│   ├── integrals.py      # Numerical integration methods
│   └── roots.py          # Root-finding algorithms
├── main.py               # Example script
├── poetry.lock           # Poetry dependency lock file
├── pyproject.toml        # Project metadata & dependencies
└── README.md             # Project overview (this file)
```

---
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits
Created by Carlos Bienvenido Ogando Montás. If you use this material, please give proper attribution.

## Notes

This is a work in progress. API changes are likely as features evolve.\
For now, import directly from `calculus/` whatever classes or functions you need.
