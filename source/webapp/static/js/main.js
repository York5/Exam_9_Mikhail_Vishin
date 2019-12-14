const baseUrl = 'http://localhost:8000/api/v1/';

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function makeRequest(path, method, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json',
        headers: {'X-CSRFToken': csrftoken}
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    return $.ajax(settings);
}

let createForm, homeLink, enterLink, exitLink, formSubmit, formTitle, content, formModal,
    usernameInput, passwordInput, authorInput, commentTextInput, textUpdateInput,
    createLink, updateForm, commentAddLink, commentPhoto, commentUser;


function setUpGlobalVars() {
    createForm = $('#create_form');
    updateForm = $('#update_form');
    homeLink = $('#home_link');
    enterLink = $('#enter_link');
    createLink = $('#create_link');
    exitLink = $('#exit_link');
    formSubmit = $('#form_submit');
    formTitle = $('#form_title');
    content = $('#content');
    formModal = $('#form_modal');
    usernameInput = $('#username_input');
    passwordInput = $('#password_input');
    authorInput = $('#author_input');
    commentTextInput = $('#comment_text');
    textUpdateInput = $('#text_update_input');
    commentAddLink = $('#comment_add_link');
    commentPhoto = $('#comment_photo');
    commentUser = $('#comment_user');
}


function setUpAddComment() {
    createForm.on('submit', function(event) {
        event.preventDefault();
        let request = makeRequest(
            'comments',
            'post',
            {"text": commentTextInput.val(), "photo": commentPhoto.val(), "author": commentUser.val()});
        request.done(function(data, status, response) {
        console.log('Comment added!');
        $('#form_modal').modal('toggle');
    }).fail(function(response, status, message) {
        console.log('Could not add Comment');
        console.log(response.responseText);
    });
        $('#form_modal').modal('toggle');
    });

    formSubmit.off('click');
    formSubmit.on('click', function(event) {
        createForm.submit();
    });

}


$(document).ready(function() {
    setUpGlobalVars();
    setUpAddComment();
    console.log('I have loaded');
});



// function rateUp(id) {
//     let request = makeRequest('quotes/' + id + '/rate_up', 'post', false);
//     request.done(function(data, status, response) {
//         console.log('Rated up quote with id ' + id + '.');
//         $('#rating_' + id).text(data.rating);
//     }).fail(function(response, status, message) {
//         console.log('Could not rate up quote with id ' + id + '.');
//         console.log(response.responseText);
//     });
// }

function getQuotes() {
    let request = makeRequest('quotes', 'get', false);
    request.done(function(data, status, response) {
        console.log(data);
        content.html("");
        data.forEach(function(item, index, array) {
            content.append($(`<div class="card" id="quote_${item.id}">
                <p>${item.text}</p>
                <p id="rating_${item.id}">${item.rating}</p>
                <p><a href="#" class="btn btn-success" id="rate_up_${item.id}">+</a></p>
            </div>`));
            $('#rate_up_' + item.id).on('click', function(event) {
                console.log('click');
                event.preventDefault();
                rateUp(item.id);
            });
        });
    }).fail(function(response, status, message) {
        console.log('Could not get quotes.');
        console.log(response.responseText);
    });
}




