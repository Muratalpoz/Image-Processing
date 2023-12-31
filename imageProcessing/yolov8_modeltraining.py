# -*- coding: utf-8 -*-
"""YOLOv8 Tutorial adlı not defterinin kopyası

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O1sIJpn5XZo6mSkoFHj1SR6GYhV1zxpK

# Setup

Pip install `ultralytics` and [dependencies](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) and check software and hardware.
"""

from google.colab import drive

drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %pip install ultralytics
from IPython.display import Image
import ultralytics
ultralytics.checks()

cd /content/drive/MyDrive/head_dataset

# Commented out IPython magic to ensure Python compatibility.
#@title Select YOLOv8 🚀 logger {run: 'auto'}
logger = 'Comet' #@param ['Comet', 'TensorBoard']

if logger == 'Comet':
#   %pip install -q comet_ml
  import comet_ml; comet_ml.init()
elif logger == 'TensorBoard':
#   %load_ext tensorboard
#   %tensorboard --logdir .

# Train YOLOv8n on COCO8 for 3 epochs
!yolo train model=yolov8n.pt data=/content/drive/MyDrive/head_dataset/data.yaml epochs=20 imgsz=640

Image(filename=f'/content/drive/MyDrive/head_dataset/runs/detect/train/results.png', width=600)

"""# 2. Val
Validate a model's accuracy on the [COCO](https://docs.ultralytics.com/datasets/detect/coco/) dataset's `val` or `test` splits. The latest YOLOv8 [models](https://github.com/ultralytics/ultralytics#models) are downloaded automatically the first time they are used. See [YOLOv8 Val Docs](https://docs.ultralytics.com/modes/val/) for more information.
"""

# Download COCO val
import torch
torch.hub.download_url_to_file('https://ultralytics.com/assets/coco2017val.zip', 'tmp.zip')  # download (780M - 5000 images)
!unzip -q tmp.zip -d datasets && rm tmp.zip  # unzip

# Validate YOLOv8n on COCO8 val
!yolo val model=/content/drive/MyDrive/head_dataset/runs/detect/train/weights/best.pt data=data.yaml

"""# 1. Predict

YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo` command for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See a full list of available `yolo` [arguments](https://docs.ultralytics.com/usage/cfg/) and other details in the [YOLOv8 Predict Docs](https://docs.ultralytics.com/modes/train/).

"""

# Run inference on an image with YOLOv8n
!yolo predict model=/content/drive/MyDrive/head_dataset/runs/detect/train/weights/best.pt source='/content/drive/MyDrive/head_dataset/test/images'

import glob
from IPython.display import Image

for image_path in glob.glob(f'/content/drive/MyDrive/head_dataset/runs/detect/predict2/*.jpg'):
    display(Image(filename=image_path, height=600))
    print("\n")