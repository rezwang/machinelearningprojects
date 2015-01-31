# By @Rezwan Ghassemi

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

# digits.data gives access to the features that can be used to classify the digits samples
print(digits.data)

#digits.target gives the ground truth for the digit dataset
print(digits.target)
print(digits.images[0])
