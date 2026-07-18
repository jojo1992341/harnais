# Plan Agentique — Harnais Local (Ollama + llama.cpp) sur Windows
# Backend Python | Frontend HTML/CSS/JS | GUI intégré | Historique conversations
# Date: 2026-07-18

## 1. Architecture globale
- Backend Python (Flask/FastAPI) : serveur local, gestion agents, historique, intégration Ollama et llama.cpp.
- Frontend HTML/CSS/JS : interface web locale avec historique, nouvelles conversations, affichage réponses.
- Intégration : Ollama via API locale (localhost:11434) et llama.cpp via exécutable Windows intégré.

## 2. Fonctions principales (chaque fonction expliquée selon spécification technique)

### FONCTION_01 : init_gui_backend
- Objectif : Initialiser le serveur backend et charger la configuration Windows.
- Paramètres : config_path (str) — chemin du fichier de configuration.
- Retour : dict — statut d'initialisation, ports utilisés, chemins modèles.
- Erreurs possibles : FileNotFoundError (config manquante), PortInUseError (port 5000/11434 occupé).

### FONCTION_02 : connect_ollama
- Objectif : Vérifier la connexion à l'instance Ollama locale et lister les modèles disponibles.
- Paramètres : ollama_url (str, défaut localhost:11434).
- Retour : list[str] — noms des modèles chargés.
- Erreurs possibles : ConnectionRefusedError, TimeoutError.

### FONCTION_03 : connect_llamacpp
- Objectif : Vérifier que l'exécutable llama.cpp (llama-server.exe ou main.exe) est présent et exécutable sous Windows.
- Paramètres : binary_path (str) — chemin vers le binaire.
- Retour : bool — disponibilité.
- Erreurs possibles : FileNotFoundError, PermissionError.

### FONCTION_04 : load_agent_orchestrator
- Objectif : Créer et configurer l'agent orchestrateur qui supervise le plan, la création d'agents et l'intégration finale.
- Paramètres : plan_path (str), agent_config (dict).
- Retour : AgentOrchestrator — instance configurée.
- Erreurs possibles : ConfigError, ImportError.

### FONCTION_05 : create_agent_plan
- Objectif : Créer l'agent Plan qui génère et met à jour le plan du projet. Explique chaque fonction selon spécification technique.
- Paramètres : project_plan (str), detail_level (str).
- Retour : AgentPlan — instance avec méthode explain_function(func_name).
- Erreurs possibles : PlanGenerationError.

### FONCTION_06 : create_pair_agents_for_function
- Objectif : Pour chaque fonction du plan, créer deux agents : Créateur_fonction_X et Réviseur_fonction_X.
- Paramètres : func_name (str), func_spec (dict), model_name (str).
- Retour : tuple[AgentCreator, AgentReviewer] — paire d'agents.
- Erreurs possibles : AgentCreationError.

### FONCTION_07 : run_creator_function
- Objectif : Lancer l'agent Créateur_fonction_X pour générer le code de la fonction selon le plan expliqué.
- Paramètres : agent_creator (AgentCreator), func_name (str), project_path (str).
- Retour : str — code généré.
- Erreurs possibles : CodeGenerationError, SyntaxError.

### FONCTION_08 : run_reviewer_function
- Objectif : Lancer l'agent Réviseur_fonction_X pour vérifier que la fonction est fonctionnelle et sans erreurs. Corrige si nécessaire.
- Paramètres : agent_reviewer (AgentReviewer), code_str (str), func_name (str).
- Retour : str — code corrigé et validé.
- Erreurs possibles : ValidationFailedError, CorrectionError.

### FONCTION_09 : integrate_function_to_project
- Objectif : Intégrer la fonction validée au projet (fichier source approprié, import, tests).
- Paramètres : corrected_code (str), func_name (str), target_file (str), project_path (str).
- Retour : dict — statut d'intégration, fichier modifié, ligne d'insertion.
- Erreurs possibles : IntegrationError, FileWriteError.

### FONCTION_10 : create_project_reviewer_agent
- Objectif : Une fois toutes les fonctions intégrées, créer l'agent Réviseur_Projet pour vérifier que le projet est fonctionnel et sans erreurs, corriger si nécessaire.
- Paramètres : project_path (str), integrated_functions (list[str]).
- Retour : AgentProjectReviewer — instance.
- Erreurs possibles : ProjectReviewerError.

