# Python Lab Re-performance

Three Python laboratory experiments repeated from the supplied college assignments, with runnable code, actual execution output and supporting documentation.

## Experiments and source mapping

| Submission folder | Original practical | Experiment | Reference file |
| --- | --- | --- | --- |
| [Experiment 1](Experiment-1/) | 8 | Creating and using packages and modules | Practical No 8 (1).pdf |
| [Experiment 2](Experiment-2/) | 9 | File handling: open, close, read, write, append and copy | Practical No 9 (2).pdf |
| [Experiment 3](Experiment-3/) | 10 | Handling built-in exceptions | Practical No 10 (1).pdf |

All eight pages of the three references were read. Practical numbers above follow the visible page headings: the PDFs' embedded text layers contain stale numbers for two documents. Exactly one experiment was selected from each file. Supporting package modules in Experiment 1 are required for its package objective. Source PDFs are reference material and are not redistributed here.

## Requirements and execution

Python 3.10 or newer. Only standard-library modules are used, so no package installation is required. requirements.txt records this explicitly.

From the repository root:

```console
python Experiment-1/experiment_1.py
python Experiment-2/experiment_2.py
python Experiment-3/experiment_3.py
```

The fixed inputs reproduce the assignment examples. Experiment 2 creates or replaces only its own outputs/source.txt and outputs/destination.txt. Repeated runs reset the original content before appending. Each experiment can also be started from another working directory.

## Repository contents

```text
Python-Lab-Reperformance/
|-- README.md
|-- requirements.txt
|-- verify_experiments.py
|-- verification.txt
|-- Experiment-1/
|   |-- experiment_1.py
|   |-- MyPackage/
|   |   |-- __init__.py
|   |   |-- arithmetic.py
|   |   `-- geometry.py
|   |-- output.txt
|   |-- README.md
|   `-- outputs/
|       |-- execution.json
|       `-- execution.png
|-- Experiment-2/
|   |-- experiment_2.py
|   |-- output.txt
|   |-- README.md
|   `-- outputs/
|       |-- source.txt
|       |-- destination.txt
|       |-- execution.json
|       `-- execution.png
`-- Experiment-3/
    |-- experiment_3.py
    |-- output.txt
    |-- README.md
    `-- outputs/
        |-- execution.json
        `-- execution.png
```

## Execution evidence and verification

Each output.txt was written directly from a successful Python subprocess's stdout, without copying the expected results from a PDF. Each outputs/execution.json records the command, Python version, UTC execution time, exit code and stderr. Each outputs/execution.png is an actual screenshot of the execution viewer showing that captured run. These are output-viewer screenshots rather than native terminal screenshots.

To verify the programs again:

```console
python -B verify_experiments.py
```

The script checks fresh execution of all three programs against the saved stdout, package calculations, file contents and identical copied bytes, repeated file handling, I/O error handling, the original five division cases, additional numeric inputs and the exception handlers. Controlled test doubles exercise the less common ValueError and generic fallback division branches. The saved run is in [verification.txt](verification.txt).

## Corrections to the reference examples

- File handling: reopen source.txt in read mode after closing the write handle. Repair indentation and broken statement wrapping.
- Exception handling: dividing 10 by 'two' or None raises TypeError. Both are correctly caught by the TypeError handler. Genuine ValueError examples are included through the integer conversion and list search functions requested in the review questions.
- Packages: retain the original MyPackage structure, functions, sample inputs and pi = 3.14. Display circle measurements to two decimal places.

Each experiment README contains its aim, problem, theory, algorithm, code explanation, actual output, corrections, result and answers to the assignment's review questions.
