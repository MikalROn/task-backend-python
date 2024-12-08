from .models import Task
from rest_framework.test import APITestCase
from rest_framework import status



class TaskTest(APITestCase):
    
    def setUp(self):
        self.task = Task.objects.create(descricao="test0", completo=False)
        self.task1 = Task.objects.create(descricao="test1", completo=False)
        self.task2 = Task.objects.create(descricao="test2", completo=False)
        
        self.uri = '/api/task/'
    
    def test_task_create(self):
        data = {
            "descricao": "test"
        }
        
        r = self.client.post(self.uri, data)
        
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
    
    
    def test_task_list(self):
        
        r = self.client.get(self.uri)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)
    
    
    def test_task_update(self):
        data = {
            "descricao": "test"
        }
        
        r = self.client.put(f'{self.uri}{self.task.pk}/', data)

        print(r.status_code, r.content, r.context)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)
    
    
    def test_task_delete(self):
        data = {
            "descricao": "test"
        }
        
        r = self.client.put(f'{self.uri}{self.task.pk}/', data)

        print(r.status_code, r.content, r.context)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)
    
    
    def test_task_get(self):
        data = {
            "descricao": "test Update"
        }
        
        r = self.client.put(f'{self.uri}{self.task.pk}/', data)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)