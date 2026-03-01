"""
job_details_view.py
-------------------
View function for the Job Details page.

Renders the applicant list for a specific job posting identified by
``job_id``. When a real database model exists the view should perform a
``get_object_or_404(Job, pk=job_id)`` lookup; for now it simply passes the
id as context so the template can reference it.
"""

from django.shortcuts import render


def job_details_view(request, job_id):
    """
    Render the Job Details / Applicants page (jobs/JobDetails.html).

    Args:
        request (HttpRequest): The incoming HTTP request.
        job_id  (int): Primary key of the job posting to display.

    Returns:
        HttpResponse: Rendered job details page.
    """
    # Pass active_page so the navbar keeps 'Jobs' highlighted,
    # and job_id so the template can build back-links or API calls.
    context = {
        'active_page': 'jobs',
        'job_id': job_id,
    }
    return render(request, 'jobs/JobDetails.html', context)
