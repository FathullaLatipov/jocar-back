$(document).ready(function () {
  // Form Submit
  $("#formID").submit(() => {
    console.log("hello world");
    const token = "5180471767:AAFWq1Z8Qd-ldeNbBJmqJaeCSlrddyIdueY";
    const chat_id = "-628715004";

    var formID = $(this);
    var message = $(formID).find(".number").val();
    var fname = $(formID).find(".fname").val();
    var lname = $(formID).find(".lname").val();


    const txt = JSON.stringify(
      `<b>First Name:</b> ${fname}%0A <b>Last Name:</b> ${lname}%0A <b>Message:</b> ${message}%0A `
    ).split('"')[1];
    console.log(txt);
    console.log(
      `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&parse_mode=html&text=${txt}`
    );

    $.ajax({
      type: "POST",
      url: `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&parse_mode=html&text=${txt}`,
      data: formID.serialize(),
      success: function (data) {
        console.log(data);
        //  Shows modal window  / Вывод модальное окно с уведомлением, об успешной отправке
        // $("#exampleModalCenter").modal("show");
        alert("Message is sent successfully");
        // Reload Page
        setTimeout(function () {
          document.location.href = "/home/home";
        }, 0001);
      },
      error: function (jqXHR, text, error) {
        // TO DO : Message on error
      },
    });
    return false;
  });
});
