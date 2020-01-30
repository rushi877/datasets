# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for colorectal_histology dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import colorectal_histology

# testing/colorectal_histology.py generates fake input data

num_classes = len(colorectal_histology._CLASS_NAMES)  # pylint: disable=protected-access


class ColorectalHistologyTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = colorectal_histology.ColorectalHistology
  SPLITS = {
      "train": 2 * num_classes,
  }


class ColorectalHistologyS3Test(ColorectalHistologyTest):
  VERSION = "experimental_latest"


class ColorectalHistologyLargeTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = colorectal_histology.ColorectalHistologyLarge
  SPLITS = {
      "test": 1,
  }


class ColorectalHistologyLargeS3Test(ColorectalHistologyLargeTest):
  VERSION = "experimental_latest"


if __name__ == "__main__":
  testing.test_main()
