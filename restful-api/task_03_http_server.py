#!/usr/bin/python3
import http.server
import socketserver
import json

class GestionnaireRequetes(http.server.BaseHTTPRequestHandler):
    def envoyer_reponse(self, code_statut, contenu, type_contenu='text/plain'):
        self.send_response(code_statut)
        self.send_header('Content-type', type_contenu)
        self.end_headers()
        
        # Encode le contenu en fonction de son type
        if isinstance(contenu, str):
            self.wfile.write(contenu.encode())
        elif isinstance(contenu, dict):
            self.wfile.write(json.dumps(contenu).encode())
    
    def do_GET(self):
        if self.path == '/':
            # Route racine
            self.envoyer_reponse(200, "Hello, this is a simple API!")
            
        elif self.path == '/data':
            # Route /data
            donnees = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.envoyer_reponse(200, donnees, 'application/json')
            
        elif self.path == '/status':
            # Route /status
            self.envoyer_reponse(200, "OK")
            
        else:
            # Gestion des routes non définies
            message_erreur = {
                "erreur": "Page non trouvée",
                "message": f"L'endpoint '{self.path}' n'existe pas",
                "endpoints_disponibles": ["/", "/data", "/status"]
            }
            self.envoyer_reponse(404, message_erreur, 'application/json')

# Configurer le port
PORT = 8000

# Créer et démarrer le serveur
with socketserver.TCPServer(("", PORT), GestionnaireRequetes) as httpd:
    print(f"Serveur démarré sur le port {PORT}")
    print(f"Endpoints disponibles:")
    print(f"- http://localhost:{PORT}/")
    print(f"- http://localhost:{PORT}/data")
    print(f"- http://localhost:{PORT}/status")
    httpd.serve_forever()
