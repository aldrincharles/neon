"""
views.py
--------
View functions for the TalentStream application.

Each view renders its corresponding template and passes an
``active_page`` context variable consumed by the shared navbar
partial (navbar.html) to highlight the current navigation link.
"""

from django.shortcuts import render


def dashboard_view(request):
    """
    Render the application dashboard (hello.html).

    Args:
        request: The incoming HTTP request.

    Returns:
        HttpResponse: Rendered dashboard page with active_page='dashboard'.
    """
    # Pass active_page so the navbar highlights 'Dashboard'
    context = {'active_page': 'dashboard'}
    return render(request, 'hello.html', context)


def jobs_view(request):
    """
    Render the Jobs Management page (jobs.html).

    Args:
        request: The incoming HTTP request.

    Returns:
        HttpResponse: Rendered jobs page with active_page='jobs'.
    """
    # Pass active_page so the navbar highlights 'Jobs'
    context = {'active_page': 'jobs'}
    return render(request, 'jobs.html', context)


def people_view(request):
    """
    Render the People Directory page (people.html).

    Args:
        request: The incoming HTTP request.

    Returns:
        HttpResponse: Rendered people page with active_page='people'.
    """
    # Pass active_page so the navbar highlights 'People'
    context = {'active_page': 'people'}
    return render(request, 'people.html', context)


def organizations_view(request):
    """
    Render the Organization Directory page (organization.html).

    Args:
        request: The incoming HTTP request.

    Returns:
        HttpResponse: Rendered organizations page with
        active_page='organizations'.
    """
    # Pass active_page so the navbar highlights 'Organizations'
    context = {'active_page': 'organizations'}
    return render(request, 'organization.html', context)
