import requests
from .authentication import FabricAuthenticator

class FabricClient:
    def __init__(self, authenticator: FabricAuthenticator):
        self.authenticator = authenticator
        self.base_url = "https://api.fabric.microsoft.com/v1"
        self.session = requests.Session()
        
    def _get_headers(self):
        token = self.authenticator.get_credential().get_token(
            "https://api.fabric.microsoft.com/.default"
        ).token
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def get_workspaces(self):
        response = self.session.get(
            f"{self.base_url}/workspaces",
            headers=self._get_headers()
        )
        response.raise_for_status()
        return response.json()
