import boto3
import base64

# ID de la clé KMS à utiliser pour le chiffrement et le déchiffrement
key_id = 'a49aa47f-422b-424d-bd9c-993b1f0b6f0a'

def hello_kms():
    # Spécifiez la région AWS à utiliser
    region_name = 'us-east-1' 

    # Créez une session Boto3 en spécifiant le profil AWS et la région à utiliser
    # 'profile_name' se réfère à un profil AWS configuré dans ~/.aws/credentials
    session = boto3.session.Session(profile_name='MAD', region_name=region_name)

    # Crée un client KMS utilisant la session Boto3
    client = session.client('kms')
    
    # Demande à l'utilisateur de saisir un texte à chiffrer
    test = input("Veuillez saisir un texte\n")

    # Chiffre le texte saisi en utilisant la clé KMS spécifiée
    encryption_result = client.encrypt(KeyId=key_id, Plaintext=test)
    
    # Récupère le texte chiffré (sous forme de blob binaire) du résultat de chiffrement
    blob = encryption_result['CiphertextBlob']
    
    # Encode le blob binaire en base64 pour le rendre lisible sous forme de chaîne de caractères
    blob = base64.b64encode(blob)
    
    # Convertit le blob encodé en base64 en chaîne de caractères UTF-8
    chiff = blob.decode('utf-8')
    print("\n") 
    # Affiche le texte chiffré en base64
    print('Chiffré =', chiff)
    print("\n")

    # Déchiffre le texte chiffré en utilisant KMS
    decrypted = client.decrypt(CiphertextBlob=base64.b64decode(blob))
    
    # Récupère le texte déchiffré (sous forme de bytes) du résultat de déchiffrement
    text = decrypted['Plaintext']
    
    # Convertit le texte déchiffré en chaîne de caractères UTF-8
    text = text.decode('utf-8')
    
    # Affiche le texte déchiffré
    print('Déchiffré =', text)
    print('\n')

# Si ce script est exécuté directement (et non importé comme module), 
# appelle la fonction hello_kms()
if __name__ == "__main__":
    hello_kms()
