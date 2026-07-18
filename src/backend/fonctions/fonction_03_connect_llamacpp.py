# FONCTION_03 : connect_llamacpp — INTÉGRÉE AU PROJET
# Objectif : Vérifier que l'exécutable llama.cpp est présent et exécutable sous Windows.
# Paramètres : binary_path (str) — chemin vers le binaire.
# Retour : bool — disponibilité.
# Erreurs possibles : FileNotFoundError, PermissionError.

def connect_llamacpp(binary_path: str = "bin/llama-server.exe") -> bool:
    """Vérifie que le binaire llama.cpp est présent et exécutable."""
    import os
    
    if not os.path.isfile(binary_path):
        raise FileNotFoundError(f"Binaire llama.cpp non trouvé : {binary_path}")
    
    if not os.access(binary_path, os.X_OK):
        raise PermissionError(f"Le binaire n'est pas exécutable : {binary_path}")
    
    return True

# RÉVISÉ PAR Réviseur_fonction_03 — Iterations: 0, Validé.
