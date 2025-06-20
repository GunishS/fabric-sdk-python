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
    
    def list_workspaces(self):
        url = f"{self.base_url}/workspaces"
        response = requests.get(
            url, headers=self.get_headers()
        )
        response.raise_for_status()
        return response.json()
    
    def list_all_workspaces(self):
        url = f"{self.base_url}/workspaces"
        all_workspaces = []
        while url:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            data = response.json()
            all_workspaces.extend(data.get('value', []))
            url = data.get('nextLink')  # If API supports pagination
        return all_workspaces
    
    def run_graphql_query(self, graphql_endpoint, query):
        token = self.authenticator.get_token("https://analysis.windows.net/powerbi/api/.default")
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.post(
            graphql_endpoint,
            json={'query': query},
            headers=headers
        )
        response.raise_for_status()
        return response.json()


