# import cv2
import tensorflow as tf
import tensorflow_hub as hub 
import json
import numpy as np
from PIL import  Image
import argparse

#define some functions 
topk = 5
def categories(jsonfile):#read all caregories of classes in json file and copy it in new dict new_categories
    with open(jsonfile, 'r') as f:
        old_categories =json.load(f)
    new_categories = {}
    for i in old_categories:
        new_categories[str(int(i)-1)] = old_categories[i]
    return new_categories

#Preproccesing of image cz image has diff size and shape but in traing our model nd output we give a fixes size
def prepare(image_file_path):
    image_size = 224
    img = Image.open(image_file_path)
    image_file = np.asarray(img)
    tf_tensor_image = tf.image.convert_image_dtype(image_file, dtype=tf.int16, saturate=False)
    resize_imgage = tf.image.resize(tf_tensor_image,(image_size,image_size)).numpy()
    img = resize_imgage/255
    return img

#main function Pridict_new_image which is load our model do prediction and return it for given image path
def predict_new_images(image_path,my_model_path, topk,classes_file):
    topk = int(topk)
    tf.keras.backend.clear_session()
    model = tf.keras.models.load_model(my_model_path, custom_objects={'KerasLayer':hub.KerasLayer})
    print(model.summary())

    new_categories = categories(classes_file)
    new_array_categories = np.array(list(new_categories.items()))
    
    image = prepare(image_path)
    prediction = model.predict(np.expand_dims(image,axis=0))
    prediction = prediction[0].tolist()
    prediction_classes = model.predict_classes(np.expand_dims(image,axis=0))
    prediction_classes_prob = prediction[prediction_classes[0]]
    prediction_cls = new_categories[str(prediction_classes[0])]
    print("-"*60)
    print("\nACcording to our Model Most likely class image is :{}\n  it's probability :{} ".format(prediction_cls ,prediction_classes_prob))
    print("-"*60)
    val, indices= tf.math.topk(prediction, k=topk)
    prediction_topk = val.numpy().tolist()
    prediction_classes_topk = indices.numpy().tolist()
    print("-"*60)
    print("top ",topk,"Predictions :",prediction_topk)
    print("top ",topk," Predictons classes :",prediction_classes_topk)
    print("-"*60)
    Prediction_class_label = [new_categories[str(i)] for i in prediction_classes_topk]
    print('top k class labels:',Prediction_class_label)
    print("-"*60)
    prediction_class_topk_prob = dict(zip(Prediction_class_label, prediction_topk))
    print("\nTop ",topk," classes along with associated probabilities according to given model :-\n",class_prob_dict)


''' # this is just for testing our function 
my_model_path = "ImageClassifierTrainedModel.h5"
image_path = "wild_pansy.jpg" 
topk = 5
classes_file = "label_map.json"
predict_new_images(image_path,my_model_path,topk,classes_file)
'''
# call all the function nd use argparse library for make a command line applicaton of this model of image classification
 

if __name__ == "__main__":
    keyword = argparse.ArgumentParser(description="Process a Machine learning model")
    keyword.add_argument("image_path",help="Path where You save Your Image ", default="")
    keyword.add_argument("my_model_path",help="Path Where You save Your Model", default="")
    keyword.add_argument("--topk", help="Fetch top k predictions (Chances to top k possible solution for image)", required = False, default = 5)
    keyword.add_argument("--classes_file", help="Class map json file(Path where is Your Json file ", required = False, default = "label_map.json")
    args = keyword.parse_args()
    predict_new_images(args.image_path,args.my_model_path,args.topk,args.classes_file)