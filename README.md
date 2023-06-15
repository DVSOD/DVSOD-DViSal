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

## References

DViSal dataset is based on diverse video sources, including [CDTB](https://votchallenge.net/vot2019/dataset.html), [PTB](https://tracking.cs.princeton.edu/dataset.html), [People](http://www2.informatik.uni-freiburg.de/~spinello/RGBD-dataset.html), [Scene](https://rgbd-dataset.cs.washington.edu/dataset/rgbd-scenes-v2/), [DET](https://github.com/xiaozai/DeT), [Tracklam](http://tracklam.informatik.uni-freiburg.de/) and [Track3D](https://github.com/yjybuaa/Track-it-in-3D). They are annotated and adjusted to better fit the DVSOD task. If you use the DViSal dataset, the citations of seven source datasets mentioned are strongly recommended.

The annotations provided in this dataset are licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/). These annotations are released for non-commercial research purpose only.

```
@inproceedings{lukezic2019cdtb,
  title={Cdtb: A color and depth visual object tracking dataset and benchmark},
  author={Lukezic, Alan and Kart, Ugur and Kapyla, Jani and Durmush, Ahmed and Kamarainen, Joni-Kristian and Matas, Jiri and Kristan, Matej},
  booktitle={ICCV},
  pages={10013--10022},
  year={2019}
}
```
```
@inproceedings{song2013tracking,
  title={Tracking revisited using RGBD camera: Unified benchmark and baselines},
  author={Song, Shuran and Xiao, Jianxiong},
  booktitle={ICCV},
  pages={233--240},
  year={2013}
}
```
```
@inproceedings{spinello2011people,
  title={People detection in RGB-D data},
  author={Spinello, Luciano and Arras, Kai O},
  booktitle={IROS},
  pages={3838--3843},
  year={2011}
}
```
```
@inproceedings{lai2014unsupervised,
  title={Unsupervised feature learning for 3d scene labeling},
  author={Lai, Kevin and Bo, Liefeng and Fox, Dieter},
  booktitle={ICRA},
  pages={3050--3057},
  year={2014}
}
```
```
@inproceedings{yan2021depthtrack,
  title={Depthtrack: Unveiling the power of rgbd tracking},
  author={Yan, Song and Yang, Jinyu and K{\"a}pyl{\"a}, Jani and Zheng, Feng and Leonardis, Ale{\v{s}} and K{\"a}m{\"a}r{\"a}inen, Joni-Kristian},
  booktitle={ICCV},
  pages={10725--10733},
  year={2021}
}
```
```
@inproceedings{caselitz2020camera,
  title={Camera tracking in lighting adaptable maps of indoor environments},
  author={Caselitz, Tim and Krawez, Michael and Sundram, Jugesh and Van Loock, Mark and Burgard, Wolfram},
  booktitle={ICRA},
  pages={3334--3340},
  year={2020}
}
```
```
@inproceedings{yang2022towards,
  title={Towards Generic 3D Tracking in RGBD Videos: Benchmark and Baseline},
  author={Yang, Jinyu and Zhang, Zhongqun and Li, Zhe and Chang, Hyung Jin and Leonardis, Ale{\v{s}} and Zheng, Feng},
  booktitle={ECCV},
  pages={112--128},
  year={2022}
}
```
