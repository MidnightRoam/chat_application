const roomName = JSON.parse(document.getElementById('json-roomname').textContent);

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
}

chatSocket.onclose = function(e) {
    console.log('onclose')
}