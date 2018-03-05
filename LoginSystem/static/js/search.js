/**
 * Created by chenchukun on 18/3/4.
 */

$('#search').on('click', function () {

    var keyword = $('#keyword').val().trim();

    if (keyword === '') {
        $.Prompt('输入不能为空');
        reutrn;
    }

    $.get('/api/search?keyword=' + keyword, function (data) {
        var obj = JSON.parse(data);
        console.log(obj);
        if (obj.retcode == 0) {
            $('#output').text(obj.data);
        }
        else {
            $.Prompt(obj.retmsg);
        }
    });
});

$('#push').on('click', function () {
    var message = $('#message').val();
    $.post('api/push', data = {'message': message}, function (data) {
        var obj = JSON.parse(data);
        console.log(obj);
        $.Prompt(obj.retmsg);
    });
});

var ws = new WebSocket('ws://' + window.location.host + '/push');
ws.onmessage = function(e) {
    console.log(e.data);
    if (e.data === 'heartbeat') {
        console.log(e.data);
    }
    else {
        $('#output').text(e.data);
    }
}

function heartbeat() {
    ws.send('heartbeat');
}

setInterval('heartbeat()', 30000);