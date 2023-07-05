from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.mail import send_mail

from .models import Media, Property, Category
from . import forms

class HomeView(ListView):
    model = Property	
    context_object_name = 'properties'
    paginate_by = 16
    template_name = 'properties/index.html'

    def get_context_data(self, **kwargs):
       context = super(HomeView, self).get_context_data(**kwargs)
       context['top_sales'] = Property.objects.filter(is_top_sale=True)
       return context


def category_list(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    my_properties = Property.objects.filter(category=category)
    return render(request, "properties/category.html", {"category": category, "properties": my_properties})


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


# authentication
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'properties/login.html'
    
    def get_success_url(self):
        return reverse_lazy('properties:list_properties') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


# crude

class AddpropertyView(LoginRequiredMixin, CreateView):
    template_name = 'properties/crud/add_property.html'
    model = Property
    form_class = forms.PropertyForm
    success_url = reverse_lazy('properties:add_property')

    def get(self, request, *args, **kwargs):
        # fetching the empty  form and formset

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        media_form = forms.MediaFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  media_form=media_form,))
    
    def post(self, request, *args, **kwargs):
    
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        media_form = forms.MediaFormSet(self.request.POST, self.request.FILES)
        if (form.is_valid() and media_form.is_valid()):
            return self.form_valid(form, media_form,)
        else:
            return self.form_invalid(form, media_form)
        
    def form_valid(self, form, media_form):

        self.object = form.save()
        media_form.instance = self.object
        media_form.save()
        messages.success( self.request,f'Property is added succesfully.')
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, media_form):
        messages.success( self.request,f'Something went wrong, please try again')
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  media_form=media_form))



class ListPropertyView(LoginRequiredMixin, ListView):
    model = Property	
    context_object_name = 'properties'
    template_name = 'properties/crud/list_properties.html'


def delete_property(request, pk):
    my_property = Property.objects.get(pk=pk) 
    my_property.delete()

    messages.success(request, 'Property was deleted successfully')
    return redirect('properties:list_properties')


class UpdatePropertyView(LoginRequiredMixin, CreateView):
    template_name = 'properties/crud/update_property.html'
    model = Property
    form_class = forms.PropertyForm
    success_url = reverse_lazy('properties:update_property')

    def get_context_data(self, **kwargs):
        context = super(UpdatePropertyView, self).get_context_data(**kwargs)
        
        if self.request.POST:
            context['form'] = forms.PropertyForm(self.request.POST, self.request.FILES, instance=self.object)
            context['media_form'] = forms.MediaFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['form'] = forms.PropertyForm(instance=self.get_object())
            context['media_form'] = forms.MediaFormSet(queryset=self.get_object)
            print(self.get_object())
        return context
    

def mark_property_as_sold(request, pk):
    my_property = Property.objects.get(pk=pk)
    my_property.is_sold = True
    my_property.save()
    return redirect('properties:list_properties')




    
    
    

    
     
    

    
    