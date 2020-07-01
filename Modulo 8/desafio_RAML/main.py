
doc = '''
#%RAML 1.0
title: python-12
version: v1
mediaType:  application/json

securitySchemes:
    oauth_2_0:
        description:
        type:
        describedBy:
            headers:
                Authorization:
                    description: |
                        Used to send a valid OAuth 2 access token. Do not use
                        with the "access_token" query string parameter.
                    type: string
                queryParameters:
                    access_token:
                        description: |
                            Used to send a valid OAuth 2 access token. Do not use with
                            the "Authorization" header.
                        type: string
                responses:
                    401:
                        description: |
                            Bad or expired token. This can happen if the user or Movie API
                            revoked or expired an access token. To fix, re-authenticate
                            the user.
                    403:
                        description: |
                            Bad OAuth request (wrong consumer key, bad nonce, expired
                            timestamp...). Unfortunately, re-authenticating the user won't help here.
                settings:
                    authorizationGrants: [ authorization_code, implicit ]
        types:
            Auth:
                type: object
                discriminator: token
                properties:
                    token: string 
        
            Agent:
                type: object
                discriminator: token
                properties:
                    agent_id:
                        type: number
                    user_id:
                        type: number
                    name:
                        type: string
                    status:
                        type: boolean
                    environment:
                        type: string
                    version:
                        type: string
                    address:
                        type: string 
                example:
                    agent_id:
                        type: number
                    user_id:
                        type: number
                    name:
                        type: string
                    status:
                        type: boolean
                    environment:
                        type: string
                    version:
                        type: string
                    address:
                        type: string 
                         
               
            Event:
                type: object
                discriminator: token
                properties:
                    event_id:
                        type: number
                    agent_id: 
                        type: number
                    level:
                        type: text
                    payload:
                        type: text
                    shelve:
                        type: boolean
                    date:
                        type: datetime 
                example:
                    event_id:
                        type: number
                    agent_id: 
                        type: number
                    level:
                        type: text
                    payload:
                        type: text
                    shelve:
                        type: boolean
                    date:
                        type: datetime 
            Group:
                type: object
                discriminator: token
                properties:
                    group_id:
                        type: number
                    name:
                        type: string
                example:
                    group_id:
                        type: number
                    name:
                        type: string
        
            User:
                type: object
                discriminator: token
                properties:
                    user_id:
                        type: number
                    name:
                        type: string
                    password:
                        type: string
                    email:
                        type: string
                    last_login:
                        type: date    
/auth/token:
    get:
        queryParameters:
    post:
        body: Auth

/agents:
    get:
        queryParameters:
            agent_id:
                required: True
                type: number
            user_id:
                required: True
                type: number
            name:
                required: True
                type: string
            status:
                required: True
                type: boolean    
            environment:
                required: True
                type: string
            version:
                required: True
                type: string
            address:
                required: True
                type: string
            
        responses:
            200:
                body:
                type: Agent[]
            500:
                body:
                type: Mensagem
                example: Ocorreu um erro inesperado          
    post:
        body:
            type: Agent[]
        /{agent_id}:
            put:
            delete:
        /{user_id}:
            get:
                queryparameters:
/event:
    get:
        queryParameters:
            event_id:
                required: True
                type: number
            agent_id:
                required: True
                type: number
            level:
                required: True
                type: text
            payload:
                required: True
                type: text
            shelve:
                required: True
                type: boolean
            date:
                required: True
                type: datetime
    post:
        body:
            type: Event[]
        /{event_id}:
            put:
            delete:
        /{agent_id}/:
            get:
                queryparameters:
                
                
/users:
    get:
        queryParameters:
            user_id:
                required: True
                type: number
            name:
                required: True
                type: string 
            password:
                required: True
                type: string
            email:
                required: True
                type: string
            last_login:
                required: True
                type: date 
    post:
        body:
          type: User[]
    /{user_id}:
        put:
        delete:

/groups:
    get:
        queryParameters:
            group_id:
                required: True
                type: number
            name:
                required: True
                type: string
    post:
        body:
          type: Group[]        
        /{group_id}:
            put:
            delete:
'''
