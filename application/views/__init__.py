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
    return render(request, 'jobs/Jobs.html', context)


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


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from application.controllers.applicant_controller import update_applicant_grade

@csrf_exempt
def update_grade_api(request, applicant_id):
    """
    API endpoint to update an applicant's grade via AJAX.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_grade = data.get('grade')
            target_column = data.get('target', 'grade')
            
            if not new_grade:
                return JsonResponse({'success': False, 'error': 'Missing grade value'}, status=400)
                
            updated_applicant = update_applicant_grade(applicant_id, new_grade, target_column)
            
            # The returned grade could be either grade or verified_grade depending on target
            updated_value = getattr(updated_applicant, target_column)
            
            return JsonResponse({
                'success': True,
                'applicant_id': updated_applicant.id,
                'new_grade': updated_value,
                'target': target_column
            })
            
        except ValueError as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
        except Exception as e:
            # Re-wrap ObjectDoesNotExist or other errors
            return JsonResponse({'success': False, 'error': str(e)}, status=404)
            
    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
