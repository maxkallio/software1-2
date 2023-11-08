<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Route from starting address to school</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.min.css" integrity="sha512-dlfd5hn5Df+LpYJGvBy/RXLj/1xjl9/9iCq3f17dB/KeLwGrjoNKPQY92UbHJF1bX7DmQ2kxOSBmLf+1dCsg7w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
      #map {
        height: 500px;
      }
    </style>
  </head>
  <body>
    <form id="address-form">
      <label for="starting-address">Starting address:</label>
      <input type="text" id="starting-address" name="starting-address" required>
      <button type="submit">Get route</button>
    </form>
    <div id="map"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.min.js" integrity="sha512-4F9+KPgwxRnRUBHjK2J/8ex3+qNzBw40jNpWYJ8qXoqEmcUx1v46lW6O8TgkLE1nmTUpd6UH2ehU8bXSyDQ2jQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-polylinedecorator/1.6.0/leaflet.polylineDecorator.min.js" integrity="sha512-S7VZYvZ8S5BkHTr1jj/uzVxvz8q4W2Qn+ynZWdG5f5R8K5WVKt+/LGnzs+vh2axJQ8gLz/+znCcyYtdohMcH9A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script>
      var map = L.map('map').setView([60.2055, 24.6559], 13);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
          '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
          'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        tileSize: 512,
        zoomOffset: -1
      }).addTo(map);
      var routeLayer = L.geoJSON().addTo(map);

      document.getElementById('address-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var startingAddress = document.getElementById('starting-address').value;
        getRoute(startingAddress);
      });

      function getRoute(startingAddress) {
        var apiUrl = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql';
        var query = `
