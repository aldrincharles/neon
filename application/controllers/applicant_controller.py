"""
applicant_controller.py
-----------------------
Controller logic for Applicant-related database operations.
Abstracts Django ORM interactions away from the view layer.
"""

from django.core.exceptions import ObjectDoesNotExist
from application.models import Applicant

def update_applicant_grade(applicant_id, new_grade, target_column='grade'):
    """
    Update the 'grade' or 'verified_grade' field of an Applicant.
    
    Args:
        applicant_id (int or str): Primary key of the Applicant.
        new_grade (str): The new grade to assign (e.g., 'Gold', 'Silver').
        target_column (str): The column to update ('grade' or 'verified_grade').
        
    Returns:
        Applicant: The updated Applicant instance.
        
    Raises:
        ObjectDoesNotExist: If the applicant ID is not found.
        ValueError: If the new_grade is not one of the allowed choices or target is invalid.
    """
    valid_grades = dict(Applicant.GRADE_CHOICES).keys()
    if new_grade not in valid_grades:
        raise ValueError(f"Invalid grade: '{new_grade}'. Must be one of {list(valid_grades)}")
        
    if target_column not in ('grade', 'verified_grade'):
        raise ValueError(f"Invalid target column: '{target_column}'")

    try:
        applicant = Applicant.objects.get(pk=applicant_id)
        if target_column == 'grade':
            applicant.grade = new_grade
        else:
            applicant.verified_grade = new_grade
        applicant.save()
        return applicant
    except Applicant.DoesNotExist:
        raise ObjectDoesNotExist(f"Applicant with ID {applicant_id} not found.")
