import firebase_admin
from firebase_admin import credentials, storage

# Initialize the Firebase app with my credentials
cred = credentials.Certificate('D:/Sandun/PythonProjects/rnr_rest_api/rnr_rest_api/rnr_rest_api/data-capturing-system-firebase-adminsdk-q8f7n-3422e2b1c6.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'data-capturing-system.appspot.com'
})

def upload_file_to_firebase(file, file_name):
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_file(file)
    blob.make_public()
    return blob.public_url