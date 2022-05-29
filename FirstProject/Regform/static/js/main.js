/*Невидимость для поля Log in на стр.  Regist*/
(function($) {
    $('.signin-image-link').on('click', function(){
        $('.signup-content').css('display', 'none'), 
            $('.signin-content').css('display', 'block');

        console.log('hi!')
    })

})(window.jQuery);

/*Невидимость для поля Regist на стр.  Log in*/
(function($) {
    $('.signup-image-link').on('click', function(){
        $('.signin-content').css('display', 'none'),
            $('.signup-content').css('display', 'block');

        console.log('hi!')
    })

})(window.jQuery);

/*Проверка совпадают ли пароли */
function checkPasswordMatch() {
    var password = $("#pass").val();
    var confirmPassword = $("#re_pass").val();

    if (confirmPassword != password)
        $("#divCheckPasswordMatch").html("Passwords do not match!");
   
    else
        $("#divCheckPasswordMatch").html("Passwords match."), style.color = "red" ;
    
}

$(main).ready(function () {
   $("#pass, #re_pass").keyup(checkPasswordMatch);
})

$('body').on('click', '.password-control', function(){
	if ($('#pass').attr('type') == 'password'){
		$(this).addClass('view');
		$('#pass').attr('type', 'text');
	} else {
		$(this).removeClass('view');
		$('#pass').attr('type', 'password');
	}
	return false;
});

// function checkPassword(form) {
//     var password = form.pass.value; // Получаем пароль из формы
//     var s_letters = "qwertyuiopasdfghjklzxcvbnm"; // Буквы в нижнем регистре
//     var b_letters = "QWERTYUIOPLKJHGFDSAZXCVBNM"; // Буквы в верхнем регистре
//     var digits = "0123456789"; // Цифры
//     var specials = "!@#$%^&*()_-+=\|/.,:;[]{}"; // Спецсимволы
//     var is_s = false; // Есть ли в пароле буквы в нижнем регистре
//     var is_b = false; // Есть ли в пароле буквы в верхнем регистре
//     var is_d = false; // Есть ли в пароле цифры
//     var is_sp = false; // Есть ли в пароле спецсимволы
//     for (var i = 0; i < password.length; i++) {
//       /* Проверяем каждый символ пароля на принадлежность к тому или иному типу */
//       if (!is_s && s_letters.indexOf(password[i]) != -1) is_s = true;
//       else if (!is_b && b_letters.indexOf(password[i]) != -1) is_b = true;
//       else if (!is_d && digits.indexOf(password[i]) != -1) is_d = true;
//       else if (!is_sp && specials.indexOf(password[i]) != -1) is_sp = true;
//     }
//     var rating = 0;
//     var text = "";
//     if (is_s) rating++; // Если в пароле есть символы в нижнем регистре, то увеличиваем рейтинг сложности
//     if (is_b) rating++; // Если в пароле есть символы в верхнем регистре, то увеличиваем рейтинг сложности
//     if (is_d) rating++; // Если в пароле есть цифры, то увеличиваем рейтинг сложности
//     if (is_sp) rating++; // Если в пароле есть спецсимволы, то увеличиваем рейтинг сложности
//     /* Далее идёт анализ длины пароля и полученного рейтинга, и на основании этого готовится текстовое описание сложности пароля */
//     if (password.length < 6 && rating < 3) text = "Простой";
//     else if (password.length < 6 && rating >= 3) text = "Средний";
//     else if (password.length >= 8 && rating < 3) text = "Средний";
//     else if (password.length >= 8 && rating >= 3) text = "Сложный";
//     else if (password.length >= 6 && rating == 1) text = "Простой";
//     else if (password.length >= 6 && rating > 1 && rating < 4) text = "Средний";
//     else if (password.length >= 6 && rating == 4) text = "Сложный";
//     alert(text); // Выводим итоговую сложность пароля
//     return false; // Форму не отправляем
//   }