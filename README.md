# Harnais Agentique Local — Intégré (Backend Python + Frontend HTML/CSS/JS)
# Windows — Ollama + llama.cpp
# Date : 2026-07-18

## Objectif
Créer un harnais agentique local entièrement intégré, sans paramètres externes nécessaires, avec un vrai GUI (interface web locale), historique des conversations et création de nouvelles conversations.

## Architecture
- **Backend** : Python (Flask) — Orchestrateur, agents Créateur/Réviseur, intégration Ollama/llama.cpp
- **Frontend** : HTML/CSS/JS intégré — Historique, nouvelles conversations, affichage réponses
- **Modèles** : Même modèle assigné à tous (Ollama / llama.cpp)

## 8 Étapes du Harnais (toutes respectées)

### Étape 1 : Agent Plan
Le plan (`plan_agentique.md`) explique chaque fonction selon spécification technique complète (nom, objectif, paramètres, retour, erreurs possibles).

### Étape 2 : Explication des fonctions
Chaque fonction du plan (F01-F18) est expliquée en détail avec sa spécification technique.

### Étape 3 : Deux agents par fonction
Pour chaque fonction, deux agents sont créés automatiquement :
- `Créateur_fonction_X` (génère le code selon le plan)
- `Réviseur_fonction_X` (vérifie et corrige en boucle itérative)

### Étape 4 : Créateur_fonction_X
Chaque créateur génère le code de la fonction en suivant le plan, avec commentaires et docstrings selon le format choisi.

### Étape 5 : Réviseur_fonction_X (boucle itérative)
Chaque réviseur vérifie la fonction. Si erreurs détectées, applique une boucle itérative de correction (règles prédéfinies + re-vérification) jusqu'à validation ou max_iterations.

### Étape 6 : Intégration au projet (avec test automatique)
Après validation par le Réviseur, chaque fonction est intégrée au projet (`src/backend/fonctions/`) avec un test unitaire automatique. Aucune intervention manuelle requise.

### Étape 7 : Réviseur_Projet
Une fois toutes les fonctions (F01-F18) intégrées, l'orchestrateur crée TOUJOURS l'agent `Réviseur_Projet`. Celui-ci effectue une révision complète (syntaxe, cohérence, intégration, GUI/backend, historique, cohérence globale) et applique des corrections automatiques si nécessaire (boucle itérative jusqu'à 3 itérations).

### Étape 8 : Questions et réponses à chaque étape
Chaque étape a été accompagnée de questions avec 3 à 5 options de réponse proposées, permettant une construction guidée et documentée du harnais.

## Fonctions Intégrées (F01-F18)
- F01 : init_gui_backend
- F02 : connect_ollama
- F03 : connect_llamacpp
- F04 : load_agent_orchestrator
- F05 : create_agent_plan
- F06 : create_pair_agents_for_function
- F07 : run_creator_function
- F08 : run_reviewer_function
- F09 : integrate_function_to_project
- F10 : create_project_reviewer_agent
- F11 : run_project_reviewer
- F12 : manage_conversation_history
- F13 : create_new_conversation
- F14 : render_gui_frontend
- F15 : integrate_ollama_model
- F16 : integrate_llamacpp_model
- F17 : save_project_state
- F18 : load_project_state

## GUI Intégré
- `src/frontend/index.html` — Interface web locale avec historique, création de nouvelles conversations, affichage des réponses et statut des agents.
- Le backend sert le frontend directement (port 5000 par défaut).

## Lancement (Windows)
```bash
# Installer les dépendances (si nécessaire)
pip install flask requests

# Lancer le serveur intégré
python src/backend/app_server.py

# Ouvrir dans le navigateur
# http://localhost:5000
```

## Historique et Conversations
- Stockage local dans `data/history/`
- Nouvelles conversations créables via le bouton "+ Créer une nouvelle conversation"
- Historique visible dans la barre latérale

## Réviseur_Projet — Résultat final
```
Statut final : VALIDÉ_SANS_ERREURS
Itérations : 1
Fonctions intégrées : 18
Corrections appliquées : []
Aucune erreur détectée.
```

## Intégration Ollama et llama.cpp
- Ollama : configuré sur `localhost:11434` (API `/api/tags`)
- llama.cpp : binaire Windows `bin/llama-server.exe` (vérifié par `connect_llamacpp`)
- Les deux sont configurés avant la création des agents dans le plan.

---
Le harnais est entièrement intégré, sans paramètres externes nécessaires pour l'utilisateur final, avec un vrai GUI, un historique des conversations et la possibilité de créer de nouvelles conversations. Toutes les 8 étapes demandées ont été appliquées.
