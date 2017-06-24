# unittest boilerplate [![Build Status](https://travis-ci.org/pedro2555/unittest-boilerplate.svg?branch=master)](https://travis-ci.org/pedro2555/unittest-boilerplate)

A super simple boilerplate on python unittest, this is mainly for me to get start at it

## Getting Started

Import the project files with `git clone` in a folder of choice.

If your using this on another project, make sure to check `setup.py` attributes to match your project

### Running the Tests

To run all your tests in one go:

`python setup.py test`

Or, to run a single test:

`python -m unittest tests.source.sample_source_test.SampleSource_test.test_IsEven`

### Linting

You can also lint your code with:

`python setup.py lint`
