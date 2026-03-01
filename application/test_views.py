"""
test_views.py
-------------
Unit tests for all TalentStream application views.

Tests verify:
- HTTP 200 OK status code for each page.
- Correct template is rendered for each view.
- Correct ``active_page`` context value is passed for each view,
  so the shared navbar can highlight the right navigation link.
"""

from django.test import TestCase, Client
from django.urls import reverse


class DashboardViewTests(TestCase):
    """Tests for the dashboard_view function."""

    def setUp(self):
        """Set up the test client before each test."""
        self.client = Client()

    def test_dashboard_returns_200(self):
        """dashboard_view should return HTTP 200 OK."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_uses_correct_template(self):
        """dashboard_view should render hello.html."""
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'hello.html')

    def test_dashboard_active_page_context(self):
        """dashboard_view should pass active_page='dashboard' in context."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.context['active_page'], 'dashboard')


class JobsViewTests(TestCase):
    """Tests for the jobs_view function."""

    def setUp(self):
        """Set up the test client before each test."""
        self.client = Client()

    def test_jobs_returns_200(self):
        """jobs_view should return HTTP 200 OK."""
        response = self.client.get(reverse('jobs'))
        self.assertEqual(response.status_code, 200)

    def test_jobs_uses_correct_template(self):
        """jobs_view should render jobs/Jobs.html."""
        response = self.client.get(reverse('jobs'))
        self.assertTemplateUsed(response, 'jobs/Jobs.html')

    def test_jobs_active_page_context(self):
        """jobs_view should pass active_page='jobs' in context."""
        response = self.client.get(reverse('jobs'))
        self.assertEqual(response.context['active_page'], 'jobs')


class PeopleViewTests(TestCase):
    """Tests for the people_view function."""

    def setUp(self):
        """Set up the test client before each test."""
        self.client = Client()

    def test_people_returns_200(self):
        """people_view should return HTTP 200 OK."""
        response = self.client.get(reverse('people'))
        self.assertEqual(response.status_code, 200)

    def test_people_uses_correct_template(self):
        """people_view should render people.html."""
        response = self.client.get(reverse('people'))
        self.assertTemplateUsed(response, 'people.html')

    def test_people_active_page_context(self):
        """people_view should pass active_page='people' in context."""
        response = self.client.get(reverse('people'))
        self.assertEqual(response.context['active_page'], 'people')


class JobDetailsViewTests(TestCase):
    """Tests for the job_details_view function."""

    def setUp(self):
        """Set up the test client before each test."""
        self.client = Client()

    def test_job_details_returns_200(self):
        """job_details_view should return HTTP 200 OK for a valid job_id."""
        response = self.client.get(reverse('job_details', kwargs={'job_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_job_details_uses_correct_template(self):
        """job_details_view should render jobs/JobDetails.html."""
        response = self.client.get(reverse('job_details', kwargs={'job_id': 1}))
        self.assertTemplateUsed(response, 'jobs/JobDetails.html')

    def test_job_details_active_page_context(self):
        """job_details_view should pass active_page='jobs' in context."""
        response = self.client.get(reverse('job_details', kwargs={'job_id': 1}))
        self.assertEqual(response.context['active_page'], 'jobs')

    def test_job_details_job_id_in_context(self):
        """job_details_view should pass the job_id integer in context."""
        response = self.client.get(reverse('job_details', kwargs={'job_id': 3}))
        self.assertEqual(response.context['job_id'], 3)

    """Tests for the organizations_view function."""

    def setUp(self):
        """Set up the test client before each test."""
        self.client = Client()

    def test_organizations_returns_200(self):
        """organizations_view should return HTTP 200 OK."""
        response = self.client.get(reverse('organizations'))
        self.assertEqual(response.status_code, 200)

    def test_organizations_uses_correct_template(self):
        """organizations_view should render organization.html."""
        response = self.client.get(reverse('organizations'))
        self.assertTemplateUsed(response, 'organization.html')

    def test_organizations_active_page_context(self):
        """organizations_view should pass active_page='organizations'."""
        response = self.client.get(reverse('organizations'))
        self.assertEqual(response.context['active_page'], 'organizations')
