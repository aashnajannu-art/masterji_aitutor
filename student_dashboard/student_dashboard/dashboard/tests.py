from django.test import TestCase
from django.urls import reverse

class DashboardViewTests(TestCase):
    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_template_used(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertTemplateUsed(response, 'dashboard/index.html')

    def test_dashboard_view_contains_xp_bar(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertContains(response, 'XP Bar')

    def test_dashboard_view_contains_assignments_bar(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertContains(response, 'Assignments Bar')

    def test_dashboard_view_contains_python_workspace(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertContains(response, 'Python Workspace')