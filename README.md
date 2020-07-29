# Udacity-Image-Classifiaction-project
There are two parts 1 in notebokk to create the model in part 2 we us ethe model using command line application 

## Image Classifier - Part 1 - Development
Developing an Image Classifier with Deep Learning
In this first part of the project, we will work through a Jupyter notebook to implement an image classifier with TensorFlow. 

## Image Classifier - Part 2 - Command Line App
Now that we will  built and trained a deep neural network on the flower data set, we will   convert it into an application that others can use. Our application should be a Python script that run from the command line. For testing, you should use the saved Keras model you saved in the first part.

Specifications
Predict.py file that uses a trained network to predict the class for an input image.

The predict.py module should predict the top flower names from an image along with their corresponding probabilities.

Basic usage:

$ python predict.py /path/to/image saved_model
Options:

--top_k : Return the top KK most likely classes:
$ python predict.py /path/to/image saved_model --top_k KK
--category_names : Path to a JSON file mapping labels to flower names:
$ python predict.py /path/to/image saved_model --category_names map.json
The best way to get the command line input into the scripts is with the argparse module in the standard library. You can also find a nice tutorial for argparse here.

Examples
For the following examples, we assume we have a file called orchid.jpg in a folder named/test_images/ that contains the image of a flower. We also assume that we have a Keras model saved in a file named my_model.h5.

Basic usage:

$ python predict.py ./test_images/orchid.jpg my_model.h5
Options:

Return the top 3 most likely classes:
$ python predict.py ./test_images/orchid.jpg my_model.h5 --top_k 3
Use a label_map.json file to map labels to flower names:
$ python predict.py ./test_images/orchid.jpg my_model.h5 --category_names label_map.json
Workspace
Install TensorFlow
We have provided a Command Line Interface workspace for you to run and test your code. Before you run any commands in the terminal make sure to install TensorFlow 2.0 and TensorFlow Hub using pip as shown below:

$ pip install -q -U "tensorflow-gpu==2.0.0b1"
$ pip install -q -U tensorflow_hub
Images for Testing
In the Command Line Interface workspace we have we have provided 4 images in the ./test_images/ folder for you to check your prediction.py module. The 4 images are:

cautleya_spicata.jpg
hard-leaved_pocket_orchid.jpg
orange_dahlia.jpg
wild_pansy.jpg

If we are using the workspace, be aware that saving large files can create issues with backing up our work. we 'll be saving a model checkpoint in Part 1 of this project which can be multiple GBs in size if you use a large classifier network. Dense networks can get large very fast since we are creating N x M weight matrices for each new layer. In general, it's better to avoid wide layers and instead use more hidden layers, this will save a lot of space. Keep an eye on the size of the checkpoint you create. You can open a terminal and enter ls -lh to see the sizes of the files. If your checkpoint is greater than 1 GB, reduce the size of your classifier network and re-save the checkpoint.
