from yandex.cloud import SDK
from yandex.cloud.secret_manager.v1 import SecretServiceClient
from yandex.cloud.exceptions import NotFoundError

def get_secret(secret_name):
    sdk = SDK()
    secret_service_client = sdk.client(SecretServiceClient)

    try:
        secret = secret_service_client.get(secret_name)
        return secret.data.payload.decode()
    except NotFoundError:
        raise Exception(f'Secret {secret_name} not found.')
