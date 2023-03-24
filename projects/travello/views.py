from django.shortcuts import render
from .models import User


# Create your views here.
def destination(request):
    return render(request,'destination_details.html')

def index(request):
    dists = User.objects.all()
    # data = serializers.serialize('json',User.objects.all())
    # cont_list1 = Countrys()
    # cont_list1.name = 'Comfortable Journey'
    # cont_list1.price = 600
    # cont_list1.img = '1.svg'

    # cont_list2 = Countrys()
    # cont_list2.name = 'Kind Service'
    # cont_list2.price = 600
    # cont_list2.img = '2.svg'

    # cont_list3= Countrys()
    # cont_list3.name = 'Luxuries Hotel'
    # cont_list3.price = 600
    # cont_list3.img = '3.svg'

    # lists = [cont_list1,cont_list2,cont_list3]
    # return HttpResponse(dists,content_type='application/json')
    return render(request,'index.html',{})