================================
Rest API
================================


List Recipe
 - :endoint:  /recipe
 - :search params:  name, preptime, difficulty, vegetarian
 - :method: GET
 - :Content Type: application/json
 - :response:

  .. code-block:: json

     {
      "results": [
          {
              "id": 5,
              "name": "Coffee",
              "preptime": 5,
              "difficulty": 1,
              "vegetarian": true
          },
      ],
      "total": 1,
      "next": null,
      "previous": null
     }

Create Recipe ( pass ACCESS-TOKEN in headers )
 - :endoint:  /recipe
 - :method: POST
 - :Content Type: application/json
 - :payload:

  .. code-block:: json

    {
        "name": "Coffee",
        "preptime": 5,
        "difficulty": 1,
        "vegetarian": true
    }

  - :response:

  .. code-block:: json

    {
        "id": 1,
        "name": "Coffee",
        "preptime": 5,
        "difficulty": 1,
        "vegetarian": true
    }


Get Recipe
 - :endoint:  /recipes/{id}
 - :method: GET
 - :Content Type: application/json
 - :response:
 
  .. code-block:: json

    {
        "id": 1,
        "name": "Coffee",
        "preptime": 5,
        "difficulty": 1,
        "vegetarian": true
    }

Update Recipe ( pass ACCESS-TOKEN in headers )
 - :endoint:  /recipes/{id}
 - :method: PUT
 - :Content Type: application/json

 - :payload:

  .. code-block:: json

    {
        "name": "Coffee",
        "preptime": 5,
        "difficulty": 1,
        "vegetarian": true
    }

 - :response:

  .. code-block:: json

    {
        "id": 1,
        "name": "Coffee",
        "preptime": 5,
        "difficulty": 1,
        "vegetarian": true
    }

Delete Recipe ( pass ACCESS-TOKEN in headers )
 - :endoint:  /recipes/{id}
 - :method: DELETE
 - :Content Type: application/json
 - :response: null


Rate Recipe
 - :endoint:  /recipes/{id}/rating
 - :method: POST
 - :Content Type: application/json
 - :payload:

  .. code-block:: json

    {
        "value": 4,
    }


User Signup
 - :endoint:  /user-signup
 - :method: POST
 - :Content Type: application/json
 - :payload:

  .. code-block:: json

    {
        "email": "abc@gmail.com",
        "password": "qwerty"
    }

  - :response:

  .. code-block:: json

    {
        "id": 1,
        "email": "abc@gmail.com"
    }

User Login
 - :endoint:  /user-login
 - :method: POST
 - :Content Type: application/json
 - :payload:

  .. code-block:: json

    {
        "email": "abc@gmail.com",
        "password": "qwerty"
    }

  - :response:

  .. code-block:: json

    {
        "ACCESS-TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjUyODY5NTIsImlhdCI6MTUyNDQyMjk1Miwic3ViIjoxfQ.su-yFnXgV1bYJrm2ZCU9Piqq2_viLPx93zCZs_cJ3SI"
    }