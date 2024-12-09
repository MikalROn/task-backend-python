from .models import Task
from rest_framework.test import APITestCase
from rest_framework import status



class TaskTest(APITestCase):
    
    def setUp(self):
        self.task = Task.objects.create(descricao="test0", completo=False)
        self.task1 = Task.objects.create(descricao="test1", completo=False)
        self.task2 = Task.objects.create(descricao="test2", completo=False)
        
        self.task_concluido = Task.objects.create(descricao="test")
        
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
        
        r = self.client.delete(f'{self.uri}{self.task.pk}/')

        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task.pk)
    
    
    def test_task_get(self):
        data = {
            "descricao": "test Update"
        }
        
        r = self.client.put(f'{self.uri}{self.task.pk}/', data)
        
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        
    def test_task_concluir_task(self):
        r = self.client.get(f'{self.uri}{self.task_concluido.pk}/completar-task/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        
        self.task_concluido.refresh_from_db()
        self.assertTrue(self.task_concluido.completo)

    def test_task_cancelar_conclusao_task(self):
        
        
        
        self.task_concluido.completo = True
        self.task_concluido.save()

        r = self.client.get(f'{self.uri}{self.task_concluido.pk}/cancelar-conclusao-task/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        self.task_concluido.refresh_from_db()
        self.assertFalse(self.task_concluido.completo)