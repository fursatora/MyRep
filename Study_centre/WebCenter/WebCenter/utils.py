from yandex.cloud import SecretManagerServiceClient
from yandex.cloud import get_sdk

def get_secret(secret_name):
    sdk = get_sdk()
    secret_service_client = sdk.client(SecretManagerServiceClient)

    try:
        secret = secret_service_client.get(secret_name)
        return secret.data.payload.decode()
    except NotFoundError:
        raise Exception(f'Secret {secret_name} not found.')