from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Category, Job, Applicant
from rest_framework  import viewsets
from .forms import JobCreationForm

## imports for api
from .serializers import CategorySerializer, JobSerializer, ApplicantSerializer, UserSerializer
from rest_framework import generics

# Create your views here.
def home(request):
	jobs = Job.objects.all().order_by('id').reverse()

	
	form = JobCreationForm()

	context = {
		'jobs': jobs,
		'form': form
	}
	return render(request, 'index.html', context)


# def create_job(request, user_id):
# 	print("testing", user_id)
# 	jobs = Job.objects.all().order_by('id').reverse()

# 	if request.method == 'POST':
# 		form = JobCreationForm(request.POST)
# 		if form.is_valid():
# 			category = form.cleaned_data['category']
# 			country = form.cleaned_data['country']
# 			city = form.cleaned_data['city']
# 			name = request.POST.get('name')
# 			description = request.POST.get('description')
# 			job_form = Job(job_offered_by_id=user_id, category=category, city=city, name=name, description=description)

# 			job_form.save()

# 			redirect('home')
# 	else:
# 		form = JobCreationForm()

# 	context = {
# 		'jobs': jobs,
# 		'form': form
# 	}
# 	return render(request, 'home.html', context)



### API end-points

##  category
class CategoryListView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoryListCreateView(generics.CreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoryListDetailedView(generics.RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoryListUpdateView(generics.UpdateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryListDeleteView(generics.DestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

##  job
class JobListView(generics.ListAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer


class JobListCreateView(generics.CreateAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer


class JobListDetailedView(generics.RetrieveAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer


class JobListUpdateView(generics.UpdateAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer

class JobListDeleteView(generics.DestroyAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer

##  applicant
class ApplicantListView(generics.ListAPIView):
	queryset = Applicant.objects.all()
	serializer_class = ApplicantSerializer


class ApplicantListCreateView(generics.CreateAPIView):
	queryset = Applicant.objects.all()
	serializer_class = ApplicantSerializer


class ApplicantListDetailedView(generics.RetrieveAPIView):
	queryset = Applicant.objects.all()
	serializer_class = ApplicantSerializer


class ApplicantListUpdateView(generics.UpdateAPIView):
	queryset = Applicant.objects.all()
	serializer_class = ApplicantSerializer

class ApplicantListDeleteView(generics.DestroyAPIView):
	queryset = Applicant.objects.all()
	serializer_class = ApplicantSerializer




# ## User auth api

class UserListView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserListCreateView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserListDetailedView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserListDeleteView(generics.DestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
