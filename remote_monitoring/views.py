import csv
import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from .models import Machine, UserMetrics, Email, Session, Survey
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.

def home(request):
    return render(request, 'registration/home.html')

def login(request):
    return render(request, 'registration/login.html')

#Registration Page is not requried as owner will take care of registrations from django admin dashboard
# def registrationPage(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         try:
#             if form.is_valid():
#                 form.save()
#                 username = form.cleaned_data.get('username')
#                 messages.success(request, f'Account created for {username}!!!')
#                 return redirect('login')  # Redirect to the login page after successful registration
#             else:
#                 messages.error(request, 'Please correct the errors below')
#         except Exception as e:
#             messages.error(request, f'Something went wrong: {str(e)}') # Display error message on registration page
#             form = RegisterForm()
#             return redirect('registration')
        
#     else:
#         form = RegisterForm()

#     return render(request, 'registration/registrationPage.html', {'form': form})
  

def base(request):
    return render(request, 'registration/base.html')

# #This function fetches all the machine names and display it on the drop down in bar graph
# def userEngagementMetrics(request):
#     try:
#       machines= Machine.objects.all()
#       messages = None #if there are no error then messages will be none
#     except Exception as e:
#         machines = None #if there are no error then data will be none
#         messages = f'Something went wrong: {str(e)}' # Display error message on homepage
    
#     return render(request, 'registration/userEngagementMetrics.html', {'machines':machines,'messages': messages })

def retrieveMachineData(request):

 try:
        # Attempt to fetch the first machine as a default
        default_machine = Machine.objects.first()
        if not default_machine:
            raise ValueError("No machine data found in the database.")

        # Retrieve the machine_id from the GET parameters or use the default machine ID
        machine_id = request.GET.get('machine_id', default_machine.id)
        
        # Try fetching the machine by the provided or default ID
        machine = Machine.objects.get(id=machine_id)
        machine_name = machine.machine_name
        messages = None  # No error message initially

        # Filter UserMetrics for the selected machine and count session types
        session_counts = UserMetrics.objects.filter(machine_id=machine_id).aggregate(
            footfall_count=Count('session_id', filter=Q(session_id=1)),
            loitering_count=Count('session_id', filter=Q(session_id=2)),
            partially_engaged=Count('session_id', filter=Q(session_id=3)),
            fully_engaged=Count('session_id', filter=Q(session_id=4)),
            fully_engaged_with_survey=Count('session_id', filter=Q(session_id=5)),
            repeated_sessions=Count('session_id', filter=Q(session_id=6)),
        )

        # Convert session counts and machine name to JSON
        session_count_json = json.dumps(session_counts)
        machine_name_json = json.dumps(machine_name)

 except Machine.DoesNotExist:
        # Handle case where machine ID is not found in the database
        session_count_json = None
        machine_name_json = None
        machine_id = None
        messages = "Selected machine not found."

 except json.JSONDecodeError as json_error:
        # Handle JSON serialization errors
        session_count_json = None
        machine_name_json = None
        messages = f"Data serialization error: {str(json_error)}"

 except Exception as e:
        # Catch-all for any other exceptions
        session_count_json = None
        machine_name_json = None
        machine_id = None
        messages = f"Something went wrong: {str(e)}"

    # Render the template with machine and other required context
 return render(request, 'registration/userEngagementMetrics.html', {
        'session_counts': session_count_json,  # Session count data
        'machines': Machine.objects.all(),  # Repopulate dropdown options
        'default_machine_id': int(machine_id) if machine_id else None,  # Default machine ID for the frontend
        'machine_name': machine_name_json,  # JSON name for chart.js display
        'messages': messages  # Error message if any
    })


#This function fetches per session detail of each machine and display it on frontend


def allSessionData(request):
    try:

        # Attempt to fetch the first machine as a default
        machine_id = request.GET.get('machine_id')
        if not machine_id:
            default_machine = Machine.objects.first()
            if not default_machine:
                raise ValueError("No machine data found in the database.")
            machine_id = default_machine.id
        
        # Retrieve UserMetrics related to the specified machine_id
        sessionData = UserMetrics.objects.filter(machine_id=machine_id).select_related('survey')
         # Retrieve UserMetrics related to the specified machine_id
        sessionData = UserMetrics.objects.filter(machine_id=machine_id).select_related('survey')

        # Pagination setup
        page = request.GET.get('page', 1)  # Get the current page number from the request
        paginator = Paginator(sessionData, 10)  # Show 10 items per page

        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            paginated_data = paginator.page(1)
        except EmptyPage:
            # If the page is out of range, deliver the last page of results
            paginated_data = paginator.page(paginator.num_pages)
        

        if request.GET.get('download') == 'true' :
            
            # Create a response with a CSV file attachment
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="Machine_{machine_id}.csv"'
            machine_name = Machine.objects.get(id=machine_id)

            # Write data to the CSV file
            writer = csv.writer(response)
            writer.writerow([f'Machine Name: {machine_name.machine_name}'])  # Add machine name as a header
            # Write headers (customize based on your model fields)
            writer.writerow(['Time Engaged', 'Distance While Active','Hand Position','CPR Rate','Compression',
                             'Recoil',
                             'Watched Animation',
                             'Sessions played',
                             'Survey Q1',
                             'Survey Q2'
                             ])
            
            for session in sessionData:
                writer.writerow([
                    session.time_engaged,
                    session.distance_while_active,
                    session.hand_position,
                    session.rate,
                    session.compression,
                    session.recoil,
                    session.watched_animation,
                    session.sessions_played,
                    session.survey.question_1_response,
                    session.survey.question_2_response
                    
                ])
            return response
        
        messages = None
        

    except Exception as e:
        # Handle any errors gracefully
        paginated_data = None
        messages = f'Something went wrong: {str(e)}'

    return render(request, 'registration/allSessionData.html', {
        'default_machine_id': int(machine_id),
        'messages': messages,
        'machines': Machine.objects.all(),  # Repopulate the machine dropdown
        'sessionData': paginated_data  # Pass sessionData to the template
    })



#This function checks health status of all the machines present in database
def healthStatus(request):
    try:
      data= Machine.objects.all()
      messages = None #if there are no error then messages will be none
    except Exception as e:
        data = None #if there are no error then data will be none
        messages = f'Something went wrong: {str(e)}' # Display error message on homepage
    return render(request, 'registration/health_dashboard.html',{'data':data,'messages': messages })


#This function fetches session status and it's count from database and display it on overall_metrics pi chart
def overallMetrics(request):
    try: 
     data = UserMetrics.objects.values('session_id').annotate(count=Count('session_id')) #Fetch session status and it's count
      # Prepare session counts as separate lists
     session = [item['session_id'] for item in data]
     for id in session:
         label = Session.objects.get(id=id)
     session_counts = [item['count'] for item in data] 
     messages = None #if there are no error then messages will be none

    except Exception as e:
        session_counts = None #if there is any issue then session_counts will be none
        messages = f'Something went wrong: {str(e)}' # Display error message on frontend
   # Send session count and error messages to the chart.js frontend
    return render(request, 'registration/overall_metrics.html', { 
        'session_counts': session_counts, 
        'messages':messages
    })


def changePassword(request):
    return render(request, 'registration/changePassword.html')


def changePassword(request):
    return render(request, 'registration/changePassword.html')









