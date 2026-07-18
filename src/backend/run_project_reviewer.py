"""
Intégration du Réviseur_Projet — Étape 7 obligatoire.
Crée l'agent et exécute la révision complète après intégration de toutes les fonctions.
"""

from src.agents.reviseur_projet import AgentProjectReviewer

# Liste des fonctions intégrées
integrated_functions = [
    "F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08", "F09",
    "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18"
]

project_path = "."

agent_project_reviewer = AgentProjectReviewer(project_path, integrated_functions)
result = agent_project_reviewer.run_full_review(max_iterations=3)

print("=== RÉVISEUR_PROJET — RÉSULTAT ===")
print(f"Statut final : {result['status_final']}")
print(f"Itérations : {result['iterations']}")
print(f"Fonctions intégrées : {result['integrated_functions_count']}")
print(f"Corrections appliquées : {result['corrections_applied']}")
if result['errors_initial']:
    print(f"Erreurs détectées : {result['errors_initial']}")
else:
    print("Aucune erreur détectée.")
