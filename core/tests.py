from .models import Task
from rest_framework.test import APITestCase
from rest_framework import status



class TaskTest(APITestCase):
    
    def setUp(self):
        self.task = Task.objects.create(descricao="test0", completo=False)
        self.task1 = Task.objects.create(descricao="test1", completo=False)
        self.url = 'api/' + 'task'
    



    def test_task_create(self):
        data = {
            "descricao": "test"
        }
        
        r = self.client.post(self.url, data)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)
    
    
    def test_task_list(self):
        
        r = self.client.get(self.url)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)
    
    def test_task_update(self):
        data = {
            "descricao": "test"
        }
        
        r = self.client.put(f'/api/task/{self.task.pk}', data)

        print(r.status_code, r.content, r.context)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)
    