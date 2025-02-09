
# Create your views here.
from django.shortcuts import render
from .models import Pregunta

def home(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'examenes/home.html', {'preguntas': preguntas})

import openai
from django.shortcuts import render
from .models import Pregunta

# Agrega tu clave gratuita de OpenAI aquí
openai.api_key = "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"

def generar_preguntas(request):
    if request.method == "POST":
        texto = request.POST['texto']

        # Llamada a la IA
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Genera preguntas y respuestas a partir del texto."},
                {"role": "user", "content": texto}
            ]
        )

        # Extraer preguntas y respuestas
        for item in respuesta['choices'][0]['message']['content'].split("\n"):
            if "Pregunta" in item:
                pregunta = item.split(":")[1].strip()
                respuesta = "Pendiente"  # Puedes mejorar esto

                Pregunta.objects.create(texto=pregunta, respuesta=respuesta)

    return render(request, 'examenes/generar.html')

from django.http import HttpResponse
from reportlab.pdfgen import canvas

def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="examen.pdf"'
    
    p = canvas.Canvas(response)
    p.drawString(100, 750, "Examen Generado")
    p.showPage()
    p.save()
    
    return response
