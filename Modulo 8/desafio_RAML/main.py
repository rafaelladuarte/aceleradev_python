
doc = '''
title: python-12
version: v1
mediaType:  application/json

securitySchemes:
    JWT:
        description: Esquema para autenticação com Token JWT.
        type: 
        describedBy:
            headers:
                Authorization:
                    description: |
                         Usado para enviar o JSON Web Token no request.
                    type: string
                    required: true
                responses:
                    401:
                        description: |
                            Senha de autenticação incorreta
                    403:
                        description: |
                            Proibido                         
                settings:
                    signatures: ['HMAC-SHA256']
                    authorizationGrants: [ authorization_code, implicit ]
types:
    Auth:
        type: object
        discriminator:  
            properties:
                token: 
        
    Agent:
        type: object
        discriminator: 
            properties:
                agent_id:
                    type: integer
                user_id:
                    type: integer
                name:
                    type: string
                    maxLength: 50
                status:
                    type: boolean
                environment:
                    type: string
                    maxLength: 20
                version:
                    type: string
                    maxLength: 5
                address:
                    type: string 
                    maxLength: 39
            example:
                agent_id: 8
                user_id: 7
                name: Agente example
                status: True
                environment: Environment X
                version: 1.0.1
                address: python12.com
                         
               
    Event:
        type: object
        discriminator: 
        properties:
            event_id:
                type: integer            
            agent_id: 
                type: integer
            level:
                type: text
                maxLength: 20
            payload:
                type: text
            shelve:
                type: boolean
            date:
                type: datetime 
        example:
            event_id: 20
            agent_id: 15
            level: Level example
            payload: Payload example
            shelve: True
            date: 2020-07-01T21:00:00

    Group:
        type: object
        discriminator: 
        properties:
            group_id:
                type: integer
            name:
                type: string
                maxLength: 20
        example:
            group_id: 27
            name: Group example
        
    User:
        type: object
        discriminator: 
        properties:
            user_id:
                type: integer
            name:
                type: string
                maxLength: 50
            password:
                type: string
                maxLength: 50
            email:
                type: string
                maxLength: 254
            last_login:
                type: datetime  
        example:  
            user_id: 12
            name: User example
            password: password example
            email: python12@email.com
            last_login:
            
/auth/token:
    description: Obter o token de autenticação.
    post:
        body:
            application/json:
                properties:
                    name:
                        type: string
                        maxLength: 50
                    password:
                        type: string
                        maxLength: 50
        responses:
            201:
                body:
                    application/json:
                        type: Auth
            400:
                body:
                    application/json:
                        example: |
                            {"error": "Solicitação Incorreta."}

/agents:
    post:
        description: Adiciona novo agente.
        securedBy: [JWT]
        body: 
            application/json:
                example: |
                    {"agent_id": 8
                    "user_id": 7
                    "name": "Agente example"
                    "status": True
                    "environment": "Environment X"
                    "version": 1.0.1
                    "address": python12.com}
        responses:
            201:
                body:
                    application/json:
                        example: |
                            {"agent_id": 36}
            401:
                body:
                    application/json:
                        example: |
                            {"error": "Senha de autenticação incorreta."}

    get:
        description: Retorna todos os agentes.
        securedBy: [JWT]
        responses:
            200:
                body:
                    application/json: Agent[]

    /{id}:
        get:
            description: Retorna o usuário com id especificado.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Agent
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação incorreta"}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}
        put:
            description: Atualização de agente pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Agent
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        delete:
            description: Remoção de agente pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "OK."}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta"}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}
                
    /{id}/events:
        post:
            description: Adição de mais de um evento à um agente específico.
            securedBy: [JWT]
            body:
                application/json: Event[]

            responses:
                201:
                    body:
                        application/json: |
                            {"message": "Aceito."}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        get:
            description: Retornar todos eventos de um agente específico.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Event[]
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        put:
            description: Alteração dos eventos de um agente específico.
            securedBy: [JWT]
            body:
                application/json: Event[]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Eventos alterados com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        delete:
            description: Remoção de mais de um evento de um agente específico.
            securedBy: [JWT]
            body:
                application/json: Event[]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Ok"}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}
/users:

    post:
        description: Adição de um novo usuário.
        securedBy: [JWT]
        body:
            application/json:
                properties:
                    name:
                        type: string
                        maxLength: 50
                    password:
                        type: string
                        maxLength: 50
                    email:
                        type: string
                        maxLength: 254
                    last_login:
                        type: date-only
                example: |
                    {"name": "User Name2",
                    "password": "senha123",
                    "email": "mail@mail.com",
                    "last_login": "2020-07-30"
                    }

        responses:
            201:
                body:
                    application/json:
                        example: |
                            {"user_id": 99}
            
            401:
                body:
                    application/json: |
                        {"error": "Senha de autenticação Incorreta."}

    get:
        description: Retorna todos os usuários.
        securedBy: [JWT]
        responses:
            200:
                body:
                    application/json: User[]
            401:
                body:
                    application/json: |
                        {"error": "Senha de autenticação Incorreta."}
            

    /{id}:
        get:
            description: Busca um usuário específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: User
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        put:
            description: Alteração de um usuário específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Ok"}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        delete:
            description: Remoção de um usuário específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json:  |
                            {"message": "Ok"}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        
/groups:

    post:
        description: Criação de um novo grupo.
        securedBy: [JWT]
        body:
            application/json:
                properties:
                    name:
                        type: string
                        maxLength: 20
                example:
                    name: "Grupo example"
        responses:
            201:
                body:
                    application/json:
                        example: |
                            {"group_id": 57}

            401:
                body:
                    application/json: |
                        {"error": "Senha de autenticação Incorreta."}

    get:
        description: Retorna todos os grupos.
        securedBy: [JWT]
        responses:
            200:
                body:
                    application/json: Group[]
            
            401:
                body:
                    application/json: |
                        {"error": "Senha de autenticação Incorreta."}
            

    /{id}:
        get:
            description: Busca um grupo específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Group

                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}
                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

        put:
            description: Alteração de um grupo específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Ok"}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}

        delete:
            description: Remoção de um grupo específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Ok"}
                401:
                    body:
                        application/json: |
                            {"error": "Senha de autenticação Incorreta."}

                404:
                    body:
                        application/json: |
                            {"error": "Não encontrado."}

'''
