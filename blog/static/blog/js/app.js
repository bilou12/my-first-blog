app = angular.module('baseApp', [])

debugger;

app.controller('baseController', function($scope) {
    var self = this;

    self.result = undefined;

    self.displayPopUpConnexion = function(){
        alert("You clicked the button using AngularJs!");
        debugger;
        $('#modalConnexion').modal({
            show: 'true'
        });
    };

    self.inscrire = function(){
        alert("You clicked the button using AngularJs!");
        debugger;
    };

    debugger;
    $.ajax({
            url: "http://rest-service.guides.spring.io/greeting"
        }).then(function(data) {
        debugger;
//       $('.greeting-id').append(data.id);
//       $('.greeting-content').append(data.content);
        self.result = data;
        debugger;
    });

  });

//app.controller('inscriptionController', function($scope){
//    var self = this;
//    debugger;
//    self.inscrire = function(){
//        alert("You clicked the button using AngularJs!");
//        debugger;
//    };
//  });