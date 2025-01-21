# Python OOPs Project

This repository contains an object-oriented programming (OOP) project in Python. It includes multiple modules and a `tests` folder that contains test cases for all the modules in the project.

## Prerequisites

To run this project, ensure you have the following installed on your system:
- Python 3.7 or higher
- `pytest`
- `pytest-cov`

You can install the required dependencies using pip:
```bash
pip install pytest pytest-cov
```

To verify the installation, run:
```bash
pytest --version
```
You should see the pytest version and a list of installed plugins, including pytest-cov.

## Running Tests
To run all the tests in the tests folder, use the following command:
```bash
python -m pytest
```
## Code Coverage
To check the code coverage of your tests, use the pytest-cov plugin. Run the following command:

```bash
python -m pytest --cov=python_oops_project
```

## Generating Detailed Coverage Reports
### Terminal Report:
```bash
python -m pytest --cov=python_oops_project --cov-report=term
```

### HTML Report:
```bash
python -m pytest --cov=python_oops_project --cov-report=html
```
The HTML report will be generated in the htmlcov directory. Open htmlcov/index.html in your browser to view the detailed report.

### XML Report:
```bash
python -m pytest --cov=python_oops_project --cov-report=xml
```
The XML report will be saved as coverage.xml.
