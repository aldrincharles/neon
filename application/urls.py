"""
urls.py (application)
----------------------
URL configuration for the TalentStream application.

Maps URL paths to the corresponding view functions and assigns
named URL patterns used throughout templates via {% url '...' %}.
"""

from django.urls import path
from . import views
from .job_details_view import job_details_view

# Named URL patterns – referenced in navbar.html as {% url '<name>' %}
urlpatterns = [
    # Dashboard – root of the application namespace
    path('', views.dashboard_view, name='dashboard'),

    # Jobs Management page
    path('jobs/', views.jobs_view, name='jobs'),

    # Job Details / Applicants page – job_id identifies the specific posting
    path('jobs/<int:job_id>/', job_details_view, name='job_details'),

    # People Directory page
    path('people/', views.people_view, name='people'),

    # Organization Directory page
    path('organizations/', views.organizations_view, name='organizations'),
]

