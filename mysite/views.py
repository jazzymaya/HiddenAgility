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

def NewHomepage(request):
    return render(request,'NewHome.html')

def NewUploadpage(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fn = fs.save(uploaded_file.name, uploaded_file)
        fn = fs.url(fn)
        testimg = '.'+fn
        img = keras.preprocessing.image.load_img(
            testimg, target_size=(200, 200, 3)
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
        
        return redirect('Advanced')
        
    return render(request, 'NewUpload.html')

def NewFAQpage(request):
    return render(request,'NewFAQ.html')

def NewAboutUspage(request):
    return render(request,'NewAboutUs.html')
    
def NewResultspage(request):
    label = request.session.get('lab')
    confidence = request.session.get('con')

    about = " "
    doc = " "
    
    if label == 'Chickenpox':
        about = """Chickenpox is a highly contagious disease caused by the varicella-zoster virus (VZV). It can cause an itchy, blister-like rash. The rash first appears on the chest, back, and face, and then spreads over the entire body, causing between 250 to 500 itchy blisters. Chickenpox can be serious, especially in babies, adolescents, adults, pregnant women, and people with weakened immune systems. The best way to prevent chickenpox is to be innoculated with the chickenpox vaccine.
                            Chickenpox used to be very common in the United States. In the early 1990s, an average of 4 million people contracted chickenpox; 10,500 to 13,000 were hospitalized, and 100 to 150 died each year.
                            A vaccine for Chickenpox became available in the United States in 1995. Each year, more than 3.5 million cases of chickenpox, 9,000 hospitalizations, and 100 deaths are prevented by the chickenpox vaccination in the United States.
                             For more information, check out the https://www.cdc.gov/chickenpox/about/index.html CDC website concerning Chickenpox."""
        doc = """If you or your child does end up having chickenpox, treatment isn't always necessary, especially when cases are mild.
                        However, the CDC recommends getting medical attention if you are at higher risk of having complications, including those who:\n
                            Are pregnant, immunocompromised,younger than the age of 1 or older than 12 years old, since chickenpox can be more severe and show complications in adults
                             
                        """
    elif label == "PinkEye":
        about = """Conjunctivitis, also known as Pink eye, is an inflammation of the conjunctiva. The conjunctiva is the thin clear tissue that lies over the white part of the eye and lines the inside of the eyelid.
                                 The illness is most common in children. And it can be highly contagious (it spreads rapidly in schools and daycares), but it’s rarely found to be serious. It's very unlikely to damage one's vision, especially if diagnosed and treated quickly. When you take care to prevent its spread and follow all healthcare recommendations, Pink eye clears up with no long-term issues.
                                 For more information, check out the <a href ="https://www.cdc.gov/conjunctivitis/index.html">CDC website</a> concerning Pink eye."""
        doc = """Although most cases of pink eye go away without medical care, there are some instances where one should see a doctor as soon as possible for any symptoms. Your doctor may prescribe eye drops to help relieve the symptoms, or to treat bacterial conjunctivitis. Times when you should see a doctor for Pink eye include:
                            If you have a depressed or weakened immune system, making it harder to fight infections;
                            You develop pain in one or both eyes;
                            You develop a sensitivity to light;
                            Your vision becomes blurry;
                            Your symptoms persist or worsen;
                            You are using antibiotic drops for a bacterial infection and the symptoms are not going away;
                            You develop a fever or other signs of an infection, such as swollen glands or fatigue;
                            You have an eye condition unrelated to conjunctivitis.
                        """
    elif label == "Normal_Skin":
        about = """Algorithm concluded that no visual injury or illness is found on the skin visible in the image."""
        doc = """As stated above, it appears that the skin is normal. However, if you are experiencing any of the following symptoms you may wish to seek help from a medical professional:
                            Burning/itching sensation,
                            Numbness,
                            Acute Pain with or without stimuli.
                        """
    elif label == "Normal_Eye":
        about = """Algorithm concluded that no visual injury or illness is found on the skin visible in the image."""
        doc = """As stated above, it appears that the eye is normal. However, if you are experiencing any of the following symptoms you may wish to seek help from a medical professional:
                            Extreme pressure,
                            Acute pain,
                            Flashes,
                            Tubular vision (also known a Tunnel vision where one experiences a loss of peripheral vision),
                            Visual Snow (Or Visual Static).
                        """
    else:
        about = """Your session has been lost. Please click on the "New Diagnosis" button and resubmit your image for a proper diagnosis!"""  
    
    
    
    context = {'label': label, 'confidence': confidence, 'about': about, 'doc': doc}

    return render(request, 'NewResults.html', context)

def Advanced(request):
    
        label = request.session.get('lab')
        confidence = request.session.get('con')

        context = {'label': label, 'confidence': confidence}

        if label == "Chickenpox" or label == "Normal_Skin":

            return render(request, 'AdvancedChickenpox.html', context)

        elif label == "PinkEye" or label == "Normal_Eye":

            return render(request, 'AdvancedPinkeye.html', context)
    
def AdvancedChickenpox(request):
    
        label = request.session.get('lab')
        confidence = request.session.get('con')
        about = " "
        doc = " "

        Oconfidence = confidence

        q1c= request.POST['q1c']
        q2c= request.POST['q2c']
        q3c= request.POST['q3c']
        q4c= request.POST['q4c']

        if q1c == "0":
            confidence = confidence + (Oconfidence * 0.1) 
        elif q1c == "1":
                confidence = confidence - (Oconfidence * 0.5)
        
        if q2c == "1":
            confidence = confidence + (Oconfidence * 0.1)
            
        if q3c == "1":
            confidence = confidence + (Oconfidence * 0.1)
        
        if q4c == "1":
            confidence = confidence + (Oconfidence * 0.1)
        
        if confidence > 100:
            confidence = 100
    
        if label == 'Chickenpox':
            about = """Chickenpox is a highly contagious disease caused by the varicella-zoster virus (VZV). It can cause an itchy, blister-like rash. The rash first appears on the chest, back, and face, and then spreads over the entire body, causing between 250 to 500 itchy blisters. Chickenpox can be serious, especially in babies, adolescents, adults, pregnant women, and people with weakened immune systems. The best way to prevent chickenpox is to be innoculated with the chickenpox vaccine.
                            Chickenpox used to be very common in the United States. In the early 1990s, an average of 4 million people contracted chickenpox; 10,500 to 13,000 were hospitalized, and 100 to 150 died each year.
                            A vaccine for Chickenpox became available in the United States in 1995. Each year, more than 3.5 million cases of chickenpox, 9,000 hospitalizations, and 100 deaths are prevented by the chickenpox vaccination in the United States.
                             For more information, check out the https://www.cdc.gov/chickenpox/about/index.html CDC website concerning Chickenpox."""
            doc = """If you or your child does end up having chickenpox, treatment isn't always necessary, especially when cases are mild.
                        However, the CDC recommends getting medical attention if you are at higher risk of having complications, including those who:\n
                            Are pregnant, immunocompromised,younger than the age of 1 or older than 12 years old, since chickenpox can be more severe and show complications in adults
                             
                        """
        elif label == "Normal_Skin":
            about = """Algorithm concluded that no visual injury or illness is found on the skin visible in the image."""
            doc = """As stated above, it appears that the skin is normal. However, if you are experiencing any of the following symptoms you may wish to seek help from a medical professional:
                            Burning/itching sensation,
                            Numbness,
                            Acute Pain with or without stimuli.
                        """
        else:
            about = """Your session has been lost. Please click on the "New Diagnosis" button and resubmit your image for a proper diagnosis!"""  
    
    
    
        context = {'label': label, 'confidence': confidence, 'about': about, 'doc': doc}

        #context = {'label': label, 'confidence': confidence}

        return render(request, 'NewResults.html', context)
        
def AdvancedPinkeye(request):
    
        label = request.session.get('lab')
        confidence = request.session.get('con')
        about = " "
        doc = " "

        Oconfidence = confidence

        q1= request.POST['q1']
        q2= request.POST['q2']
        q3= request.POST['q3']
        q4= request.POST['q4']

        if label == "Normal_Eye":

            if q1 == "1":
                confidence = confidence - (Oconfidence * 0.03)

            if q2 == "1":
                confidence = confidence - (Oconfidence * 0.05)

            if q3 == "1":
                confidence = confidence - (Oconfidence * 0.1)

            if q4 == "1":
                confidence = confidence - (Oconfidence * 0.02)
            about = """Algorithm concluded that no visual injury or illness is found on the skin visible in the image."""
            doc = """As stated above, it appears that the eye is normal. However, if you are experiencing any of the following symptoms you may wish to seek help from a medical professional:
                            Extreme pressure,
                            Acute pain,
                            Flashes,
                            Tubular vision (also known a Tunnel vision where one experiences a loss of peripheral vision),
                            Visual Snow (Or Visual Static).
                        """
        if label == "PinkEye":

            if q1 == "1":
                confidence = confidence + (Oconfidence * 0.03)

            if q2 == "1":
                confidence = confidence + (Oconfidence * 0.05)

            if q3 == "1":
                confidence = confidence + (Oconfidence * 0.1)

            if q4 == "1":
                confidence = confidence + (Oconfidence * 0.02)
        
            if confidence > 100:
                confidence = 100
            about = """Conjunctivitis, also known as Pink eye, is an inflammation of the conjunctiva. The conjunctiva is the thin clear tissue that lies over the white part of the eye and lines the inside of the eyelid.
                                 The illness is most common in children. And it can be highly contagious (it spreads rapidly in schools and daycares), but it’s rarely found to be serious. It's very unlikely to damage one's vision, especially if diagnosed and treated quickly. When you take care to prevent its spread and follow all healthcare recommendations, Pink eye clears up with no long-term issues.
                                 For more information, check out the <a href ="https://www.cdc.gov/conjunctivitis/index.html">CDC website</a> concerning Pink eye."""
            doc = """Although most cases of pink eye go away without medical care, there are some instances where one should see a doctor as soon as possible for any symptoms. Your doctor may prescribe eye drops to help relieve the symptoms, or to treat bacterial conjunctivitis. Times when you should see a doctor for Pink eye include:
                            If you have a depressed or weakened immune system, making it harder to fight infections;
                            You develop pain in one or both eyes;
                            You develop a sensitivity to light;
                            Your vision becomes blurry;
                            Your symptoms persist or worsen;
                            You are using antibiotic drops for a bacterial infection and the symptoms are not going away;
                            You develop a fever or other signs of an infection, such as swollen glands or fatigue;
                            You have an eye condition unrelated to conjunctivitis.
                        """
        else:
            about = """Your session has been lost. Please click on the "New Diagnosis" button and resubmit your image for a proper diagnosis!"""  
    
    
    
        context = {'label': label, 'confidence': confidence, 'about': about, 'doc': doc}
        #context = {'label': label, 'confidence': confidence}

        return render(request, 'NewResults.html', context)