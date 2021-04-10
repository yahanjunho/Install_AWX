DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "VG5wOEksQjR2b1pTOFF4czBNSnBxN0p3c3VqUllrbCxfaS4xRnh1WV9TQ1FPMDlMVHA0UnNYRDRvRDlpWElOOlo0OEl4LG8wcnFrSGx6dUI0ZkdBU3NtdzkseUw3XzNNR1ROc1ZCTHRCWTpRcU9oNURGaXJ0TSxkanoxd3hxSTk="
