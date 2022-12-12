# KNNClassifier

## run.py
Implements the K-Nearest Neighbors Classifier. K-Nearest Neighbors Classifier is a non-parametric, supervised learning model. It operates by calculating the distance of a test point to the rest of the points in the set, then finds the closest K neighbors. The class prediction of the point is a majority vote of the classes of the closest K neighbors. K-Nearest Neighbors has higher accuracy and is more robust when compared to 1-Nearest Neighbor.

## Xtrain.csv and Ytrain.csv
These are the training sets for the KNN Classifier and provide the format for any test sets. Rows in Xtrain.csv represent a point in vector form, columns represent feature dimensions. Each row in `Ytrain.csv` holds the ground truth label for each corresponding point in `Xtrain.csv` (either 0 or 1).
