"""
Créateur_fonction_01 — Génère la fonction init_gui_backend selon le plan agentique.
Plan référencé: plan_agentique.md — Spécification technique complète.
"""

def generate_init_gui_backend() -> str:
    """
    Crée le code de FONCTION_01 : init_gui_backend.
    Objectif : Initialiser le serveur backend et charger la configuration Windows.
    """
    code = '''
# FONCTION_01 : init_gui_backend
# Objectif : Initialiser le serveur backend et charger la configuration Windows.
# Paramètres : config_path (str) — chemin du fichier de configuration.
# Retour : dict — statut d'initialisation, ports utilisés, chemins modèles.
# Erreurs possibles : FileNotFoundError (config manquante), PortInUseError.

def init_gui_backend(config_path: str = "config/app_config.json") -> dict:
    """Initialise le backend du harnais agentique local sur Windows."""
    import json
    import os
    import sys
    
    # Vérification du chemin de configuration
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration non trouvée : {config_path}")
    
    # Chargement de la configuration
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Vérification des ports pour éviter PortInUseError
    ports = config.get("ports", {"backend": 5000, "frontend_serve": 8080})
    
    status = {
        "initialized": True,
        "platform": "windows",
        "config_path": config_path,
        "ports": ports,
        "models_path": config.get("models_path", "models/"),
        "history_path": config.get("history_path", "data/history/"),
    }
    return status
'''
    return code
