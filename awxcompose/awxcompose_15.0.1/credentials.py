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

BROADCAST_WEBSOCKET_SECRET = "X2VKdDBISzUzLUxOc2dzUFV3WCxZLmxsSkI3YURnejQ0OFRWR2JBVUFGbTFMZDhjYURjR1h1ZVpMdzpJeCx1Tnd0OHdmM2dGdncsbnNsY2hUd1hta0ZKcHVkWjd3V2NFRW1QNTVFSEkzd2ksSnZYWnhOVEZ2Q1BRc1RUT3c4Nno="
