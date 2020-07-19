<h3>How to run the project:</h3>

- Install python version 3.6 or higher

- Install the dependences using the following command: pip install -r requirements.txt 

- Now run cryptoyou.py


<h3>How to use:</h3>
- In http://127.0.0.1:5000/ you can see the cypher types and the doc link.

- In http://127.0.0.1:5000/crypt you can make a post(the http method) with the data to cypher following the model.

- In http://127.0.0.1:5000/decrypt you can make a post(the http method) with the data to decypher following the model.

- Model: 
{
    'cryptography' : 'cypher types',
    'data' : 'data to cypher or decypher',
    'key' : 'key to method'
}


- Kinds of cypher:

- Chinese


PS: more types will be added later!