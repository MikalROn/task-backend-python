from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomTaskPagination(PageNumberPagination):
    """
    
    """
    page_size = 10  
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'tasks': data, 
            'totalElements': self.page.paginator.count,  
            'totalPages': self.page.paginator.num_pages,  
        })