
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        arr = msg.number.split(',');

        val = arr[0];
        num_of_prod = arr[1];

        $('#val').html(val);
        $('#noo').html(num_of_prod);
    });

});