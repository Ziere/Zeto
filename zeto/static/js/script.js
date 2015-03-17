var app;

app = angular.module('example.app.basic', []);

app.controller('AppController', [
  '$scope', '$http', '$timeout', function($scope, $http, $timeout) {

    var poll = function() {
        $timeout(function() {
            $scope.customers = [];
            $http.get('/customer/').then(function(result) {
                angular.forEach(result.data.results, function(item) {
                  $scope.customers.push(item);
                });
            });
            $scope.orderProp = 'name';
            poll();
        }, 5000);
    };
    poll();
  }
]);

app.directive('chart', function() {
    return {
        restrict: 'A',
        scope : {
            customers : '='  // '=' indicates 2 way binding
        },
    };
});

/* TESTING BASIC ANGULAR
app = angular.module('example.app.basic', []);

app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.customers = [];
    return $http.get('/customer/').then(function(result) {
      return angular.forEach(result.data.results, function(item) {
        return $scope.customers.push(item);
      });
    });
  }
]);
*/