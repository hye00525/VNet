"""
Diogo Amorim, 2018-07-10
Evaluate Predictions - Vnet
"""

import h5py
import matplotlib.pyplot as plt
import numpy as np
import tkinter


def load_dataset(path, h5=True):
    #print("Loading dataset... Shape:")
    file = h5py.File(path, 'r')
    if h5:
        data = file.get('data')
        truth = file.get('truth')
    else:
        data = file.get('data').value
        truth = file.get('truth').value
    # print(data.shape)
    return data, truth

def load_predictions(path):
    path = path + 'predictions_vnet.h5'
    print("Loading predictions... Shape:")
    data = h5py.File(path, 'r')
    predictions = data.get('predictions').value
    print(predictions.shape)
    return predictions


def print_prediction(x_test, y_test, m, slice):
    plt.close()
    fig = plt.figure()
    x = fig.add_subplot(1, 2, 1)
    x.imshow(x_test[m, :, :, slice], cmap='gray')
    y = fig.add_subplot(1, 2, 2)
    y.imshow(y_test[m, :, :, slice], cmap='gray')
  #   y = fig.add_subplot(1, 2, 2)
  #  y.imshow(pred[m, :, :, slice], cmap='gray')
    plt.show()

'''
def print_prediction(x_test, y_test, m, slice):
    #plt.close()
    fig = plt.figure()
    i=1
    while(i<10):
        x = fig.add_subplot(10, 2, i)
        x.imshow(x_test[m, :, :, i], cmap='gray')
        y = fig.add_subplot(10, 2, i+1)
        y.imshow(y_test[m, :, :, i], cmap='gray')
        i=i+1
    plt.show()
'''
save_dir = "./dataset/"
test_dir = save_dir + "val_data.h5"

predictions = load_predictions(save_dir)
x_test, y_test = load_dataset(test_dir)
x_test = np.squeeze(np.array(np.split(x_test, 8, axis=0)))
y_test = np.squeeze(np.array(np.split(y_test, 8, axis=0)))

#print_prediction(y_test, predictions, 5, 10)
print_prediction(x_test, y_test, 5, 10)

key =0
i=0
def KeyClick(e):
    #plt.close()
    global key, i
    key = e.keysym

    print_prediction(x_test, y_test, 5, i)
    i = i + 1

tk = tkinter.Tk()

tk.bind("<Key>",KeyClick)
tk.mainloop()
