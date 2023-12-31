# -*- coding: utf-8 -*-
"""FirstNeuralNetwork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A8V-uW1kKcIh61M5u0POEZR38fxB5JPx
"""

'''This Neural Netwrok converts Celsius to Farenheit'''
import tensorflow as tf
import numpy as np

#Array of Farenheit values to train
celsius = np.array([-40,-10,0,8,15,22,38], dtype = float)
# Array of Celsius Values to train
farenheit = np.array([-40, 14, 32, 46, 59,72,100], dtype = float)

'''Dense layer but we just have 2 neurons
Dense(number of neurons, input neuron number)'''
#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#Model used: sequential
#modelo = tf.keras.Sequential([capa])
#****************************************
#**********Model with 2 hidden layers with 3 neurons
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

#Model optimizer and loss function
modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entenamiento....")
#Fit function (input data, expected data, number of epochs)
historial = modelo.fit(celsius, farenheit, epochs = 1000, verbose=False)
print("Modelo entrenado")

import matplotlib.pyplot as plt
plt.xlabel("# epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

print("Hagamos una predicción")
resultado = modelo.predict([100.0])
# 100 Celsiud should be 212 Farenheit
print(f"El resultado es: {resultado} farenheit!")

print("variables internas del modelo")
#print(capa.get_weights())
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())