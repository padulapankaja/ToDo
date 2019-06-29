var app = angular.module('toDo', []);
app.controller('toDoController', function ($scope, $http) {
    //$scope.todoList = [{todoText:'Finish this app', done: false}];
    $http.get('/todo/api/').then(function (response) {
        $scope.todoList = [];
        for (var i = 0; i < response.data.length; i++) {
            var todo = {};
            todo.todoText = response.data[i].text;
            todo.done = response.data[i].done;
            todo.id = response.data[i].id;
            todo.cuDate = response.data[i].cuDate;
            todo.expDate = response.data[i].expDate;

            $scope.todoList.push(todo);
        }
        console.log(response.data);
    });
    $scope.saveData = function () {
        var data = { text: $scope.todoInput, expDate: $scope.checkOut, cuDate: $scope.cuDate, done: false };
        $http.put('/todo/api/', data);
    };
    $scope.todoAdd = function () {
        $scope.todoList.push({ todoText: $scope.todoInput, expDate: $scope.checkOut, cuDate: $scope.cuDate, done: false });
        $scope.todoInput = '';
    };
    $scope.remove = function () {
        var oldList = $scope.todoList;
        $scope.todoList = [];
        angular.forEach(oldList, function (todo) {
            if (todo.done) {
                // $scope.todoList.push(tabeldone);
                $http.delete('/todo/api/' + todo.id + '/');
            }
            else {
                $scope.todoList.push(todo);
            }
        });
    }
});

// cd 

// function isValidDate(expDate) {
//     var temp = date.split('/');
//     var d = new Date(temp[2] + '/' + temp[0] + '/' + temp[1]);
//     return (d && (d.getMonth() + 1) == temp[0] && d.getDate() == Number(temp[1]) && d.getFullYear() == Number(temp[2]));
// }


// Search function 
// $(document).ready(function(){
//     $("#myInput").on("keyup", function() {
//       var value = $(this).val().toLowerCase();
//       $("#myTable tr").filter(function() {
//         $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
//       });
//     });
//   });
    // window.onunload = function() { debugger; }
    // INSERT INTO tabeldone (id,text,done)
    // SELECT id, text, done
    // FROM todo_todo