### FONCTION_11 : run_project_reviewer
- Objectif : Exécuter la révision globale du projet (tests d'intégration, cohérence, erreurs syntaxiques, fonctionnement GUI/backend).
- Paramètres : agent_project_reviewer (AgentProjectReviewer), project_path (str).
- Retour : dict — rapport de révision, erreurs trouvées, corrections appliquées, statut final (OK/KO corrigé).
- Erreurs possibles : ProjectReviewFailedError.

### FONCTION_12 : manage_conversation_history
- Objectif : Gérer l'historique des conversations (création, chargement, suppression, affichage) dans une base locale (JSON/SQLite).
- Paramètres : action (str: create/load/delete/show), conversation_id (str, optionnel), data (dict, optionnel).
- Retour : dict — résultat de l'action, liste des conversations ou contenu.
- Erreurs possibles : HistoryNotFoundError, DatabaseError.

### FONCTION_13 : create_new_conversation
- Objectif : Créer une nouvelle session de conversation agentique avec un identifiant unique, un titre et un historique vide.
- Paramètres : title (str), initial_message (str), agent_mode (str).
- Retour : str — conversation_id.
- Erreurs possibles : ConversationCreationError.

### FONCTION_14 : render_gui_frontend
- Objectif : Générer et servir l'interface HTML/CSS/JS locale (port défini) permettant la création de conversations, l'affichage historique, la visualisation des réponses et le contrôle des agents.
- Paramètres : server_port (int), template_dir (str), conversation_history (list).
- Retour : bool — statut du rendu.
- Erreurs possibles : TemplateNotFoundError, RenderError.

### FONCTION_15 : integrate_ollama_model
- Objectif : Charger et configurer un modèle spécifique via Ollama pour l'utilisation par les agents (Créateur, Réviseur, Orchestrateur).
- Paramètres : model_name (str), ollama_url (str).
- Retour : dict — statut du modèle, taille, temps de chargement.
- Erreurs possibles : ModelLoadError, ModelNotFoundError.

### FONCTION_16 : integrate_llamacpp_model
- Objectif : Configurer et lancer le modèle via llama.cpp (exécutable Windows) avec paramètres adaptés (contexte, threads, GPU si disponible).
- Paramètres : binary_path (str), model_path (str), n_ctx (int), n_threads (int).
- Retour : dict — statut du processus, port d'écoute, PID.
- Erreurs possibles : ProcessStartError, BinaryNotFoundError.

### FONCTION_17 : save_project_state
- Objectif : Sauvegarder l'état complet du projet (code intégré, historique conversations, configurations agents, résultats révisions) dans un fichier d'état.
- Paramètres : state_data (dict), state_path (str).
- Retour : bool — succès de la sauvegarde.
- Erreurs possibles : StateSaveError.

### FONCTION_18 : load_project_state
- Objectif : Restaurer l'état du projet depuis le fichier d'état (pour reprise après arrêt).
- Paramètres : state_path (str).
- Retour : dict — données d'état restaurées.
- Erreurs possibles : StateLoadError, CorruptStateError.

---
## 3. Dépendances et flux
- Orchestrateur (F04) → Plan (F05) → Paire agents par fonction (F06) pour F01-F18.
- Pour chaque fonction : Créateur (F07) → Réviseur (F08) → Intégration (F09).
- Après intégration de toutes : Réviseur_Projet (F10, F11).
- GUI et historique (F12, F13, F14) fonctionnent en parallèle et sont intégrés dès F01.
- Ollama (F15) et llama.cpp (F16) sont configurés avant création des agents.

---
## 4. Technologies cibles
- Windows : exécution native, chemins Windows, binaire llama.cpp (.exe).
- Backend : Python 3.11+, Flask/FastAPI, SQLite/JSON pour historique.
- Frontend : HTML5, CSS3, JavaScript vanilla (pas de build nécessaire, intégré directement dans templates).
- Agents : prompts structurés envoyés à Ollama ou llama.cpp selon configuration.
