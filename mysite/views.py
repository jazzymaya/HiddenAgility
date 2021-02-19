from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

# Create your views here.
model = tf.keras.models.load_model('./models/NewSymcheckModel.h5')
class_names = ["Chickenpox", "Normal_Skin", "Normal_Eye", "PinkEye"]

def Imagepage(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fn = fs.save(uploaded_file.name, uploaded_file)
        fn = fs.url(fn)
        test_img = '.'+fn
        img = keras.preprocessing.image.load_img(
            test_img, target_size=(200, 200, 3)
        )
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
                .format(class_names[np.argmax(score)], 100 * np.max(score))
        )
        label = class_names[np.argmax(score)]
        confidence = 100 * np.max(score)
        request.session['lab'] = label
        request.session['con'] = confidence
        return redirect('Results')
    return render(request, 'Imagepage.html')


def Homepage(request):
    return render(request, 'Homepage.html')


def Results(request):
    label = request.session.get('lab')
    confidence = request.session.get('con')
    context = {'label': label, 'confidence': confidence}
    return render(request, 'Results.html', context)
