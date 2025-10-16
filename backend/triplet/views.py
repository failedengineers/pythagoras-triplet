from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from triplet.models import triplets
from triplet.serializer import tripletsserializer





@api_view(['GET'])
def index(request):
    
    A = request.GET.get('A')
    B = request.GET.get('B')
    C = request.GET.get('C')

    
    if A is None or B is None or C is None:
        return Response({"error": "Please provide A, B, and C"}, status=400)

    
    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        return Response({"error": "A, B, and C must be numeric"}, status=400)

    # 4️⃣ Validate right triangle
    if round(A**2 + B**2, 5) != round(C**2, 5):
        return Response({"error": "Invalid triangle: C² must equal A² + B²"}, status=400)

    # 5️⃣ Calculations
    secC_num = C
    secC_den = B
    cotA_num = B
    cotA_den = A

    secC_value = C / B
    cotA_value = B / A
    final_value = secC_value + cotA_value


    squares = {"A2": A**2, "B2": B**2, "C2": C**2}

    
    response_data = {
        "A": A,
        "B": B,
        "C": C,
        "sec": {"numerator": secC_num, "denominator": secC_den},
        "cot": {"numerator": cotA_num, "denominator": cotA_den},
        "finalAnswer": {"value": round(final_value, 2)},
        "squares": squares
    }

    return Response(response_data)
def home(request):
    return render(request, 'temp1.html')
