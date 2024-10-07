from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
import time
from functions import encode, decode, encode_str, decode_str, brute_force_sdes
import numpy as np
from werkzeug.utils import secure_filename
import os
import base64
# S-DES 加密函数

@app.route('/encrypt8Bit', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080')  # 允许指定源的跨域请求
# 8080 端口是前端开发服务器运行的端口，只有来自 http://127.0.0.1:8080 的前端请求才会被允许进行跨域通信
def encrypt8Bit():
    data = request.get_json()
    key = data['key']
    plaintext = data['plaintext']
    key = np.array(list(key)).astype(int)
    plaintext = np.array(list(plaintext)).astype(int)
    # 调用加密函数
    encrypted = encode(key, plaintext)
    return jsonify({'encrypted': encrypted.tolist()})


@app.route('/decrypt8Bit', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080')  # 允许指定源的跨域请求
def decrypt8Bit():
    data = request.get_json()
    key = data['key']
    ciphertext = data['ciphertext']
    key = np.array(list(key)).astype(int)
    ciphertext = np.array(list(ciphertext)).astype(int)
    # 调用解密函数
    decrypted = decode(key, ciphertext)
    return jsonify({'decrypted': decrypted.tolist()})

# ASCII加密路由
@app.route('/encrypt_ascii', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080')  # 允许指定源的跨域请求
def encrypt_ascii():
    data = request.get_json()
    plaintext = data['plaintext']
    key = data['key']
    key = np.array(list(key)).astype(int)
    encrypted = encode_str(key, plaintext)
    return jsonify({"encrypted": encrypted})

# ASCII解密路由
@app.route('/decrypt_ascii', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080')
def decrypt_ascii():
    data = request.get_json()
    ciphertext = data['ciphertext']
    key = data['key']
    key = np.array(list(key)).astype(int)
    decrypted = decode_str(key, ciphertext)
    return jsonify({"decrypted": decrypted})


@app.route('/encrypt_file', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080')  # 允许指定源的跨域请求
def encrypt_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    key = request.form.get('key')
    try:
        key = np.array(list(key)).astype(int)
    except ValueError:
        return jsonify({'error': 'Invalid key format'}), 400

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join('/tmp', filename)
    file.save(file_path)

    encrypted_content = ''
    try:
        with open(file_path, 'r') as file:
            for line in file:
                encrypted_line = encode_str(key, line)
                encrypted_content += encrypted_line
    finally:
        os.remove(file_path)  # 删除临时保存的文件
       # 返回加密后的内容
    return jsonify({'encrypted': encrypted_content})



@app.route('/decrypt_file', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080')  # 允许指定源的跨域请求
def decrypt_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    key = request.form.get('key')
    try:
        key = np.array(list(key)).astype(int)
    except ValueError:
        return jsonify({'error': 'Invalid key format'}), 400

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join('/tmp', filename)
    file.save(file_path)

    decrypted_content = ''
    try:
        with open(file_path, 'r') as file:
            for line in file:
                decrypted_line = decode_str(key, line)
                decrypted_content += decrypted_line
    finally:
        os.remove(file_path)  # 删除临时保存的文件
    return jsonify({'decrypted': decrypted_content})


# 暴力破解路由
@app.route('/bruteforce', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080')
def bruteforce():
    data = request.get_json()
    plaintext = data['plaintext']
    ciphertext = data['ciphertext']
    start_time = time.time()
    ciphertext = np.array(list(ciphertext)).astype(int)
    plaintext = np.array(list(plaintext)).astype(int)
    key = brute_force_sdes(plaintext, ciphertext)
    end_time = time.time()
    # return jsonify({"key": key, "time": round(end_time - start_time, 2)})
    return jsonify({"key": key, "time": round(end_time - start_time, 2)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8050, debug=True)

