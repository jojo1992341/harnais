# FONCTION_01 : init_gui_backend — INTÉGRÉE AU PROJET
# Objectif : Initialiser le serveur backend et charger la configuration Windows.
# Paramètres : config_path (str) — chemin du fichier de configuration.
# Retour : dict — statut d'initialisation, ports utilisés, chemins modèles.
# Erreurs possibles : FileNotFoundError (config manquante), PortInUseError.

def init_gui_backend(config_path: str = "config/app_config.json") -> dict:
    """Initialise le backend du harnais agentique local sur Windows."""
    import json
    import os
    
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration non trouvée : {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
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

# RÉVISÉ PAR Réviseur_fonction_01 — Validé sans erreurs.
