Author: Carlos E. Hdez. R.
Student ID: A****1616

Pair: José René Signoret Becerra
Student ID: A****4797

## Prerequisites

## You need **Python3.6** or better to run this modules

Python 3.5 or less will not work.

Make sure that you have installed the Coverage.py module with _pip_ or _anaconda_.

```bash
$ pip3 install coverage
```

In order to run the coverage from the console, **first move to the _src/_ folder**.

Coverage.py can receive module names (which can include Python packages) in the same way as the _python_ interpreter.

Since this repository is using Python packages to organize the assignments, we need to specify them when running the
test module, we can specify this with the _-m_ parameter and the name of the file containing the unit tests.

### Running coverage for L6
```bash
$ coverage3 run -m L6.datasorter_test
```

**Note how, when invoking the script as a Python module you don't specify the .py extension. The name of the file is enough.**


### Running coverage for L4
```bash
$ coverage3 run -m L4.assignment_l4_a_d_c_s_carlosehdezrincon
```

**Note how, when invoking the script as a Python module you don't specify the .py extension. The name of the file is enough.**

## Generating a report
After running the coverage report, we can then generate a report to the console:
```bash
$ coverage3 report
```
Or we can get a nicely formatted HTML instead:
```bash
$ coverage3 html
```
This will generate an _htmlcov/index.html_ file that, when opened in a browser will have a colored report on coverage.