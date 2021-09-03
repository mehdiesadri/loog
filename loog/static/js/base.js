function notification_click(id, url) {
    $.ajax({
        url: `/api/notifications/v1/notifications/${id}/`,
        method: 'PATCH',
        data: {'read': true},
        success: function (data) {
            if (url !== 'null')
                window.location.href = url;
            else {
                $("#notification_"+id).remove();
            }
        },
        error: function (error) {
            console.error(error);
        }
    });
}


function add_notification(notification) {
    $("#notificationList").prepend(`<a id="notification_${notification.id}" onclick="notification_click(${notification.id}, '${notification.url}');" class="list-group-item list-group-item-action">
                                    <div class="row align-items-center">
                                        <div class="col-auto">
                                            <!-- Avatar -->
                                            <img alt="Image placeholder" src="${notification.icon_url || '/static/img/brand/loog.png'}"
                                                 class="avatar rounded-circle">
                                        </div>
                                        <div class="col ml--2">
                                            <div class="d-flex justify-content-between align-items-center">
                                                <div>
                                                    <h4 class="mb-0 text-sm">${notification.title}</h4>
                                                </div>
                                                <div class="text-right text-muted">
                                                    <small>${new Date(notification.created_at).toLocaleString("en-US")}</small>
                                                </div>
                                            </div>
                                            <p class="text-sm mb-0">${notification.body}</p>
                                        </div>
                                    </div>
                                </a>`);
}


$('document').ready(function () {
    // Document is ready.
    console.log("Seyyed Ali Ayati");
    $(".alert-error").toggleClass('alert-error', 'alert-danger');

    // Setup AJAX
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        url: '/api/notifications/v1/notifications/',
        method: 'GET',
        success: function (data) {
            $("#notificationCount").text(data.length);
            data.forEach(notification => {
                add_notification(notification);
            });
        },
        error: function (error) {
            console.error(error);
        }
    });

});


const notificationSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/notifications/'
);

notificationSocket.onopen = function (e) {
    console.log("Opened...");
}

notificationSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);

    switch (data.type) {
        case 'system_message':
            if (data.head === "REDIRECT") {
                if (window.location.href !== data.url) {
                    window.location.href = data.url;
                }
            }
            break;

        case 'notification_message':
            add_notification(data);
            break;

        default:
            console.log(data);
            break;
    }
}

notificationSocket.onclose = function (e) {
    console.log("The socket closed....");
    console.log(e);
}