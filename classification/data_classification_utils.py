import numpy as np
import math
import util
import matplotlib.pyplot as plt
from util import raiseNotDefined


def display_digit_features(weights, bias):
    """Visualizes a set of weight vectors for each digit.
        Do not modify this code."""
    feature_matrices = []
    for i in range(10):
      feature_matrices.append(convert_weight_vector_to_matrix(weights[:, i], 28, 28, bias))

    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.imshow(feature_matrices[i], cmap='gray')
        
    plt.show()

def apply_bias(samples):
    """
    samples: The samples under test, should be a numpy array of shape (numSamples, numFeatures).
    Mutates samples to add a bias term to each feature vector. This example appends a 1 to
    the front, but the bias term could be added anywhere.

    Do not modify this code."""
    return np.hstack([samples, np.ones((len(samples), 1))])

def simple_image_featurization(image):
    """Converts an image to a numpy vector of shape (1, w * h), where w is the
        width of the image, and h is the height."""

    """YOUR CODE HERE"""

    arr = np.array([image.getPixels()])
    return arr.flatten('F')

    # return vec
def zero_one_loss_ss(classifier, sample, label):
    """
    classifier: The classifier under test.
    sample: The sample under test, should be a numpy array of shape (1, numFeatures).
    label: The correct label of the sample under test.

    Returns 0.0 if the classifier classifies the sample correctly, or 1.0 otherwise."""

    """YOUR CODE HERE"""
    result = classifier.classify(sample)
    # print 'label: ', label
    # print 'result: ', result
    if result == label:
        return 0.0
    return 1.0

def zero_one_loss(classifier, samples, labels):
    """
    classifier: The classifier under test.
    sample: The samples under test, should be a numpy array of shape (numSamples, numFeatures).
    label: The correct labels of the samples under test.

    Returns the fraction of samples that are wrong. For example, if the classifier gets
    65 out of 100 samples right, this function should return 0.35."""

    """YOUR CODE HERE"""
    num = 0.0
    for i in range(len(samples)):
        result = classifier.classify(samples[i])
        if result != labels[i]:
            num += 1.0
    # print 'ans: ', 1.0 - nfum / len(samples)
    return 1.0 - num / len(samples)



def convert_weight_vector_to_matrix(weight_vector, w, h, bias):
    """weight_vector: The weight vector to transformed into a matrix.
    w: the width of the matrix
    h: the height of the matrix
    bias: whether or not there is a bias feature

    Returns a w x h array where the first w entries of the weight vector for this label correspond to the
    first row, the next w the next row, and so forth. Assume that w * h is equal to the size of the
    weight vector. Ignore the bias if there is one"""

    """YOUR CODE HERE"""
    # print 'weight: ', weight_vector
    # print 'shape: ', np.shape(weight_vector)
    # print 'w: ', w
    # print 'h: ', h

    return np.reshape(weight_vector, (w, h))