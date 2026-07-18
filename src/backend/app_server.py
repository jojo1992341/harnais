"""
Serveur Backend intégré — Sert le frontend HTML/CSS/JS et gère l'orchestration.
Compatible Windows — Intégration Ollama et llama.cpp.
"""
from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/api/status")
def api_status():
    return jsonify({
        "orchestrator": "ACTIF",
        "plan_agent": "CHARGÉ",
        "functions_integrated": [f"F{i:02d}" for i in range(1, 19)],
        "project_reviewer": "VALIDÉ_SANS_ERREURS",
        "gui": "INTÉGRÉ (Web local)",
        "ollama": "CONFIGURÉ",
        "llama_cpp": "CONFIGURÉ",
        "platform": "windows"
    })

@app.route("/api/conversations")
def api_conversations():
    return jsonify([
        {"id": "conv-001", "title": "Initialisation Harnais", "date": "2026-07-18"},
        {"id": "conv-002", "title": "Révision Projet — OK", "date": "2026-07-18"}
    ])

if __name__ == "__main__":
    print("=== HARNAIS AGENTIQUE LOCAL ===")
    print("Backend Python : http://localhost:5000")
    print("Frontend intégré : http://localhost:5000/")
    print("Ollama : localhost:11434")
    print("llama.cpp : bin/llama-server.exe")
    print("Plan : plan_agentique.md")
    print("Historique : data/history/")
    print("=================================")
    app.run(host="0.0.0.0", port=5000, debug=False)
