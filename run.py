import numpy as np

# kNN classifier
# distance measure: Euclidean -> np.linalg.norm()

# model learning
def knn_classifier(train_input_dir, train_label_dir):

def predictions(point):

def run(train_input_dir, train_label_dir, test_input_dir, pred_file):
    train_data = np.loadtxt('Xtrain.csv', delimiter=",", dtype=float)
    train_label = np.loadtxt('Ytrain.csv', delimiter=",", dtype=int)
    test_data = np.loadtxt(test_input_dir, delimiter=",", dtype=float)
    knn_classifier(train_data, train_label)
    prediction = np.array([predictions(point) for point in test_data], dtype=object)
    np.savetxt(pred_file, prediction, fmt='%1d', delimiter=",")