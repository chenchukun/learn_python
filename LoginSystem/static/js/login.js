/**
 * Created by chenchukun on 18/3/4.
 */

var emailRe = /^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$/;
var passwordRe = /.{6,16}/;
var userNameRe = /[a-zA-z]\w{0,9}/;

$('#login').on('click', function () {
    var email = $('#login_email').val().trim();
    var password = $('#login_password').val().trim();

    if (! emailRe.test(email)) {
        $.Prompt('邮箱不合法');
        return;
    }
    if (! passwordRe.test(password)) {
        $.Prompt('密码不合法');
        return;
    }

    $.post('/api/login', {'email': email, 'password': password}, function (data) {
        var obj = JSON.parse(data);
        console.log(obj);
        $.Prompt(obj.retmsg);
        if (obj.retcode == 0) {
            $(location).attr('href', '/');
        }
    });
});

$('#register').on('click', function () {
    var email = $('#register_email').val().trim();
    var password = $('#register_password').val().trim();
    var username = $('#register_username').val().trim();

    if (! emailRe.test(email)) {
        $.Prompt('邮箱不合法');
        return;
    }
    if (! passwordRe.test(password)) {
        $.Prompt('密码不合法');
        return;
    }
    if (! userNameRe.test(username)) {
        $.Prompt('用户名不合法');
        return;
    }

    $.post('/api/register', {'email': email, 'password': password, 'username': username}, function (data) {
        var obj = JSON.parse(data);
        console.log(obj);
        $.Prompt(obj.retmsg);
        if (obj.retcode == 0) {
            $('#register_email').val('');
            $('#register_password').val('');
            $('#register_username').val('');
        }
    });
});
