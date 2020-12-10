import tensorflow as tf
import keras
from keras.applications.vgg19 import VGG19, preprocess_input
from keras.models import Model
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def preprocess_image_VGG19(img_path):
    img = image.load_img(img_path, target_size=(244, 244))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)

    return preprocess_input(img_data)

def get_layer_features(base_model, layer_name, input_data):
    model = Model(inputs=base_model.input, outputs=base_model.get_layer(layer_name).output)

    return model.predict(input_data)
    
def extract_features(img_path):
    base_model = VGG19(weights='imagenet', include_top=False)
    
    img_data = preprocess_image_VGG19(img_path)

    block1_pool_features = get_layer_features(base_model, 'block1_pool', img_data)
    block2_pool_features = get_layer_features(base_model, 'block2_pool', img_data)
    block3_pool_features = get_layer_features(base_model, 'block3_pool', img_data)
    block4_pool_features = get_layer_features(base_model, 'block4_pool', img_data)
    block5_pool_features = get_layer_features(base_model, 'block5_pool', img_data)

    fmap1 = tf.image.resize(block1_pool_features, [224,224])
    fmap2 = tf.image.resize(block2_pool_features, [224,224])
    fmap3 = tf.image.resize(block3_pool_features, [224,224])
    fmap4 = tf.image.resize(block4_pool_features, [224,224])
    fmap5 = tf.image.resize(block5_pool_features, [224,224])

    return tf.concat([fmap1, fmap2, fmap3, fmap4, fmap5], 3)

if __name__ == '__main__':
    image1_path = 'sample_image_1_1.jpg'
    image2_path = 'sample_image_1_2.jpg'

    features1 = extract_features(image1_path)
    features2 = extract_features(image2_path)
    
    diff = tf.subtract(features1, features2)
    d_square = tf.square(diff)
    d_square_sum = tf.reduce_sum(d_square, axis=3)
    dist = tf.sqrt(d_square_sum)
    dist = dist.numpy()
    dist = np.resize(dist, [224,224])

    norm_dist = (dist - np.min(dist)) / (np.max(dist) - np.min(dist))
    
    img1 = mpimg.imread(image1_path)
    img2 = mpimg.imread(image2_path)

    absdiff = cv2.absdiff(img1, img2)

    plt.subplot(141)
    plt.imshow(img1)
    plt.subplot(142)
    plt.imshow(img2)
    plt.subplot(143)
    plt.imshow(absdiff)
    plt.subplot(144)
    plt.imshow(norm_dist)
    plt.show()