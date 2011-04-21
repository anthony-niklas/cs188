# minicontest.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod

class contestClassifier(classificationMethod.ClassificationMethod):
  """
  Create any sort of classifier you want. You might copy over one of your
  existing classifiers and improve it.
  """
  def __init__(self, legalLabels):
    self.guess = None
    self.type = "minicontest"
  
  def train(self, data, labels, validationData, validationLabels):
    """
    Please describe your training procedure here.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
  
  def classify(self, testData):
    """
    Please describe how data is classified here.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
