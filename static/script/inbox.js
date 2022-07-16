let input_message = $('#input-message')
let message_body = $('.msg_card_body')
let send_message_form = $('#send-message-form')
const USER_ID = $('#logged-in-user').val()

let loc = window.location
let wsStart = 'ws://'

if (loc.protocol === 'https') {
  wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname

let imageBase64 = ""; // Base64形式に変換した画像を代入する変数

const imageInput = document.getElementById("image-input");


imageInput.addEventListener('change', (e) => {
  // 画像ファイルを取得し、画像データ(URL)を変数に代入
  const imageFile = e.target.files[0];
  const imageURL = window.URL.createObjectURL(imageFile);
  // img要素を作成し、src属性に画像のURLを指定
  const imageElement = new Image();
  imageElement.src = imageURL;

  imageElement.onload = function () {
    // canvas要素を作成し、img要素を描画
    const canvasElement = document.createElement('canvas');
    canvasElement.width = imageElement.width;
    canvasElement.height = imageElement.height;
    const canvasContext = canvasElement.getContext('2d');
    canvasContext.drawImage(imageElement, 0, 0);
    // canvas要素をbase64形式に変換
    imageBase64 = canvasElement.toDataURL("image/png");
  };
});

var socket = new WebSocket(endpoint)

var objDiv = document.getElementById("message-box");
objDiv.scrollTop = objDiv.scrollHeight;

socket.onopen = async function (e) {
  console.log('open', e)
  send_message_form.on('submit', function (e) {
    e.preventDefault()
    let message = input_message.val()
    let send_to = get_active_other_user_id()
    let thread_id = get_active_thread_id()

    let data = {
      'message': message,
      'sent_by': USER_ID,
      'send_to': send_to,
      'thread_id': thread_id,
      'image': imageBase64
    }
    data = JSON.stringify(data)
    socket.send(data)
    $(this)[0].reset()
    imageBase64 = ""
  })
}

socket.onmessage = async function (e) {
  console.log('message', e)
  let data = JSON.parse(e.data)
  let message = data['message']
  let sent_by_id = data['sent_by']
  let thread_id = data['thread_id']
  let time = data['datetime']
  let image = data['image']
  newMessage(message, sent_by_id, thread_id, time, image)

  var objDiv = document.getElementById("message-box");
  objDiv.scrollTop = objDiv.scrollHeight;
}

socket.onerror = async function (e) {
  console.log('error', e)
}

socket.onclose = async function (e) {
  console.log('close', e)
}


function newMessage(message, sent_by_id, thread_id, time, image) {
  if ($.trim(message) === '' && $.trim(image) === '') {
    return false;
  }
  let message_element;
  let chat_id = 'chat_' + thread_id
  if (sent_by_id == USER_ID) {
    message_element = `
        <div class="column is-narrow is-two-thirds-mobile is-offset-one-third-mobile is-two-thirds-tablet is-offset-one-third-tablet is-two-third-desktop is-offset-one-third-desktop is-offset-one-third-widescreen is-two-third-widescreen is-two-third-fullhd is-offset-one-third-fullhd">
                  <p>
                    <strong><small>${time}</small></strong>
                  </p>
                  <div class="box has-background-warning">
                    <div class="media-content">
                      <div class="content">
                        ${message}
                        <img src="${image}">
                      </div>
                    </div>
                  </div>
                </div>
	    `
  }
  else {
    message_element = `
        <div class="column is-narrow is-two-thirds-mobile is-two-thirds-tablet is-two-thirds-widescreen is-two-thirds-fullhd">
                  <p>
                    <strong><small>${time}</small></strong>
                  </p>
                  <div class="box has-background-grey-lighter">
                    <div class="media-content">
                      <div class="content">
                        ${message}
                        <img src="${image}">
                      </div>
                    </div>
                  </div>
                </div>
        `

  }

  let message_body = $('.messages-wrapper[chat-id="' + chat_id + '"] .msg_card_body')
  message_body.append($(message_element))
  var objDiv = document.getElementById("message-box");
  objDiv.scrollTop = objDiv.scrollHeight;
  input_message.val(null);
  imageBase64.val(null);
}


$('.contact-li').on('click', function () {
  $('.contacts .active').removeClass('active').removeClass('has-background-warning')
  $(this).addClass('active').addClass('has-background-warning')

  // message wrappers
  let chat_id = $(this).attr('chat-id')
  $('.messages-wrapper.is_active').removeClass('is_active').addClass('is-hidden')
  $('.messages-wrapper[chat-id="' + chat_id + '"]').addClass('is_active').removeClass('is-hidden')
})

function get_active_other_user_id() {
  let other_user_id = $('.messages-wrapper.is_active').attr('other-user-id')
  other_user_id = $.trim(other_user_id)
  return other_user_id
}

function get_active_thread_id() {
  let chat_id = $('.messages-wrapper.is_active').attr('chat-id')
  let thread_id = chat_id.replace('chat_', '')
  return thread_id
}