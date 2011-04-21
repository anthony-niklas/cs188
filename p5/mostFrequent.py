# mostFrequent.py
# ---------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod

class MostFrequentClassifier(classificationMethod.ClassificationMethod):
  """
  The MostFrequentClassifier is a very simple classifier: for
  every test instance presented to it, the classifier returns
  the label that was seen most often in the training data.
  """
  def __init__(self, legalLabels):
    self.guess = None
    self.type = "mostfrequent"
  
  def train(self, data, labels, validationData, validationLabels):
    """
    Find the most common label in the training data.
    """
    counter = util.Counter()
    counter.incrementAll(labels, 1)
    self.guess = counter.argMax()
  
  def classify(self, testData):
    """
    Classify all test data as the most common label.
    """
    return [self.guess for i in testData]
