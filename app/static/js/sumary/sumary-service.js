'use strict';

angular.module('review')
  .factory('Sumary', ['$resource', function ($resource) {
    return $resource('review/sumaries/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
