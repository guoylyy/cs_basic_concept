'use strict';

angular.module('review')
  .controller('SumaryController', ['$scope', '$modal', 'resolvedSumary', 'Sumary',
    function ($scope, $modal, resolvedSumary, Sumary) {

      $scope.sumaries = resolvedSumary;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.sumary = Sumary.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Sumary.delete({id: id},
          function () {
            $scope.sumaries = Sumary.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Sumary.update({id: id}, $scope.sumary,
            function () {
              $scope.sumaries = Sumary.query();
              $scope.clear();
            });
        } else {
          Sumary.save($scope.sumary,
            function () {
              $scope.sumaries = Sumary.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.sumary = {
          
          "summary": "",
          
          "email": "",
          
          "want_name": "",
          
          "is_send": "",
          
          "myattr": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var sumarySave = $modal.open({
          templateUrl: 'sumary-save.html',
          controller: SumarySaveController,
          resolve: {
            sumary: function () {
              return $scope.sumary;
            }
          }
        });

        sumarySave.result.then(function (entity) {
          $scope.sumary = entity;
          $scope.save(id);
        });
      };
    }]);

var SumarySaveController =
  function ($scope, $modalInstance, sumary) {
    $scope.sumary = sumary;

    

    $scope.ok = function () {
      $modalInstance.close($scope.sumary);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
