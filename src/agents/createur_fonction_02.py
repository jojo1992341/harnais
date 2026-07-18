"""
Créateur_fonction_02 — Génère connect_ollama selon le plan agentique.
Boucle itérative avec Réviseur_fonction_02 si erreurs.
"""

def generate_connect_ollama() -> str:
    """
    Génère le code de FONCTION_02 : connect_ollama.
    """
    code = '''
# FONCTION_02 : connect_ollama
# Objectif : Vérifier la connexion à l'instance Ollama locale et lister les modèles disponibles.
# Paramètres : ollama_url (str, défaut localhost:11434).
# Retour : list[str] — noms des modèles chargés.
# Erreurs possibles : ConnectionRefusedError, TimeoutError.

def connect_ollama(ollama_url: str = "http://localhost:11434") -> list:
    """Vérifie la connexion Ollama locale et retourne la liste des modèles."""
    import requests
    import urllib.parse
    
    url = ollama_url.rstrip("/") + "/api/tags"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        models = [model["name"] for model in data.get("models", [])]
        return models
    except requests.exceptions.ConnectionError:
        raise ConnectionRefusedError(f"Impossible de se connecter à Ollama sur {ollama_url}")
    except requests.exceptions.Timeout:
        raise TimeoutError("Délai d'attente dépassé pour la connexion Ollama")
'''
    return code
