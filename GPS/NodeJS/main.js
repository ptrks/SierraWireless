var mysql = require('mysql');
var server = require('dgram').createSocket('udp4');
var moment = require('moment');

var SERVER_PORT = 21228;
var SERVER_HOST = '0.0.0.0';

var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'me',
    password : 'secret'
});

connection.connect(function(err) {
    if(err) {
        console.log('Cannot connect to database.  Error: '+err);
    } else {
        console.log('Connected to database successfully.');

    }
});

function updateGPS(ip,lat,lon) {
    var now = moment().format("YYYY-MM-DD HH:mm:ss");
    console.log(now);
    var queryString = 'UPDATE gps \
					   SET latitude = ?, longitude = ?, polltime = ? \
					   WHERE ip = ?';
    var query = connection.query(queryString, [lat, lon, now, id], function (err, result) {
        if (err) throw err;
        console.log("Updating " + id + " with lat: " + lat + " and lon: " + lon + "at " + now);
    });

}


function parseGPS(rawstring)
{
    var regex = /^>(\w)(\w{2})(\d{5})(\+|-)(\d{2})(\d{5})(\+|-)(\d{3})(\d{5})(\d{3})(\d{3})(\d)(\d)(?:;ID=(\w+))?;\*(\w+)<$/;
    var matches = [];
    var gps;
    var processedString = String(rawstring);
    matches = processedString.match(regex);
    if(matches)
    {
        gps = {
            "type":matches[0],
            "data":matches[1],
            "time":matches[2],
            "latitude":matches[4] + matches[5] + "." + matches[3],
            "longitude":matches[7] + matches[8] + "." + matches[6],
            "speed":matches[9],
            "heading":matches[10],
            "source":matches[11],
            "age":matches[12],
            "id":matches[13]
        };
    }
    else
    {
        gps = null;
    }

    return gps;
}

server.on('listening',function(){
    var address = server.address();
    console.log('UDP server listening on ' + address.address + ":" + address.port);
});

server.on('message',function(message,remote){
    var ipAddress = remote.address;
    var gpsData = parseGPS(message);
    console.log("Message from " + ipAddress);
    if (gpsData != null) {
        updateGPS(ipAddress,gpsData.latitude,gpsData.longitude);
    }
});



server.bind(SERVER_PORT,SERVER_HOST);
