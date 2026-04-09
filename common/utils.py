from django.utils.text import slugify
import uuid
import random
import string


def generate_unique_id():
    """Generate a unique ID"""
    return str(uuid.uuid4())


def generate_random_string(length=10):
    """Generate a random string of specified length"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def convert_to_slug(text):
    """Convert text to slug format"""
    return slugify(text)


def get_client_ip(request):
    """Get client IP from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def paginate_queryset(queryset, page, page_size=20):
    """Manually paginate a queryset"""
    start = (page - 1) * page_size
    end = start + page_size
    return queryset[start:end]
