// Отправка сообщения
const sendMessage = document.querySelector('#chat-message-submit').onclick = (e) => {
    e.preventDefault();

    const userName = JSON.parse(document.getElementById('json-username').textContent);
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
    const data = JSON.parse(e.data);
//    const messageElement = document.createElement('div')
    const userId = data['user_id'] // Получаем айди пользователя
    const loggedInUserId = JSON.parse(document.getElementById('user_id').textContent);

    console.log(userId);
    console.log(loggedInUserId);

    // Добавление классов в сообщение в зависимости от того, является ли пользователь получателем или отправителем
//    if (userId === loggedInUserId) {
//        messageElement.classList.add('right__message')
//    } else {
//        messageElement.classList.add('left__message')
//    }

//    chatMessages = document.querySelector('#chat-messages')
//    chatMessages.appendChild(messageElement)

    // Время сообщения
    const date = new Date();
    const timeMessage = `${date.getHours()}:${date.getMinutes()}`;

    if (data.message) {
        let html = `
            <div class="left__message rounded" id="message">
                <div class="message__container">
                    <p class="message__username">${data.username}</p>
                    <p class="message__text">${data.message}</p><br>
                </div>
                <div class="send__info" id="send-info">
                    <p class="message__date">${timeMessage}</p>
                    <img src="https://img.icons8.com/officel/512/checkmark.png" alt="" class="check__send" id="send-img">
                </div>
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
