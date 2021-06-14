import os, random

import pickle, pandas as pd, requests
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request


#creates a connection with google api and goes through OAuth2
def createService(credFile):
    cred = None
    pickle_file = 'token_photoslibrary_v1.pickle'
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credFile, 'https://www.googleapis.com/auth/photoslibrary')
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    service = build('photoslibrary', 'v1', credentials=cred, static_discovery=False)
    #print(API_SERVICE_NAME, 'service created successfully')
    return service

#uses googlephotoslibrary api to obtain the albums and obtain the list of files
def obtainImage(petName: str):
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.max_rows', 150)
    pd.set_option('display.max_colwidth', 150)
    pd.set_option('display.width', 150)
    pd.set_option('expand_frame_repr', True)

    credFile = 'client_secret_discord_bot.json'
    service = createService(credFile)

    albums = service.albums().list().execute()
    albums_list = albums.get('albums')

    dfalbums = pd.DataFrame(albums_list)
    album_id = dfalbums[dfalbums['title'] == petName]['id'].to_string(index=False).strip()

    #initialize a list for all the items in a specific album
    mediaItemList = []
    pageToken = ""
    #iterates through all pages in an album
    while True:
        body = {
            "albumId": album_id,
            "pageToken": pageToken if pageToken != "" else "",
            "pageSize": 100
        }
        res = service.mediaItems().search(body=body).execute()
        mediaItems = res.get('mediaItems', [])
        mediaItemList.extend(mediaItems)
        pageToken = res.get('nextPageToken')
        if not pageToken:
            break

    #initialize a list of all the download urls of each item in mediaItemList
    images = []
    for media_file in mediaItemList:
        #file_name = media_file['filename']
        download_url = media_file['baseUrl'] + '=d'
        images.append(download_url)
    chosen_image = random.choice(images)

    rdNumber = random.randrange(1000)
    file_name = f'temp{rdNumber}.jpg'
    download_file(chosen_image, file_name)
    return file_name

#downloads the image file
def download_file(url:str, file_name:str):
    response = requests.get(url)
    if response.status_code == 200:
        #print('Downloading file {0}'.format(file_name))
        with open(os.path.join(r'./temp', file_name), 'wb') as f:
            f.write(response.content)
            f.close()

#obtainImage('Billy')
#obtainImage('Mocha')
