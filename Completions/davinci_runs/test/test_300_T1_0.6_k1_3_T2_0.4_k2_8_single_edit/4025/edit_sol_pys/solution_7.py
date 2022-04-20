
#!/usr/bin/env python
# coding: utf-8
#
# Author:   Kazuto Nakashima
# URL:      http://kazuto1011.github.io
# Created:  2017-11-30
#
# Modified by: 
#

from __future__ import absolute_import, division, print_function

import os
import torch
import torch.nn.functional as F
import torch.utils.data as data
import torchvision.transforms as transforms

from PIL import Image
from tqdm import tqdm


class VOC2012ClassSeg(data.Dataset):
    """
    PASCAL VOC 2012 semantic segmentation dataset
    """

    _voc_root = "/home/kazuto1011/datasets/VOCdevkit/VOC2012/"
    _mask_dir = _voc_root + "SegmentationClass/"
    _image_dir = _voc_root + "JPEGImages/"

    def __init__(self, split="train", transform=None, target_transform=None):
        super(VOC2012ClassSeg, self).__init__()
        self.split = split
        self.transform = transform
        self.target_transform = target_transform

        _splits_dir = os.path.join(self._voc_root, "ImageSets/Segmentation")

        _split_f = os.path.join(
            _splits_dir,
            "train.txt" if self.split == "train" else "val.txt",
        )

        self.im_ids = []
        self.images = []
        self.masks = []

        with open(os.path.join(_split_f), "r") as f:
            lines = f.read().splitlines()

        for ii, line in tqdm(enumerate(lines), total=len(lines)):
            _image = os.path.join(self._image_dir, line + ".jpg")
            assert os.path.isfile(_image)
            self.im_ids.append(line)
            self.images.append(_image)
            if split != "test":
                _mask = os.path.join(self._mask_dir, line + ".png")
                assert os.path.isfile(_mask)
                self.masks.append(_mask)

    def __getitem__(self, index):
        _img, _target = self.make_img_gt_point_pair(index)
        sample = {'image': _img, 'label': _target}

        if self.transform is not None:
            sample = self.transform(sample)

        if self.target_transform is not None:
            sample["label"] = self.target_transform(sample["label"])

        return sample

    def __len__(self):
        return len(self.images)

    def make_img_gt_point_pair(self, index):
        _img = Image.open(self.images[index]).convert('RGB')
        if self.split == "test":
            return _img, os.path.basename(self.images[index])

        _target = Image.open(self.masks[index])

        return _img, _target


class VOC2012ClassSegInstance(VOC2012ClassSeg):
    """
    PASCAL VOC 2012 semantic segmentation dataset
    (with instance segmentation annotations)
    """

    _voc_root = "/home/kazuto1011/datasets/VOCdevkit/VOC2012/"
    _mask_dir = _voc_root + "SegmentationClass/"
    _image_dir = _voc_root + "JPEGImages/"

    def __init__(self, split="train", transform=None, target_transform=None):
        super(VOC2012ClassSegInstance, self).__init__(
            split, transform, target_transform
        )
        self._mask_dir = self._voc_root + "SegmentationObject/"

    def __getitem__(self, index):
        _img, _target = self.make_img_gt_point_pair(index)
        sample = {'image': _img, 'label': _target}

        if self.transform is not None:
            sample = self.transform(sample)

        if self.target_transform is not None:
            sample["label"] = self.target_transform(sample["label"])

        return sample


if __name__ == "__main__":
    from torch.utils.data import DataLoader
    import matplotlib.pyplot as plt
    import numpy as np

    voc_train = VOC2012ClassSegInstance(split="train")
    voc_val = VOC2012ClassSegInstance(split="val")
    voc_test = VOC2012ClassSegInstance(split="test")

    print("# train: {}".format(len(voc_train)))
    print("# val: {}".format(len(voc_val)))
    print("# test: {}".format(len(voc_test)))

    dataloader = DataLoader(voc_train, batch_size=4, shuffle=True, num_workers=4)

    for ii, sample in enumerate(dataloader):
        for jj in range(sample["image"].size()[0]):
            img = sample["image"].numpy()
            gt = sample["label"].numpy()
            tmp = np.array(gt[jj]).astype(np.uint8)
            segmap = decode_segmap(tmp, dataset='pascal')
            img_tmp = np.transpose(img[jj], axes=[1, 2, 0])
            img_tmp *= (0.229, 0.224, 0.225)
            img_tmp += (0.485, 0.456, 0.406)
            img_tmp *= 255.0
            img_tmp = img_tmp.astype(np.uint8)
            plt.figure()
            plt.title('display')
            plt.subplot(211)
            plt.imshow(img_tmp)
            plt.subplot(212)
            plt.imshow(segmap)

        if ii == 1:
            break

    plt.show(block=True)
