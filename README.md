# IEUK 2025 Engineering Skills Project

The report for the task can be found [here][report].

## Code Installation Guide

The code is in Python 3.13 which should be able to be downoaded [here][python].

It also uses a data handling library called Pandas. It should be able to be downloaded via the pip package manager which should be installed alongside Python. To do so, you just need to input the following into the terminal.

```
pip3 install -U pandas
```

You can check what packages are installed with this command:

```
pip3 list
```

Now you can run the code by navigating to the repo in the terminal and using the following command:
```
python3 logAnalysis.py
```
Where `logAnalysis.py` is of course the name of the file you want to run. Alternatively you can use an IDE like VSCode.

### Troubleshooting

If you have multiple versions of Python installed, do check that the correct pip and python version is being used. You can check via the following commands:
```
pip3 -V
python3 -V
```

If the versions don't match, you can just at `python3 -m` before the pip commands to specify the python version of which the pip is being used.

[report]: report.md
[python]: https://www.python.org/downloads/
