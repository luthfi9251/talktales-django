from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

# Create your views here.
class SpeechRecognitionView(APIView):
    parser_classes = [MultiPartParser]

    """def post(self, request, format=None):
        audio_file = request.FILES['file']
        audio = AudioSegment.from_file(audio_file)

        # Convert audio to numpy array
        samples = np.array(audio.get_array_of_samples())
        
        # Assuming your model expects audio input in a specific shape
        # This is an example, adjust according to your model's requirements
        samples = samples.reshape(1, -1, 1)

        # Perform prediction
        global model
        prediction = model.predict(samples)
        
        # Process the prediction to get the result
        result = process_prediction(prediction)

        return JsonResponse({'result': result})"""
    
    def get(self, request, format=None):
        return JsonResponse({"Hallo": "World"})