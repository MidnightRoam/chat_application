// При клике на дверь в чате - делать переход на страницу с выбором чатов
const chatDoor = document.querySelector('#chat-door')
chatDoor.addEventListener('click', () => {
    window.location.replace("/chats/");
})
