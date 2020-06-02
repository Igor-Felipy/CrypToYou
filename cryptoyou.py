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
        'how_to_use' : 'https://github.com/Igor-Felipy/CrypToYou ',
        'cryptography_types' : {
            'chinese' : 'convert the characters to chinese characters'
        }
    })

@app.route("/crypt", methods=['POST'])
def choose_crypt():
    try:
        data = request.get_json()
        crypt = data['cryptography']
        user_data = data['data']
        key = data['key']

        response = crypt_functions

        return jsonify({'crypted' : response.To_crypt(user_data, crypt, key)}), 200
    except:
        return jsonify({'error':'server error'}), 400


@app.route("/decrypt", methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        crypt = data['cryptography']
        user_data = data['data']
        key = data['key']

        response = decrypt_functions

        return jsonify({'decrypted':response.To_decrypt(user_data, crypt, key)}), 200
    except:
        return jsonify({'error':'server error'}), 400





if __name__ == "__main__":
    app.run(debug=True)