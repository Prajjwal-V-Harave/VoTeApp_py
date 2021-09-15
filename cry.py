import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('google-services.json')
firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://voteapp-1e334-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('/')
ref.set({

    'CANDIDATE':
        {
            'CANDIDATE4': {
                'name': 'vk',
                'id': '4',
                'picture': 'link',

                'votes': '0'

            },

        }
})