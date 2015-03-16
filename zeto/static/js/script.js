var app;

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