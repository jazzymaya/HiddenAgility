


   function openMap() {
     document.getElementById("MyMap").style.display = "block";
   }
   
   function closeMap() {
     document.getElementById("MyMap").style.display = "none";
   }
   
  
   var map;
   var infoWindow;

   function initMap() {
      let location =new Object();
      navigator.geolocation.getCurrentPosition(function(pos){
           location.lat = pos.coords.latitude;
           location.long = pos.coords.longitude;
           map = new google.maps.Map(document.getElementById("map"),{
             center: {lat: location.lat, lng: location.long},
             zoom: 11
           });
           getHospitals(location);  
      });

    function getHospitals(location) {
      var pyrmont = new google.maps.LatLng(location.lat, location.long);
      var request = {
        location: pyrmont,
        radius: '10000',
        type: ['hospital']

      };
      service = new google.maps.places.PlacesService(map);
      service.nearbySearch(request,callback);
    }

    function callback(results, status) {
      if(status == google.maps.places.PlacesServiceStatus.OK) {
        for (var i =0; i < results.length; i++){
          var place = results[i];
          let content = 
          `<h3>${place.name}</h3>
          <h4>${place.vicinity}</h4>`;

          var marker = new google.maps.Marker({
            position: place.geometry.location,
            map: map,
            title: place.name
          });

          var infowindow = new google.maps.InfoWindow({
            content: content
          });

          bindInfoWindow(marker, map, infowindow, content);
          marker.setMap(map);
        }
      }
    }

    function bindInfoWindow(marker, map, infowindow, html) {
      marker.addListener('click', function(){
        infowindow.setContent(html);
        infowindow.open(map, this);
      });
    }
   
    infoWindow = new google.maps.InfoWindow;

if(navigator.geolocation){
navigator.geolocation.getCurrentPosition(function(p){
 var position = {
   lat: p.coords.latitude,
   lng: p.coords.longitude
 };
 infoWindow.setPosition(position);
 infoWindow.setContent('You are here');
 infoWindow.open(map);
}, function () {
 handleLocationError('Geolocation service failed', map.center());
})
} else {
handleLocationError('No geolocation available', map.center());
}
   
     
   }

   function handleLocationError (content, position) {
     infoWindow.setPosition(position);
     infoWindow.setContent(content);
     infoWindow.open(map);
   }
   
 