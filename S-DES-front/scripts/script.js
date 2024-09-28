function showTab(tabId) {
    // 隐藏所有tab内容
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    // 显示对应tab内容
    document.getElementById(tabId).classList.add('active');
}

function showBit8Tab(action) {
    var encryptTab = document.getElementById('bit8-encrypt');
    var decryptTab = document.getElementById('bit8-decrypt');

    // 隐藏所有界面
    encryptTab.classList.remove('active');
    decryptTab.classList.remove('active');

    // 根据用户点击的按钮显示加密或解密
    if (action === 'encrypt') {
        encryptTab.classList.add('active'); // 显示加密界面
    } else if (action === 'decrypt') {
        decryptTab.classList.add('active'); // 显示解密界面
    }
}

// 显示 ASCII 加密或解密界面
function showASCIITab(action) {
    // 获取所有 ASCII 加密和解密的界面元素
    var encryptTab = document.getElementById('ascii-encrypt');
    var decryptTab = document.getElementById('ascii-decrypt');
    
    // 隐藏所有界面
    encryptTab.classList.remove('active');
    decryptTab.classList.remove('active');
    
    // 根据用户点击的按钮显示加密或解密
    if (action === 'encrypt') {
        encryptTab.classList.add('active'); // 显示加密界面
    } else if (action === 'decrypt') {
        decryptTab.classList.add('active'); // 显示解密界面
    }
}

// 显示文件加密或解密界面
function showFileTab(action) {
    // 获取所有文件加密和解密的界面元素
    var encryptTab = document.getElementById('file-encrypt');
    var decryptTab = document.getElementById('file-decrypt');
    
    // 隐藏所有界面
    encryptTab.classList.remove('active');
    decryptTab.classList.remove('active');
    
    // 根据用户点击的按钮显示加密或解密
    if (action === 'encrypt') {
        encryptTab.classList.add('active'); // 显示加密界面
    } else if (action === 'decrypt') {
        decryptTab.classList.add('active'); // 显示解密界面
    }
}

//重置
function resetInputs() {
    document.querySelectorAll('input').forEach(input => input.value = '');
    document.getElementById("bit8-plaintext").value = "";
    document.getElementById("bit8-key").value = "";
    document.getElementById("bit8-ciphertext").innerText = "";
    document.getElementById("bit8-key-decrypt").innerText = "";
}

// 重置输入
function resetASCIIInputs() {
    document.getElementById("ascii-plaintext").value = "";
    document.getElementById("ascii-ciphertext").value = "";
    document.getElementById("ascii-result-encrypt").innerText = "";
    document.getElementById("ascii-result-decrypt").innerText = "";
}

// 重置文件输入
function resetFileInputs() {
    document.getElementById("file-input-encrypt").value = "";
    document.getElementById("file-input-decrypt").value = "";
    document.getElementById("file-result-encrypt").innerText = "";
    document.getElementById("file-result-decrypt").innerText = "";
}

//选择文件按钮
document.getElementById('custom-file-input-encrypt').addEventListener('click', function() {
    document.getElementById('file-input-encrypt').click();
});

document.getElementById('custom-file-input-decrypt').addEventListener('click', function() {
    document.getElementById('file-input-decrypt').click();
});



// 发送加密请求到后端
async function encrypt8Bit() {
    const plaintext = document.getElementById('bit8-plaintext').value;
    const key = document.getElementById('bit8-key').value;

    // 发送请求到后端
    const response = await fetch('http://127.0.0.1:8050/encrypt8Bit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            key: key,
            plaintext: plaintext,
        }),
    });
    const data = await response.json();
    console.log(data)
    document.getElementById('bit8-result').innerText = `加密后的密文是：${data.encrypted}`;
}

// 发送解密请求到后端
async function decrypt8Bit() {
    const ciphertext = document.getElementById('bit8-ciphertext').value;
    const key = document.getElementById('bit8-key-decrypt').value;

    // 发送请求到后端
    const response = await fetch('http://localhost:8050/decrypt8Bit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            key: key,
            ciphertext: ciphertext,
        }),
    });

    const data = await response.json();
    console.log(data)
    document.getElementById('bit8-result-decrypt').innerText = `解密后的明文是：${data.decrypted}`;
}

// ASCII 加密
async function encryptASCII() {
    const plaintext = document.getElementById('ascii-plaintext').value;
    const key = document.getElementById("ascii-key").value;
    const response = await fetch('http://localhost:8050/encrypt_ascii', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ plaintext: plaintext, key:key }),
    });
    const data = await response.json();
    console.log(data)
    document.getElementById('ascii-result-encrypt').innerText = `加密结果：${data.encrypted}`;
}

// ASCII 解密
async function decryptASCII() {
    const ciphertext = document.getElementById('ascii-ciphertext').value;
    const key = document.getElementById("ascii-key-decrypt").value;
    const response = await fetch('http://localhost:8050/decrypt_ascii', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ciphertext: ciphertext, key:key}),
    });
    const data = await response.json();
    console.log(data)
    document.getElementById('ascii-result-decrypt').innerText = `解密结果：${data.decrypted}`;
}

// 文件加密
async function encryptFile() {
    const fileInput = document.getElementById('file-input-encrypt');
    const key = document.getElementById("file-key").value;
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('key',key);
    const response = await fetch('http://localhost:8050/encrypt_file', {
        method: 'POST',
        body: formData,
    });

    const data = await response.json();
    console.log(data)
    document.getElementById('file-result-encrypt').innerText = `加密结果：${data.encrypted}`;
}

// 文件解密
async function decryptFile() {
    const fileInput = document.getElementById('file-input-decrypt');
    const key = document.getElementById("file-key-decrypt").value;
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('key',key);
    const response = await fetch('http://localhost:8050/decrypt_file', {
        method: 'POST',
        body: formData,
    });

    const data = await response.json();
    console.log(data)
    document.getElementById('file-result-decrypt').innerText = `解密结果：${data.decrypted}`;
}

// 暴力破解
async function violentSolve() {
    const plaintext = document.getElementById('violent-plaintext').value;
    const ciphertext = document.getElementById("violent-ciphertext").value;
    const response = await fetch('http://localhost:8050/bruteforce', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            plaintext: plaintext, 
            ciphertext: ciphertext, 
        }),
    });

    const data = await response.json();
    console.log(data)
    // document.getElementById('violent-result-encrypt').innerText = `找到的密钥：${data.key}, 用时：${data.time}s`;
    document.getElementById('violent-result-encrypt').innerHTML = `找到的密钥：<br>${data.key.replace(/\n/g, '<br>')}<br> 用时：${data.time}s`
}

