"""Keras implementation of SSD."""

import keras.backend as K
from keras.layers import Activation
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import GlobalAveragePooling2D
from keras.layers import Input
from keras.layers import MaxPool2D
from keras.layers import concatenate
from keras.layers import Reshape
from keras.layers import ZeroPadding2D
from keras.models import Model

from ssd_layers import Normalize


def ssd300_body(x):
    
    source_layers = []
    
    # Block 1
    x = Conv2D(64, 3, strides=1, padding='same', name='conv1_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(64, 3, strides=1, padding='same', name='conv1_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool1')(x)
    # Block 2
    x = Conv2D(128, 3, strides=1, padding='same', name='conv2_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(128, 3, strides=1, padding='same', name='conv2_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool2')(x)
    # Block 3
    x = Conv2D(256, 3, strides=1, padding='same', name='conv3_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 3, strides=1, padding='same', name='conv3_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 3, strides=1, padding='same', name='conv3_3', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool3')(x)
    # Block 4
    x = Conv2D(512, 3, strides=1, padding='same', name='conv4_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv4_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv4_3', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool4')(x)
    # Block 5
    x = Conv2D(512, 3, strides=1, padding='same', name='conv5_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv5_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv5_3', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=3, strides=1, padding='same', name='pool5')(x)
    # FC6
    x = Conv2D(1024, 3, strides=1, dilation_rate=(6, 6), padding='same', name='fc6', activation='relu')(x)
    #x = Activation('relu')(x)
    # x = Dropout(0.5, name='drop6')(x)
    # FC7
    x = Conv2D(1024, 1, strides=1, padding='same', name='fc7', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # x = Dropout(0.5, name='drop7')(x)
    
    # Block 6
    x = Conv2D(256, 1, strides=1, padding='same', name='conv6_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=2, padding='same', name='conv6_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # Block 7
    x = Conv2D(128, 1, strides=1, padding='same', name='conv7_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = ZeroPadding2D((1,1))(x)
    x = Conv2D(256, 3, strides=2, padding='valid', name='conv7_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # Block 8
    x = Conv2D(128, 1, strides=1, padding='same', name='conv8_1', activation='relu')(x)
    #x = Activation('relu')(x)
    #conv8_1 = ZeroPadding2D(((1,1),(1,1)))(x) # (top, bottom), (left, right) TODO ????
    x = Conv2D(256, 3, strides=2, padding='same', name='conv8_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # Block 9
    x = Conv2D(128, 1, strides=1, padding='same', name='conv9_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 3, strides=2, padding='valid', name='conv9_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    
    return source_layers


def ssd512_body(x):
    
    source_layers = []
    
    # Block 1
    x = Conv2D(64, 3, strides=1, padding='same', name='conv1_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(64, 3, strides=1, padding='same', name='conv1_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool1')(x)
    # Block 2
    x = Conv2D(128, 3, strides=1, padding='same', name='conv2_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(128, 3, strides=1, padding='same', name='conv2_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool2')(x)
    # Block 3
    x = Conv2D(256, 3, strides=1, padding='same', name='conv3_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 3, strides=1, padding='same', name='conv3_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 3, strides=1, padding='same', name='conv3_3', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool3')(x)
    # Block 4
    x = Conv2D(512, 3, strides=1, padding='same', name='conv4_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv4_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv4_3', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    x = MaxPool2D(pool_size=2, strides=2, padding='same', name='pool4')(x)
    # Block 5
    x = Conv2D(512, 3, strides=1, padding='same', name='conv5_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv5_2', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(512, 3, strides=1, padding='same', name='conv5_3', activation='relu')(x)
    #x = Activation('relu')(x)
    x = MaxPool2D(pool_size=3, strides=1, padding='same', name='pool5')(x)
    # FC6
    x = Conv2D(1024, 3, strides=1, dilation_rate=(6, 6), padding='same', name='fc6', activation='relu')(x)
    #x = Activation('relu')(x)
    # x = Dropout(0.5, name='drop6')(x)
    # FC7
    x = Conv2D(1024, 1, strides=1, padding='same', name='fc7', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # x = Dropout(0.5, name='drop7')(x)
    
    # Block 6
    x = Conv2D(256, 1, strides=1, padding='same', name='conv6_1', activation='relu')(x)
    #x = Activation('relu')(x)
    #x = ZeroPadding2D()(x)
    x = Conv2D(512, 3, strides=2, padding='same', name='conv6_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # Block 7
    x = Conv2D(128, 1, strides=1, padding='same', name='conv7_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = ZeroPadding2D()(x)
    x = Conv2D(256, 3, strides=2, padding='valid', name='conv7_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # Block 8
    x = Conv2D(128, 1, strides=1, padding='same', name='conv8_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 3, strides=2, padding='same', name='conv8_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # Block 9
    x = Conv2D(128, 1, strides=1, padding='same', name='conv9_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 3, strides=2, padding='same', name='conv9_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    # Block 10 
    x = Conv2D(128, 1, strides=1, padding='same', name='conv10_1', activation='relu')(x)
    #x = Activation('relu')(x)
    x = Conv2D(256, 4, strides=2, padding='same', name='conv10_2', activation='relu')(x)
    #x = Activation('relu')(x)
    source_layers.append(x)
    
    return source_layers


def multibox_head(source_layers, num_priors, num_classes, normalizations=None):

    postfix = '' if num_classes == 21 else '_%i'%num_classes

    mbox_conf = []
    mbox_loc = []
    for i in range(len(source_layers)):
        x = source_layers[i]
        name = x.name.split('/')[0]
        
        # normalize
        if normalizations is not None and normalizations[i] > 0:
            name = name + '_norm'
            x = Normalize(normalizations[i], name=name)(x)
            
        # confidence
        name1 = name + '_mbox_conf' + postfix
        x1 = Conv2D(num_priors[i] * num_classes, 3, padding='same', name=name1)(x)
        x1 = Flatten(name=name1+'_flat')(x1)
        mbox_conf.append(x1)

        # location
        name2 = name + '_mbox_loc' + postfix
        x2 = Conv2D(num_priors[i] * 4, 3, padding='same', name=name2)(x)
        x2 = Flatten(name=name2+'_flat')(x2)
        mbox_loc.append(x2)

    mbox_loc = concatenate(mbox_loc, axis=1, name='mbox_loc')
    mbox_loc = Reshape((-1, 4), name='mbox_loc_final')(mbox_loc)

    mbox_conf = concatenate(mbox_conf, axis=1, name='mbox_conf')
    mbox_conf = Reshape((-1, num_classes), name='mbox_conf_logits')(mbox_conf)
    mbox_conf = Activation('softmax', name='mbox_conf_final')(mbox_conf)

    predictions = concatenate([mbox_loc, mbox_conf], axis=2, name='predictions')
    
    return predictions


def SSD300(input_shape=(300, 300, 3), num_classes=21):
    """SSD300 architecture.

    # Arguments
        input_shape: Shape of the input image.
        num_classes: Number of classes including background.
    
    # Notes
        In order to stay compatible with pre-trained models, the parameters 
        were chosen as in the caffee implementation.
    
    # References
        https://arxiv.org/abs/1512.02325
    """
    K.clear_session()
    
    x = input_tensor = Input(shape=input_shape)
    source_layers = ssd300_body(x)
    
    # Add multibox head for classification and regression
    num_priors = [4, 6, 6, 6, 4, 4]
    normalizations = [20, -1, -1, -1, -1, -1]
    output_tensor = multibox_head(source_layers, num_priors, num_classes, normalizations)
    model = Model(input_tensor, output_tensor)

    # parameters for prior boxes
    model.image_size = input_shape[:2]
    model.source_layers = source_layers
    model.source_layers_names = ['conv4_3', 'fc7', 'conv6_2', 'conv7_2', 'conv8_2', 'conv9_2']
    # stay compatible with caffe models
    model.aspect_ratios = [[1,2], [1,2,3], [1,2,3], [1,2,3], [1,2], [1,2]]
    model.minmax_sizes = [(30, 60), (60, 111), (111, 162), (162, 213), (213, 264), (264, 315)]
    model.steps = [8, 16, 32, 64, 100, 300]
    
    return model


def SSD512(input_shape=(512, 512, 3), num_classes=21):
    """SSD512 architecture.

    # Arguments
        input_shape: Shape of the input image.
        num_classes: Number of classes including background.
    
    # Notes
        In order to stay compatible with pre-trained models, the parameters 
        were chosen as in the caffee implementation.
    
    # References
        https://arxiv.org/abs/1512.02325
    """
    K.clear_session()
    
    x = input_tensor = Input(shape=input_shape)
    source_layers = ssd512_body(x)
    
    # Add multibox head for classification and regression
    num_priors = [4, 6, 6, 6, 6, 4, 4]
    normalizations = [20, -1, -1, -1, -1, -1, -1]
    output_tensor = multibox_head(source_layers, num_priors, num_classes, normalizations)
    model = Model(input_tensor, output_tensor)

    # parameters for prior boxes
    model.image_size = input_shape[:2]
    model.source_layers = source_layers
    model.source_layers_names = ['conv4_3', 'fc7', 'conv6_2', 'conv7_2', 'conv8_2', 'conv9_2', 'conv10_2']
    # stay compatible with caffe models
    model.aspect_ratios = [[1,2], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2], [1,2]]
    model.minmax_sizes = [(35, 76), (76, 153), (153, 230), (230, 307), (307, 384), (384, 460), (460, 537)]
    model.steps = [8, 16, 32, 64, 128, 256, 512]
    
    return model
