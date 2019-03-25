# Compare Version Numbers

### Question Statement:

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

------------

For this question, I've assumed that a version number is represented as mentioned in https://semver.org/, which follows the format MAJOR.MINOR.PATCH with an optional pre-release (alpha/beta).

### How To Run:

```
$ python -m unittest tests/tests_compare_versions.py
```

Python version used: **Python 3.6.4**
