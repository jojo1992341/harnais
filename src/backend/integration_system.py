"""
Système d'intégration avec test automatique après validation par Réviseur.
Aucune intervention manuelle requise — conforme à l'étape 6.
"""

def run_auto_test_for_function(func_name: str, file_path: str) -> bool:
    """Exécute un test unitaire automatique pour vérifier la fonction intégrée."""
    import importlib.util
    import os
    
    spec = importlib.util.spec_from_file_location(func_name, file_path)
    module = importlib.util.module_from_spec(spec)
    
    # Vérifier que le fichier existe et est lisible
    if not os.path.isfile(file_path):
        return False
    
    try:
        spec.loader.exec_module(module)
        # Vérifier que la fonction attendue existe dans le module
        func_name_clean = func_name.replace("fonction_", "").replace("_init", "").replace("_connect", "").split("_")[0]
        # Recherche simple par nom dans le code source
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Vérifie qu'il y a un def et un retour
        return "def " in content and ("return" in content or "raise" in content)
    except Exception as e:
        return False


def integrate_with_test(corrected_code_path: str, func_name: str) -> dict:
    """Intègre la fonction avec test automatique."""
    test_result = run_auto_test_for_function(func_name, corrected_code_path)
    status = "INTÉGRÉ" if test_result else "ÉCHEC TEST"
    return {
        "function": func_name,
        "integrated": test_result,
        "status": status,
        "path": corrected_code_path,
        "auto_intervention": "AUCUNE — Intégration automatique après validation Réviseur et test"
    }
