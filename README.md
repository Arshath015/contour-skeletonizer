# CAD Blueprint Generator using Contour Skeletonization
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-4.6-blue.svg)
A submodule for generating CAD blueprints from furniture photos using computer vision techniques.
## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Case Studies](#case-studies)
* [Testing](#testing)
* [Limitations](#limitations)
* [Roadmap](#roadmap)
* [License](#license)
## Overview
This submodule uses contour detection and skeletonization to generate CAD blueprints from furniture photos.
## Tech Stack
* Python 3.10
* OpenCV 4.6
## Architecture
```
          +---------------+
          |  Input Image  |
          +---------------+
                  |
                  |
                  v
          +---------------+
          | Contour Detection|
          +---------------+
                  |
                  |
                  v
          +---------------+
          |  Skeletonization  |
          +---------------+
                  |
                  |
                  v
          +---------------+
          |  CAD Blueprint    |
          +---------------+
```
## Theoretical Background
The submodule uses the Zhang-Suen skeletonization algorithm to reduce the contours detected in the input image to a skeleton. This skeleton is then used to generate the CAD blueprint.
## Installation
To install the submodule, run the following commands:
```
pip install -r requirements.txt
git clone https://github.com/user/contour-skeletonizer.git
```
## Usage
To use the submodule, import the `ContourSkeletonizer` class and call the `generate_cad_blueprint` method:
```
from src.contour_skeletonizer import ContourSkeletonizer
skeletonizer = ContourSkeletonizer()
skeletonizer.generate_cad_blueprint('input_image.jpg')
```
## API Reference
* `ContourSkeletonizer` class:
  * `__init__` method: Initializes the contour skeletonizer.
  * `generate_cad_blueprint` method: Generates a CAD blueprint from an input image.
## Case Studies
See [case_studies/office_chair.md](case_studies/office_chair.md) for an example use case.
## Testing
See [tests/test_contour_skeletonizer.py](tests/test_contour_skeletonizer.py) for test cases.
## Limitations
The submodule currently only supports generating CAD blueprints for simple furniture pieces.
## Roadmap
* Improve the submodule to support more complex furniture pieces.
## License
MIT License