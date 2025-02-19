#!/usr/bin/python3
import http.server
import json

class GestionnaireAPI(http.server.BaseHTTPRequestHandler):
    def _definir_entetes(self, type_contenu='text/plain', code_statut=200):
        self.send_response(code_statut)
        self.send_header('Content-type', type_contenu)
        self.end_headers()

    def do_GET(self):
        # Définition des données exemple
        donnees_exemple = {
            "nom": "Jean",
            "age": 30,
            "ville": "Paris"
        }

        # Gestion des routes
        if self.path == '/':
            self._definir_entetes()
            self.wfile.write(b"Bonjour, ceci est une API simple!")
        
        elif self.path == '/donnees':
            self._definir_entetes('application/json')
            self.wfile.write(json.dumps(donnees_exemple).encode())
        
        elif self.path == '/statut':
            self._definir_entetes()
            self.wfile.write(b"OK")
        
        else:
            # Gestion de l'erreur 404 Non Trouvé
            self._definir_entetes(code_statut=404)
            message_erreur = {"erreur": "Point d'accès non trouvé"}
            self.wfile.write(json.dumps(message_erreur).encode())

def demarrer_serveur(port=8000):
    adresse_serveur = ('', port)
    httpd = http.server.HTTPServer(adresse_serveur, GestionnaireAPI)
    print(f"Serveur en cours d'exécution sur le port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    demarrer_serveur()
