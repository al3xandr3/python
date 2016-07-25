from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]] #  [weight, texture(bumpy|smooth)]
labels = [0,0,1,1] # Orange=1, Apple=0
classifier = tree.DecisionTreeClassifier() # 
classifier = classifier.fit(features,labels)
print classifier.predict([[150,0]])