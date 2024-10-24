from yandexcloud import SDK
from yandex.cloud.secret_manager.v1 import SecretServiceClient
from yandex.cloud.secret_manager.v1 import GetSecretRequest
from yandex.cloud.exceptions import NotFoundError

def get_secret(secret_name):
    sdk = SDK()
    secret_service_client = sdk.client(SecretServiceClient)

    try:
        request = GetSecretRequest(secret_id=secret_name)
        secret = secret_service_client.get(request)
        return secret.data.payload.decode()
    except NotFoundError:
        raise Exception(f'Secret {secret_name} not found.')
