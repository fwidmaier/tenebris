# Tenebris

In the [examples](/examples) directory, you can find some use cases and demonstrations of the mathematical 
capabilities of this small library. A small first-glance application is the implicit definition of functions
(the square root for example):
````python
from tenebris.solver import solve

sqrt = lambda t: solve(lambda x: x * x, t, 1)

print(sqrt(2))  # 1.414213562373095
````

## Installation
Install the library by installing the [wheel file](dist/tenebris-1.0-py2.py3-none-any.whl) from [dist](/dist)
```bash
pip install tenebris-1.0-py2.py3-none-any.whl
```

## (Re-)Building the library
Use the following bash command to build the [wheel file](dist/tenebris-1.0-py2.py3-none-any.whl)
````bash
python setup.py bdist_wheel --universal
````