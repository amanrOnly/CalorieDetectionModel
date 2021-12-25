from keras.models import load_model
import tensorflow as tf

model=load_model("FCE_demo.h5.h5")

converter=tf.lite.TFLiteConverter.from_kera_model(model)
tflite_model=convereter.convert()

print("model converted")

with open('model.tflite','wb') as f:
    f.write(tflite_model)