from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.mail import send_mail



from .models import Media, Property


class HomeView(ListView):
    model = Property	
    context_object_name = 'properties'
    paginate_by = 16
    template_name = 'properties/index.html'

    def get_context_data(self, **kwargs):
       context = super(HomeView, self).get_context_data(**kwargs)
       context['top_sales'] = Property.objects.filter(is_top_sale=True)
       return context


# class PropertyDetailView(DetailView):
#     model = Property
#     context_object_name = 'property'
#     template_name = 'properties/detail.html'

def property_details(request, slug):
    property_detail = Property.objects.get(slug=slug)
    property_images = Media.objects.filter(house_property=property_detail)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            send_mail(
                'Message From '+name+' <'+email+'>',
                message,
                'contact@clevelandmedcenter.org',
                ['contact@clevelandmedcenter.org'],
                fail_silently=False,
            )
            messages.success(request, 'Email sent successfully, we will get back to you as soon as possible')
        except:
            messages.error(request, 'There was an error while trying to send your email, please try again')

        finally:
            return redirect('properties:details', slug=property_detail.slug)


    context = {'property': property_detail, 'property_images':property_images}
    return render(request, 'properties/detail.html', context)


class ContactView(TemplateView):
    template_name = 'properties/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            send_mail(
                'Message From '+name+' <'+email+'>',
                message,
                'contact@clevelandmedcenter.org',
                ['contact@clevelandmedcenter.org'],
                fail_silently=False,
            )
            messages.success(request, 'Email sent successfully, we will get back to you as soon as possible')
        except:
            messages.error(request, 'There was an error while trying to send your email, please try again')

        finally:
            return HttpResponseRedirect(reverse_lazy('properties:contact'))


class AllPropertiesView(ListView):
    model = Property	
    context_object_name = 'properties'
    template_name = 'properties/properties.html'


class PropertyDetailView(TemplateView):
    template_name = 'properties/detail.html'



    
    