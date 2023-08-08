# DVSOD-DViSal
This repository provides the DViSal dataset for DVSOD.

![avatar](https://github.com/DVSOD/DVSOD-DViSal/blob/main/introduction.png)  

**Introduction Figure**. Visual illustration of the advantages of employing RGBD videos for SOD. The last three columns exhibit the segmentation results achieved using different input modalities.

## Statistics

DViSal comprises 237 RGB-D videos at a frame rate of 25 f/s, including 175,442 RGB-D pairs in total and 7,117 annotated frames. In addition to providing conventional object-level annotations used in SOD tasks, DViSal also offers additional instance-level annotations, as well as weak annotations consisting of bounding boxes and scribbles, as displayed in the figure below.

![avatar](https://github.com/DVSOD/DVSOD-DViSal/blob/main/dataset.png)
**Dataset Figure**. Examples of the DViSal dataset. We provide diverse annotations, including fully-supervised object-/instance-level markings, as well as weakly-supervised scribbles and bounding boxes.

## Getting Started

Download the `DViSal` [dataset](https://drive.google.com/file/d/16tkVx1A_yaOEaVZOMdUpMb95nnXbY0QO/view?usp=sharing) (Google Drive), which is structured as follows:

```
DViSal_dataset/
├─ train.txt
├─ test_xxx.txt
├─ val.txt
│ ···
├─ data/
│  ├─ video1/
│  │  ├─ RGB/
│  │  │  ├─ 00000001.jpg
│  │  │  ├─ 00000002.jpg
│  │  ├─ Depth/
│  │  │  ├─ 00000001.png
│  │  ├─ GT/
│  │  │  ├─ 00000001.png
│  │  ├─ GT_edge/
│  │  │  ├─ 00000001.png
│  │  ├─ Instance/
│  │  │  ├─ 00000001.npy
│  │  ├─ Scribble/
│  │  │  ├─ 00000001.npy
│  │  ├─ BBox/
│  │  │  ├─ 00000001.txt
│  │
│  ├─ video2/
│  │  ├─ RGB/
···
```

Training/testing/validation splits can be found in `train.txt`, `test_xxx.txt` or `val.txt` which can be downloaded using the above [link](https://drive.google.com/file/d/16tkVx1A_yaOEaVZOMdUpMb95nnXbY0QO/view?usp=sharing) as well. (Note: Bounding boxes are saved in the format of ' x_min, y_min, x_max, y_max '.)

## Benchmark Results

The benchmark results in the paper can be accessed in this [link](https://drive.google.com/file/d/1WH6WLkRmnFaybgtS8vgWXnIwZ52xBqnQ/view?usp=sharing). This [evaluation tool](https://github.com/DVSOD/DVSOD-Evaluation) is used to measure all saliency results.

## Licence

The annotations provided in this dataset are licensed under a [GPL v3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text). This license can make sure that you have the freedom to copy and distribute copies of free source. Note that our annotations are released for non-commercial research purpose only.


