# Written by @Rezwan Ghassemi



from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)
digits.target
digits.images[0]