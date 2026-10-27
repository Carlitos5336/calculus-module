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

You can install the library directly from GitHub using `pip`.

```bash
python -m pip install "git+https://github.com/Carlitos5336/calculus-module.git"
```

This command downloads the repository, builds the package, and installs it along with its declared dependencies.

### Install from source

Alternatively, clone the repository and install it locally:

```bash
git clone https://github.com/Carlitos5336/calculus-module.git
cd calculus-module
python -m pip install .
```

If you plan to modify the library while developing it, use editable mode instead:

```bash
python -m pip install -e .
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
├── calculus/
│   ├── __init__.py       # Package initialization
│   ├── base.py           # Core function classes
│   ├── diff_eq.py        # Differential equations tools
│   ├── integrals.py      # Numerical integration methods
│   └── roots.py          # Root-finding algorithms
├── main.py               # Example script
├── pyproject.toml        # Project metadata and build configuration
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

---
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits
Created by Carlos Bienvenido Ogando Montás. If you use this material, please give proper attribution.

## Notes

This is a work in progress, and API changes are likely as features evolve.

For now, import the classes and functions you need directly from the calculus package.
