from yandex.cloud import get_sdk
from yandex.cloud.secret_manager.v1.secret_service import SecretServiceClient
from yandex.cloud.exceptions import NotFoundError

def get_secret(secret_name):
    sdk = get_sdk()
    secret_service_client = sdk.client(SecretServiceClient)

    try:
        secret = secret_service_client.get(secret_name)
        return secret.data.payload.decode()
    except NotFoundError:
        raise Exception(f'Secret {secret_name} not found.')
