from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser, run_flow
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools

#Mets ici le chemin vers ton fichier client_secret.json
CLIENT_SECRETS_FILE = "./client_secret.json"

#Cette URL est requise, mais non utilisée dans cet exemple.
MISSING_CLIENT_SECRETS_MESSAGE = "WARNING: Please configure OAuth 2.0"

YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

#Cette fonction permet de récupérer les credentials OAuth2
def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
        scope=YOUTUBE_SCOPE,
        message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        flags = argparser.parse_args()
        credentials = ru
n_flow(flow, storage, flags)

 return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

#Cette fonction va poster le commentaire
def insert_comment(youtube, channel_id, video_id, text):
    try:
        youtube.commentThreads().insert(
            part="snippet",
            body=dict(
                snippet=dict(
                    channelId=channel_id,
                    videoId=video_id,
                    topLevelComment=dict(
                        snippet=dict(
                            textOriginal=text
                        )
                    )
                )
            )
        ).execute()
    except HttpError as e:
        print("Une erreur est survenue: %s" % e)

if name == "main":
    youtube = get_authenticated_service()
    channel_id = "@Domi_Geek"  # Remplace par l'ID de la chaîne où tu veux commenter
    video_id = "F7tJQypHC08"  # Remplace par l'ID de la vidéo que tu veux commenter
    text = "first"  # Remplace par le texte de ton commentaire
    insert_comment(youtube, channel_id, video_id, text)