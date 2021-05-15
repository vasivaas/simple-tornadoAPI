# **Test task:**

Develop simple Tornado API with ability to add, delete, get info about user credentials from MongoDB.
Credentials are of two types: user/password, api_token. Although, you should store these objects in one collection.

## Installation & running from source codes
1. Clone the repo: with https:

        git clone https://github.com/vasivaas/simple-tornadoAPI.git

    or
   
        other method convenient for you

2. Install dependencies:
    
        pip install -r requirements.txt 

3. Run the app:

        cd /path/to/tornadoAPI
        python3 app.py


## Possible requests
1. POST (http://yourhost:yourport/api/v1/credentials) --  add new user credential(-s)
2. GET (http://yourhost:yourport/api/v1/credentials)  --  get info about all credentials collection
3. GET (http://yourhost:yourport/api/v1/credentials/<credential_id>) -- get info about one user credential by id
4. DELETE (http://yourhost:yourport/api/v1/credentials/<credential_id>) --  remove one user credential with id-><credential_id>
