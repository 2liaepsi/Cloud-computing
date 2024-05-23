import subprocess
import os

def run_command(command, display_output=True):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if display_output:
        if output:
            print(output.decode('utf-8'))
        if error:
            print(error.decode('utf-8'))
    return output.decode('utf-8'), error.decode('utf-8')

def display_file_content(filename):
    try:
        with open(filename, 'rb') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

def main():
    # Demande à l'utilisateur de saisir un texte
    mess = input('Saisissez un texte: ')

    # Demande à l'utilisateur de saisir le nom de base pour le keyring et la clé
    base_name = input('Saisissez le nom de base pour le keyring et la clé: ')

    # Ouvre un fichier nommé `test.txt` en mode écriture et y écrit le texte saisi
    with open('test.txt', 'w') as fichier:
        fichier.write(mess)
    print("Le contenu du fichier initial")

    # Affiche le contenu du fichier `test.txt`
    output, error = run_command("type test.txt")

    # Liste les keyrings disponibles dans la région `us-central1`
    output, error = run_command("gcloud kms keyrings list --location us-central1", display_output=False)

    # Crée un keyring nommé avec le nom de base fourni par l'utilisateur dans la région `us-central1`
    keyring_name = f"{base_name}-kms"
    output, error = run_command(f"gcloud kms keyrings create {keyring_name} --location us-central1")

    # Liste les clés disponibles dans le keyring créé dans la région `us-central1`
    output, error = run_command(f"gcloud kms keys list --location us-central1 --keyring {keyring_name}", display_output=False)

    # Crée une clé nommée avec le nom de base fourni par l'utilisateur dans le keyring créé avec l'objectif d'encryptage, dans la région `us-central1`
    key_name = f"{base_name}-key"
    output, error = run_command(f"gcloud kms keys create {key_name} --location us-central1 --keyring {keyring_name} --purpose encryption")

    # Crypte le fichier `test.txt` en utilisant la clé créée dans le keyring créé. Le résultat chiffré est stocké dans `claire.txt.enc`
    encrypt_command = (
        f"gcloud kms encrypt --key={key_name} --keyring={keyring_name} --location=us-central1 "
        "--plaintext-file=test.txt --ciphertext-file=claire.txt.enc"
    )
    output, error = run_command(encrypt_command)
    if error:
        print("Erreur de chiffrement:", error)
        return

    # Vérifie si le fichier chiffré a été créé avec succès
    if not os.path.exists('claire.txt.enc'):
        print("Erreur : Le fichier claire.txt.enc n'a pas été créé.")
        return

    # Affiche le contenu du fichier chiffré `claire.txt.enc`
    print("Contenu du fichier chiffré claire.txt.enc :")
    encrypted_content = display_file_content('claire.txt.enc')
    if encrypted_content:
        print(encrypted_content.hex())

    # Décrypte le fichier chiffré `claire.txt.enc` en utilisant la clé créée dans le keyring créé. Le résultat déchiffré est stocké dans `decrypted.txt`
    decrypt_command = (
        f"gcloud kms decrypt --key={key_name} --keyring={keyring_name} --location=us-central1 "
        "--ciphertext-file=claire.txt.enc --plaintext-file=decrypted.txt"
    )
    print("Contenu du fichier déchiffré decrypted.txt :")
    output, error = run_command(decrypt_command)
    if error:
        print("Erreur de déchiffrement:", error)
        return

    # Vérifie si le fichier déchiffré a été créé avec succès
    if not os.path.exists('decrypted.txt'):
        print("Erreur : Le fichier decrypted.txt n'a pas été créé.")
        return

    # Affiche le contenu du fichier déchiffré `decrypted.txt`
    output, error = run_command("type decrypted.txt")

if __name__ == "__main__":
    main()
