from django.test import TestCase
from rest_framework.test import APIClient
from .models import Todo

class TodoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_todos(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        creating = self.client.post('/api/todos/', {'title': 'Test Todo'})
        self.assertEqual(creating.status_code, 201)

    def test_delete_todo(self):
        todo = Todo.objects.create(title='Test')
        deleting = self.client.delete(f'/api/todos/{todo.id}/')
        self.assertEqual(deleting.status_code, 204)

    def test_create_todo_empty_list(self):
        empty = self.client.post('/api/todos/', {'title': ''})
        self.assertEqual(empty.status_code, 400)