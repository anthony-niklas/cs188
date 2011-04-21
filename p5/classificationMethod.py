# classificationMethod.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

# This file contains the abstract class ClassificationMethod

class ClassificationMethod:
  """
  ClassificationMethod is the abstract superclass of 
   - MostFrequentClassifier
   - NaiveBayesClassifier
   - PerceptronClassifier
   - MiraClassifier
 
  As such, you need not add any code to this file.  You can write
  all of your implementation code in the files for the individual
  classification methods listed above.
  """
  def __init__(self, legalLabels):
    """
    For digits dataset, the set of legal labels will be 0,1,..,9
    For faces dataset, the set of legal labels will be 0 (non-face) or 1 (face)
    """
    self.legalLabels = legalLabels
    
    
  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    This is the supervised training function for the classifier.  Two sets of 
    labeled data are passed in: a large training set and a small validation set.
    
    Many types of classifiers have a common training structure in practice: using
    training data for the main supervised training loop but tuning certain parameters
    with a small held-out validation set.

    For some classifiers (naive Bayes, MIRA), you will need to return the parameters' 
    values after traning and tuning step.
    
    To make the classifier generic to multiple problems, the data should be represented
    as lists of Counters containing feature descriptions and their counts.
    """
    abstract
    
  def classify(self, data):
    """
    This function returns a list of labels, each drawn from the set of legal labels
    provided to the classifier upon construction.

    To make the classifier generic to multiple problems, the data should be represented
    as lists of Counters containing feature descriptions and their counts.
    """
    abstract

