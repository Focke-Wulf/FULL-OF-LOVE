class Keys:
    def __init__(self, c_key, c_sec, a_token, a_sec):
        self.c_key = c_key
        self.c_sec = c_sec
        self.a_token = a_token
        self.a_sec = a_sec

token_pool = {
    'Benjamin': Keys(
        '##############################',
        '##############################',
        '##############################',
        '##############################'
    ),

    'XXX': Keys(
        '##############################',
        '##############################',
        '##############################',
        '##############################'
    ),

    'XXX': Keys(
        '##############################',
        '##############################',
        '##############################',
        '##############################'
    ),

    'XXX': Keys(
        '##############################',
        '##############################',
        '##############################',
        '##############################'
    ),

    'XXX': Keys(
        '##############################',
        '##############################',
        '##############################',
        '##############################'
    )
}

db_name = 'melbourne_tweet'

couch_server = ['115.146.94.162:5984','115.146.95.53:5984']

geocode="xxxx"

locations = [
    ["-87.940267,41.946774", "-87.524044, 42.023131"],
    ["-87.862968,41.870391", "-87.524044,41.946774"],
    ["-87.862968,41.794034", "-87.524044,41.870391"],
    ["-87.862968,41.717677", "-87.524044,41.794034"],
    ["-87.862968,41.644335", "-87.524044,41.717677"]]

couchdb_admin={"admin":"cccteam12","password":"admin"}
