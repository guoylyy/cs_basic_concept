'use strict';

angular.module('review')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/sumaries', {
        templateUrl: 'views/sumary/sumaries.html',
        controller: 'SumaryController',
        resolve:{
          resolvedSumary: ['Sumary', function (Sumary) {
            return Sumary.query();
          }]
        }
      })
    }]);
