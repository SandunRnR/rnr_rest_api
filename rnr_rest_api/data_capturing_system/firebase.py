import firebase_admin
from firebase_admin import credentials, storage

# Initialize the Firebase app with my credentials
cred = credentials.Certificate('Local path where the generated private key is stored')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'data_capturing_system_storage_bucket_url'
})

def upload_file_to_firebase(file, file_name):
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_file(file)
    blob.make_public()
    return blob.public_url