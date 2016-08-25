var labels = ["09:54:02", "09:53:02", "09:52:02", "09:51:02", "09:50:02", "09:49:02", "09:48:03"],
    humidity = [57, 57, 57, 57.1, 57, 57, 57],
    illuminance = [0.2, 0.1, 0.2, 0.2, 0.1, 0.3, 0.2],
    objtemp = [22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5],
    ambtemp = [22.7, 22.7, 22.7, 22.7, 22.6, 22.7, 22.7];

/*var labels = [],
    timestamps = [],
    humidity = [],
    illuminance = [],
    objtemp = [],
    ambtemp = [],
    date1 = "",
    date2 = "";

function fetchData() {

    $.getJSON("http://127.0.0.1:5000/api/byproperty/all/100", function (data) {
        $(data.reverse()).each(function (index) {
            timestamps.push(data[index].timestamp);
            humidity.push(data[index].humidity);
            illuminance.push(data[index].illuminance);
            ambtemp.push(data[index].ambtemp);
            objtemp.push(data[index].objtemp);
        });
        
        $(timestamps).each(function (index) {
            labels.push(timestamps[index].split(" ")[1]);
        });

        date1 = timestamps[0].split(" ")[0];
        date2 = timestamps[timestamps.length - 1].split(" ")[0];
    });
    
}*/

function drawHumidity() {

    var dataset = [{
        label: "Relative Luftfeuchtigeit in %",
        fill: false,
        data: humidity,
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.4)",
        pointBorderColor: "rgba(75,192,192,1)",
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1
    }],
        data = {
            labels: labels,
            datasets: dataset
        },
        ctx = document.getElementById("humidity"),
        humidityChart = new Chart(ctx, { type: 'line', data: data });
}

function drawIlluminance() {

    var dataset = [{
        label: "Lichtstärke in Lux",
        fill: false,
        data: illuminance,
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.4)",
        pointBorderColor: "rgba(75,192,192,1)",
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1
    }],
        data = {
            labels: labels,
            datasets: dataset
        },
        ctx = document.getElementById("illuminance"),
        illuminanceChart = new Chart(ctx, { type: 'line', data: data });
}

function drawAmbientTemperature() {

    var datasets = [{
        label: "Umgebungstemperatur in °C",
        fill: false,
        data: ambtemp,
        borderColor: "rgba(90,1,192,1)",
        backgroundColor: "rgba(90,1,192,0.4)",
        pointBorderColor: "rgba(90,1,192,1)",
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1
    }],
        data = {
            labels: labels,
            datasets: datasets
        },
        ctx = document.getElementById("ambientTemperatur"),
        ambientTemperaturChart = new Chart(ctx, { type: 'line', data: data });
}

function drawObjectTemperatur() {

    var datasets = [{
        label: "Objekttemperatur in °C",
        fill: false,
        data: objtemp,
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.4)",
        pointBorderColor: "rgba(75,192,192,1)",
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1
    }],
        data = {
            labels: labels,
            datasets: datasets
        },
        ctx = document.getElementById("objectTemperatur"),
        objectTemperaturChart = new Chart(ctx, { type: 'line', data: data });
}

window.onload = function () {
//    fetchData();
    drawHumidity();
    drawIlluminance();
    drawAmbientTemperature();
    drawObjectTemperatur();
};