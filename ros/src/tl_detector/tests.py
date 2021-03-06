import aug
import cv2
import net
import utils
import keras
import tensorflow as tf

print("Keras version: " + keras.__version__)
print("Tensorflow version: " + tf.__version__)

a = [0,1,2,3,4,5,6,7,8,9,"a","b","C","D"]
print(a)
b = utils.shuffle(a)
print(b)

c, d = utils.train_test_split(b, 0.2)

print(c)
print(d)


data1 = aug.DataClass(["test.jpg"], 3, True, label_str="Test1", label=2, label_hot = [0,0,1,0])
data2 = aug.DataClass(["test2.jpg"], 4, True, label_str="Test2", label=3, label_hot = [0,0,0,1])

set = aug.DataSet([data1, data2], 0.2, augment_validation=True)

print("Training: ")
training_set = set.get_training_set() #data1.get_elems_augmented()
for idx, aug in enumerate(training_set):
    print(str(idx) + ": " + aug.to_string())
    cv2.imwrite("out\\train_" + str(idx) + "-" + str(aug.label) + ".jpg", aug.get())

print("Validation: ")
validation_set = set.get_validation_set()
for idx, aug in enumerate(validation_set):
    print(str(idx) + ": " + aug.to_string())
    cv2.imwrite("out\\valid_" + str(idx) + "-" + str(aug.label) + ".jpg", aug.get())


lb = net.Labels(["A", "B", "C"])

for label in lb.labels:
    print(label.to_string())