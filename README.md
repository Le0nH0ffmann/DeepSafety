# DeepSafety
This is a repository to study safety concepts for deep learning perception applications at Ravensburg-Weingarten University.

## The Codebase
### kickstart.py
Provides an initial pipeline, supporting pretrained models, data loading from directory and a train / validation split, preprocessing steps, tensorboard support, the model training pipeline, and save capabilities for training logs and the final model. The script is an adaptation from [here](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)

### requirements.txt
Running python == 3.9, the crucial imports are
'''
numpy==1.21.2
tensorflow==2.7.0
tensorflow-hub==0.12.0
tensorboard==2.6.0
'''

### Data
The data to train and validate the model we will be using initially can be downloaded [here](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/download)
The data enables you to train a neural network for traffic sign recognition - we assume that the final goal is to use this model in an autonomous vehicle - meaning the system will not have any form of human intervention or supervision at any point.

## Safety and Attacks
During the lecture you will be tasked with providing a safety strategy for your deep learning application.
To make things spicy, you will be asked to validate your model on data that you will not know beforehand.
Your goal is to prepare yourself for these data ingests. 
Preparing includes acting and documenting on:
- An elaborate validation pipeline for your model, with the goal to precisely describe the functionality of your model
- An elaborate safety concept, including roles and processes on hazzard and risk assessment 
- At some point you will need to implement and decide on a safety architecture


### Contact
mark.schutera@gmail.com
feel free to connect
