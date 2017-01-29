$(document).ready(function() {
    debugger;
    $.ajax({
        url: "http://rest-service.guides.spring.io/greeting"
    }).then(function(data) {
        debugger;
       $('.greeting-id').append(data.id);
       $('.greeting-content').append(data.content);
    });
});