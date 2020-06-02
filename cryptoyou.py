from flask import Flask, request, jsonify
import crypt_functions
import decrypt_functions


app = Flask(__name__)

model = {
    'cryptography' : '',
    'data' : '',
    'key' : ''
}


@app.route("/", methods=['GET'])
def rules():
    return jsonify({
        'how_to_use' : ' ',
        'cryptography_types' : {
            'chinese' : 'convert the characters to chinese characters'
        }
    })

@app.route("/crypt", methods=['POST'])
def choose_crypt():
    data = request.get_json()
    crypt = data['cryptography']
    user_data = data['data']
    key = data['key']

    response = crypt_functions

    return jsonify({'crypted' : response.To_crypt(user_data, crypt, key)}), 200

    return jsonify({'error':'server error'}), 400


@app.route("/decrypt", methods=['POST'])
def decrypt():
    data = request.get_json()
    crypt = data['cryptography']
    user_data = data['data']
    key = data['key']

    response = decrypt_functions

    return jsonify({'decrypted':response.To_decrypt(user_data, crypt, key)}), 200

    return jsonify({'error':'server error'}), 400





if __name__ == "__main__":
    app.run(debug=True)