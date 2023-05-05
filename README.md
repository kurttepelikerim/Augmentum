# Augmentum
A library for doing image augmentation

[![license badge - Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-brightgreen)](./LICENSE)
![image](https://img.shields.io/github/issues/kurttepelikerim/Augmentum)
[![codecov](https://codecov.io/gh/kurttepelikerim/Augmentum/branch/codecov/graph/badge.svg?token=D4K13TWGTK)](https://codecov.io/gh/kurttepelikerim/Augmentum)
[![Build Status](https://github.com/kurttepelikerim/Augmentum/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/kurttepelikerim/Augmentum/actions?query=workflow%3A%22Build+Status%22)

## Overview:
Augmentum is a library to apply many image augmentations and allow this via a simple interface. This library relies on other libraries and selects the augmentations and their parameters randomly from the sensible presets.

### Development and Contributions:
For development details and contribution instructions, please refer to the [contribution guidelines](https://github.com/kurttepelikerim/Augmentum/blob/main/CONTRIBUTING.md).

## Installation: 
First, install Python 3.7 (or later) and numpy, and then install this repo as a Python package. 

```bash
$ pip install numpy
$ pip install Augmentum
```

## Quick Start Example:
Below is a simple use-case for quick start:
    
```python
#given a image in the form of a square matrix (list of lists):
image_matrix = square_matrix = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]

#returns a list of images:
new_images = Augmentum.augment_image(image_matrix)
```
