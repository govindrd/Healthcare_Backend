from rest_framework.response import Response


class APIResponse:
    """Standard API response class"""
    
    @staticmethod
    def success(data=None, message="Success", status_code=200):
        """Return success response"""
        return Response({
            'status': 'success',
            'message': message,
            'data': data,
        }, status=status_code)
    
    @staticmethod
    def error(message="Error", errors=None, status_code=400):
        """Return error response"""
        return Response({
            'status': 'error',
            'message': message,
            'errors': errors,
        }, status=status_code)
    
    @staticmethod
    def paginated(data, message="Success", page_info=None, status_code=200):
        """Return paginated response"""
        response_data = {
            'status': 'success',
            'message': message,
            'data': data,
        }
        if page_info:
            response_data['pagination'] = page_info
        return Response(response_data, status=status_code)
