### Here will be github actions
___

# Object Recognition Application
___

This is a final team project for `GoIT Python Data Science 7` online course.

This is an application that provides image recognition functionality. It allows users to upload an image and predicts the object category present in the image using a pre-trained machine learning model.
___
The task is to create and train a convolutional neural network capable of classifying an image given to it into one of
the 10 classes proposed in the dataset `CIFAR-10`
___
## Features

- Accepts image uploads and predicts the object category.
- Handles exceptions related to invalid image files.
- Utilizes the FastAPI framework for building the web application.
- Uses TensorFlow and PIL libraries for image preprocessing and prediction.
- Provides a user-friendly API for integrating with other systems.

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