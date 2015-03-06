'use strict';

angular.module('api')
  .factory('Mainpage', ['$resource', function ($resource) {
    return $resource('api/mainpages/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
