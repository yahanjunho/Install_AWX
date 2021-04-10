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

BROADCAST_WEBSOCKET_SECRET = "bDVnMGV1YXVXZkZXeEpJOnVRLGpTbEJ3dDVVeWpUR3Fna2IzLF9ZZXY3YUw6cVhsUXlrLnlDdlEydUtVQTZ6eHFxU1lGQS1vSWJNRk90LGRycXR2NElkeS01OnpLTTJfbXk1VW04d1NUeXVBSm1kMzYxNC1kaHAsSmctSzpqd2Q="
