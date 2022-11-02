const userName = JSON.parse(document.getElementById('json-username').textContent);

// Отправка сообщения
const sendMessage = document.querySelector('#chat-message-submit').onclick = (e) => {
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

// Фронт-энд вывод сообщений
chatSocket.onmessage = function(e) {
    console.log('onmessage')

    const data = JSON.parse(e.data);
    console.log(data);

    // Время сообщения
    const date = new Date();
    const timeMessage = `${date.getHours()}:${date.getMinutes()}`;


    if (data.message) {
        let html = `
            <div class="left__message rounded">
                <p class="message__username">${data.username}</p>

                <p class="message__text"><br>${data.message}</p>
                <p class="message__date">${timeMessage}</p>
            </div>
            `

            document.querySelector('#chat-messages').innerHTML += html;

            scrollToBottom();
    } else {
        alert('The message was empty');
    }
}

// Скролл всегда будет следовать за последним сообщением
function scrollToBottom() {
    const objDiv =  document.querySelector('#chat-messages')
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();
