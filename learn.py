from train_test_csv_read import *

myML = svm.SVC(kernel="linear")
myML.fit(X_train,Y_train)

train_prediction = myML.predict(X_train)
training_accuracy = accuracy_score(train_prediction, Y_train)
print('Training Accuracy  : ', training_accuracy*100)

test_prediction = myML.predict(X_test)
test_accuracy = accuracy_score(test_prediction, Y_test)
print('Testing Accuracy  : ', test_accuracy*100)