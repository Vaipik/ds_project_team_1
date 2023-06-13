### Here will be github actions
___

# Object Recognition Application
___

This is a final team project for `GoIT Python Data Science 7` online course.

This is an application that provides image recognition functionality. It allows users to upload an image and predicts the 
object category present in the image using a pre-trained machine learning model.
___
The task is to create and train a convolutional neural network capable of classifying an image given to it into one of
the 10 classes proposed in the `CIFAR-10` dataset.
___
## Features

- Accepts image uploads and predicts the object category.
- Handles exceptions related to invalid image files.
- Utilizes the FastAPI framework for building the web application.
- Uses TensorFlow and PIL libraries for image preprocessing and prediction.
- Provides a user-friendly API for integrating with other systems.

## Model Description

The application uses a pre-trained on `ImageNet` `EfficientNetV2B1` network with subsequent fine-tuning of the weights.
This network architecture was proposed in a paper [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298).
`EfficientNetV2B1` is a good fit for `CIFAR-10` as it combines good performance with a reasonable size of the network. 
As a result, we get a high accuracy score, no overfitting to the training data, and a small size of the final model.

To compensate for a smaller network size and achieve higher accuracy rates we used multitask learning. In particular, we added
two output layers atop of the base model - one for the label prediction and the other one for differentiation between
animals and non-animals. This combination made the confusion matrix much cleaner and reduced the number of misclassifications
drastically.

To prevent overfitting and make the network more robust to different quality of images, illumination, differences in position,
deformations of images we used data augmentation techniques. Moreover, we used labels smoothening to improve generalization
capabilities of the network.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Vaipik/ds_project_team_1.git
   cd ds_project_team_1
   ```
2. Change name env file and change value if need:

   ```bash
   sudo cp .env.env .env
   sudo nano .env #if need
   sudo rm .env.env
   ```

3. Run docker-compose file:

   ```bash
   sudo docker-compose up -d
   ```