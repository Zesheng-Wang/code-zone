from django.shortcuts import render, redirect
from .models import WeightRecord
from .forms import WeightRecordForm
import json

def dashboard(request):
    records = WeightRecord.objects.all().order_by('date')
    
    chart_data = {
        'dates': [record.date.strftime("%Y-%m-%d") for record in records],
        'weights': [float(record.weight) for record in records],
        'bmis': [float(record.bmi) for record in records]
    }
    
    context = {
        'form': WeightRecordForm(),
        'records': records.reverse()[:10],
        'chart_data': json.dumps(chart_data),
        'latest_record': records.last()
    }
    return render(request, 'health_tracker/dashboard.html', context)

def add_weight(request):
    if request.method == 'POST':
        form = WeightRecordForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')