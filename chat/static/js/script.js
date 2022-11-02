const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);

// Создание вебсокета

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
);

chatSocket.onopen = (e) => {
    console.log('Client is connected')
}

chatSocket.onmessage = function(e) {
    console.log('onmessage')

    const data = JSON.parse(e.data);

    if (data.message) {
        let html = `
            <div class="left__message rounded">
            <p class="message__username">${data.username}</p>
            <p class="message__text">${data.message}</p></div>
            `

            document.querySelector('#chat-messages').innerHTML += html;

            scrollToBottom();
    } else {
        alert('The message was empty');
    }
}

chatSocket.onclose = function(e) {
    console.log('onclose')
}

// Отправка сообщения

document.querySelector('#chat-message-submit').onclick = (e) => {
    e.preventDefault();

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }));

    messageInputDom.value = '';

    return false;
}

// Скролл всегда будет следовать за последним сообщением

function scrollToBottom() {
    const objDiv =  document.querySelector('#chat-messages')
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();
