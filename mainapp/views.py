from django.shortcuts import render, get_object_or_404, redirect
from .models import SMS
from .forms import SMSForm
import requests

def sms_list(request):
    sms_list = SMS.objects.all()
    return render(request, 'sms_list.html', {'sms_list': sms_list})

def sms_detail(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    return render(request, 'sms_detail.html', {'sms': sms})

def sms_new(request):
    if request.method == "POST":
        form = SMSForm(request.POST)
        if form.is_valid():
            sms = form.save(commit=False)
            sms.save()
            send_sms(sms.to_number, sms.message)
            return redirect('sms_detail', pk=sms.pk)
    else:
        form = SMSForm()
    return render(request, 'index.html', {'form': form})
def sms_edit(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    if request.method == "POST":
        form = SMSForm(request.POST, instance=sms)
        if form.is_valid():
            sms = form.save(commit=False)
            sms.save()
            send_sms(sms.to_number, sms.message)
            return redirect('sms_detail', pk=sms.pk)
    else:
        form = SMSForm(instance=sms)
    return render(request, 'index.html', {'form': form})

def sms_delete(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    sms.delete()
    return redirect('sms_list')

def send_sms(to_number, message):
    api_key = "q2fTLzxo4m7KwO0ctcnTICwuCv0UJHKoK7XEOIjZW8xXoVCgP5Px9fK1NlT0"
    base_url = "https://www.fast2sms.com/dev/bulkV2"

    headers = {
        "authorization": api_key,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    payload = {
        "route": "q",
        "message": message,
        "language": "english",
        "numbers": to_number,
    }

    response = requests.post(base_url, headers=headers, json=payload)
    print(response.text)  # You can handle the API response as need

# def index(request):
#     return render(request,"index.html")