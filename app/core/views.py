import logging
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .models import FaultPrediction

FASTAPI_URL = "http://localhost:8000/predict"

def home(request):
    return render(request, 'home.html')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def predict_fault(request):
    if request.method == "GET":
        return render(request, 'predict.html')

    try:
        # Unified data extraction
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST.dict()

        # Validate and convert input
        try:
            payload = {
                "Va": float(data["Va"]),
                "Vb": float(data["Vb"]),
                "Vc": float(data["Vc"]),
                "Ia": float(data["Ia"]),
                "Ib": float(data["Ib"]),
                "Ic": float(data["Ic"]),
            }
        except (KeyError, ValueError) as e:
            return JsonResponse({"error": f"Invalid or missing input data: {str(e)}"}, status=400)

        # Call FastAPI with better error handling
        try:
            response = requests.post(FASTAPI_URL, json=payload, timeout=10)
            response.raise_for_status()
            prediction_result = response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"FastAPI connection error: {str(e)}")
            return JsonResponse({"error": f"ML service error: {str(e)}"}, status=503)

        # Validate prediction result
        required_keys = ["G", "A", "B", "C"]
        if not all(key in prediction_result for key in required_keys):
            return JsonResponse({"error": "Invalid response from ML service"}, status=502)

        # Save to database
        fault_prediction = FaultPrediction.objects.create(
            Va=payload["Va"],
            Vb=payload["Vb"],
            Vc=payload["Vc"],
            Ia=payload["Ia"],
            Ib=payload["Ib"],
            Ic=payload["Ic"],
            G=int(prediction_result["G"]),
            A=int(prediction_result["A"]),
            B=int(prediction_result["B"]),
            C=int(prediction_result["C"])
        )

        context = {
            "id": fault_prediction.id,
            "G": prediction_result["G"],
            "A": prediction_result["A"],
            "B": prediction_result["B"],
            "C": prediction_result["C"],
            "input": payload
        }
        
        # Use the correct template name
        return render(request, 'results.html', context)

    except Exception as e:
        logging.exception("Unexpected error in predict_fault")
        return JsonResponse({"error": f"Internal server error: {str(e)}"}, status=500)