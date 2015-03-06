'use strict';

angular.module('api')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/mainpages', {
        templateUrl: 'views/mainpage/mainpages.html',
        controller: 'MainpageController',
        resolve:{
          resolvedMainpage: ['Mainpage', function (Mainpage) {
            return Mainpage.query();
          }]
        }
      })
    }]);
