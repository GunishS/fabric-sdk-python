from azure.identity import AzureCliCredential, ClientSecretCredential
from typing import Union

class FabricAuthenticator:
    def __init__(self, tenant_id: str = None, client_id: str = None, client_secret: str = None):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

    def get_credential(self) -> Union[AzureCliCredential, ClientSecretCredential]:
        if self.client_id and self.client_secret:
            return ClientSecretCredential(
                tenant_id=self.tenant_id,
                client_id=self.client_id,
                client_secret=self.client_secret
            )
        return AzureCliCredential()
