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

let logInForm, createForm, homeLink, enterLink, exitLink, formSubmit, formTitle, content, formModal,
    usernameInput, passwordInput, authorInput, textInput, emailInput, textUpdateInput, statusInput,
    ratingInput, createLink, updateForm, commentAddLink;


function setUpGlobalVars() {
    logInForm = $('#login_form');
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
    textInput = $('#text_input');
    emailInput = $('#email_input');
    textUpdateInput = $('#text_update_input');
    statusInput = $('#status_input');
    ratingInput = $('#rating_input');
    commentAddLink = $('#comment_add_link');
}


function setUpAddComment() {
    createForm.on('submit', function(event) {
        event.preventDefault();
        let request = makeRequest(
            'quotes',
            'post',
            checkAuthQuotes(),
            {"text": textInput.val(), "author_name": authorInput.val(), "author_email": emailInput.val()});
        request.done(function(data, status, response) {
        console.log('Quote added');
    }).fail(function(response, status, message) {
        console.log('Could not add QUote');
        console.log(response.responseText);
    });
        $('#form_modal').modal('toggle');
    });

    commentAddLink.on('click', function(event) {
        event.preventDefault();
        formSubmit.off('click');
        formSubmit.on('click', function(event) {
            createForm.submit();
        });
    });
}



$(document).ready(function() {
    setUpGlobalVars();
    console.log('I have loaded');

});

// function saveToken(token) {
//     localStorage.setItem('authToken', token);
// }
//
// function getToken() {
//     return localStorage.getItem('authToken');
// }
//
// function removeToken() {
//     localStorage.removeItem('authToken');
// }

// function logIn(username, password) {
//     const credentials = {username, password};
//     let request = makeRequest('login', 'post', false, credentials);
//     request.done(function(data, status, response) {
//         console.log('Received token');
//         saveToken(data.token);
//         enterLink.addClass('d-none');
//         exitLink.removeClass('d-none');
//     }).fail(function(response, status, message) {
//         console.log('Could not get token');
//         console.log(response);
//     });
// }

// function logOut() {
//     let request = makeRequest('logout', 'post', true);
//     request.done(function(data, status, response) {
//         console.log('Cleaned token');
//         removeToken();
//         enterLink.removeClass('d-none');
//         exitLink.addClass('d-none');
//     }).fail(function(response, status, message) {
//         console.log('Could not clean token');
//         console.log(response.responseText);
//     });
// }




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

// function setHome() {
//     homeLink.on('click', function (event) {
//         event.preventDefault();
//         getQuotes();
//     });
// }

// function setUpCreate() {
//     createForm.on('submit', function(event) {
//         event.preventDefault();
//         let request = makeRequest(
//             'quotes',
//             'post',
//             checkAuthQuotes(),
//             {"text": textInput.val(), "author_name": authorInput.val(), "author_email": emailInput.val()});
//         request.done(function(data, status, response) {
//         console.log('Quote added');
//     }).fail(function(response, status, message) {
//         console.log('Could not add Quote');
//         console.log(response.responseText);
//     });
//         $('#form_modal').modal('toggle');
//     });
//
//     createLink.on('click', function(event) {
//         event.preventDefault();
//         createForm.removeClass('d-none');
//         logInForm.addClass('d-none');
//         updateForm.addClass('d-none');
//         formTitle.text('New Quote');
//         formSubmit.text('Submit');
//         formSubmit.off('click');
//         formSubmit.on('click', function(event) {
//             createForm.submit();
//         });
//     });
// }



