# malaria-cell-detector
Malaria parasite identification on blood smear images. A simple implementation for college.

The Code segments the image into 3 parts: the parasite, the cell and the border. An image is also created with the segmented parts highlighted.

# Content

* [Dataset](#dataset)
* [Images](#images)
* [Dependencies](#dependencies)
* [How to run](#how-to-run)
* [Project structure](#project-structure)

# Dataset
A repository of segmented cells from the thin blood smear slide images.
[Click here to access the dataset page](https://lhncbc.nlm.nih.gov/LHC-downloads/downloads.html#malaria-datasets)

# Images
The images inside the `images` directory are sampled from the dataset, balanced with the same hue, to avoid threshold issues. It also contains two non-dataset images for testing with non-dataset images.

# Dependencies
In this project the implementation of opencv for python is used.

# How to run
To run the tests run at root:
`python test.py`

# Project structure

```bash
├── images // The images used in the tests
├── pipeline_segmentation.py // File with the sequence of segmentation algorithms
├── test.py // File to run the test
└── utils.py // File with utility functions
```