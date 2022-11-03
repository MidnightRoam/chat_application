const roomName = JSON.parse(document.getElementById('json-roomname').textContent);

// Создание вебсокета
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
);

// Подключение сокета
chatSocket.onopen = (e) => {
    console.log('Client is connected')
}

// Закрытие сокета
chatSocket.onclose = function(e) {
    console.log('onclose')
}
