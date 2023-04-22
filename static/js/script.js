let comments = [];
loadComments();

document.getElementById('comment-add').onclick = function(){
    let commentName = document.getElementById('comment-name');
    let commentBody = document.getElementById('comment-body');
    if (commentName.value.length > 0 && commentBody.value.length > 0) {
        let comment = {
            name : commentName.value,
            body : commentBody.value,
            time : timeConverter(Math.floor(Date.now() / 1000))
        }
        commentName.value = '';
        commentBody.value = '';
        comments.push(comment);
        saveComments();
        showComments();
    }
}

function saveComments() {
  fetch('/comments', {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'    },
    body: JSON.stringify(comments)
  })
  .then(response => response.json())
  .catch(error => console.error('Ошибка:', error));
}

function loadComments() {
  fetch('/comments', {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'    },
    body: JSON.stringify(comments)
  })
  .then(response => response.json())
  .then(data => {
      comments = data;
      showComments()
  })
  .catch(error => console.error('Ошибка:', error));
}

function showComments (){
    let commentField = document.getElementById('comment-field');
    let out = '';
    comments.forEach(function(item){
        out += `<p class="text-right small"><em>${timeConverter(item.time)}</em></p>`;
        out += `<p class="text-left text-block-1" role="alert"><strong>${item.name}</strong></p>`;
        out += `<p class="alert alert-success text-block-1" role="alert">${item.body} </p>`;
    });
    commentField.innerHTML = out;
}

function timeConverter(UNIX_timestamp){
    var a = new Date(UNIX_timestamp * 1000);
    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var year = a.getFullYear();
    var month = months[a.getMonth()];
    var date = a.getDate();
    var hour = a.getHours();
    var min = a.getMinutes();
    var sec = a.getSeconds();
    var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
    return time;
  }

function scrollTopAnimated() {
    $('html, body').animate({scrollTop: 0}, 600);
}

function scrollDownAnimated() {
    $('html, body').animate({scrollTop: $(document).height() - $(window).height()}, 600);
}

window.onload=function(){
     window.scrollTo(0,document.body.scrollHeight);
}