'use strict';

angular.module('api')
  .controller('MainpageController', ['$scope', '$modal', 'resolvedMainpage', 'Mainpage',
    function ($scope, $modal, resolvedMainpage, Mainpage) {

      $scope.mainpages = resolvedMainpage;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.mainpage = Mainpage.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Mainpage.delete({id: id},
          function () {
            $scope.mainpages = Mainpage.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Mainpage.update({id: id}, $scope.mainpage,
            function () {
              $scope.mainpages = Mainpage.query();
              $scope.clear();
            });
        } else {
          Mainpage.save($scope.mainpage,
            function () {
              $scope.mainpages = Mainpage.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.mainpage = {
          
          "test": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var mainpageSave = $modal.open({
          templateUrl: 'mainpage-save.html',
          controller: MainpageSaveController,
          resolve: {
            mainpage: function () {
              return $scope.mainpage;
            }
          }
        });

        mainpageSave.result.then(function (entity) {
          $scope.mainpage = entity;
          $scope.save(id);
        });
      };
    }]);

var MainpageSaveController =
  function ($scope, $modalInstance, mainpage) {
    $scope.mainpage = mainpage;

    

    $scope.ok = function () {
      $modalInstance.close($scope.mainpage);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
