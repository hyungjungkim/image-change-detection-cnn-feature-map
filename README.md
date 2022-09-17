# CNN 특징맵을 이용한 이미지 변화 검출(image change detection using CNN feature maps)

## Idea
CNN은 입력 데이터의 형상 정보를 유지하면서 특징 추출이 가능하기 때문에 이미지의 차이 검출에도 사용이 가능해요.
특징 추출이 이루어지는 hidden layer에서 얻어지는 feature map은 깊이가 얕을수록(입력에 가까울수록) 이미지 자체의 형상 정보(spatial information)를 많이 포함하고 있고 깊이가 깊을수록(FC에 가까울수록) 의미적인 정보(semantic information)를 강하게 갖게 되죠.
이러한 특징을 이용하여 두 이미지의 형상적인 차이에 의미적인 차이를 혼합해서 살펴보면 이미지의 차이를 검출하는 것이 가능해요.
여기의 코드는 변화가 있는 두 이미지에 대해 대표적인 사전학습 모델인 VGG-19의 hidden layer 중 pooling layer에서 얻어지는 feature map들의 거리를 계산하여 두 이미지의 차이를 확인하는 예제예요.

CNN (Convolutional Neural Network), which can extract features while maintaining geometric information, can be used to change images’ detection.
Feature maps from hidden layers where feature extraction is processed contain more spatial information of an image in shallow depth (closer to input) and more semantic information of an image in deeper depth (closer to fully connected layers).
Using this point, we can detect changes in images by checking mixed spatial and semantic differences between two images.
The code in this repository shows an example of change detection of two images by calculating distances of feature maps of pooling layers from hidden layers of VGG-19, one of the most famous pre-trained CNN models.


![Sample image #1](/sample_image_1_1.jpg) ![Sample image #1](/sample_image_1_2.jpg)

![Change detection result compared with Absdiff from OpenCV](/result1.png)

## Reference
 - Arabi Mohammed El Amin, Qingjie Liu, Yunhong Wang, "Convolutional neural network features based change detection in satellite images," 2018.

 ## Related publication
 - Kim, H., Jung, W. K., Park, Y. C., Lee, J. W., & Ahn, S. H. (2022). Broken stitch detection method for sewing operation using CNN feature map and image-processing techniques. Expert Systems with Applications, 188, 116014. [[Link](https://doi.org/10.1016/j.eswa.2021.116014)]
