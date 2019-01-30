import tensorflow as tf
import tensorflowjs as tfjs
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import TensorBoard

mnist = tf.keras.datasets.mnist  # 28x28 images of handwritten digits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)


def train():
    tensorboard = TensorBoard(log_dir='logs/learning-model')

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=x_train.shape[1:]))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=10, callbacks=[tensorboard])

    model.save('digit_model.h5')
    tfjs.converters.save_keras_model(model, 'target')
    return model


def test_model():
    new_model = tf.keras.models.load_model('digit_model')
    predictions = new_model.predict([x_test])

    print(np.argmax(predictions[0]))

    plt.imshow(x_test[0], cmap=plt.get_cmap('gray_r'))
    plt.show()


train()

# val_loss, val_acc = model.evaluate(x_test, y_test)
# print(val_loss, val_acc)

# plt.imshow(x_train[0], cmap=plt.get_cmap('gray_r'))
# plt.show()
