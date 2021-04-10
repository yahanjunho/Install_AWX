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

BROADCAST_WEBSOCKET_SECRET = "U1BZbE9ULDJCaE9IWlRDVWJRSmRGRWRZWkQuLERuLGFrbFpFaGt4RUNqWkh1T3d6V0xRLDdpTU5zd2puLHNjaFB1X212dk1Va0lFUExHZjN1T045c1RqUFgtTEhlUDBaMHVhZm15cnNjaixhOEFZUDpBUXh4TE01czFqMXB2d2I="
