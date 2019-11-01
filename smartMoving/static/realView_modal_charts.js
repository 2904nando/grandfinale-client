$(document).ready(function(){
  var ctx = $("#chartTempT1")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Temperatura',
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
        borderColor: 'rgba(255, 99, 132, 1)',
        data: [25, 27, 27, 28, 26],
        borderWidth: 1
      }]
    }
  })
  var ctx = $("#chartUmidT1")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Umidade',
        backgroundColor: 'rgba(110, 97, 255, 0.6)',
        borderColor: 'rgba(110, 97, 255, 1)',
        data: [85, 87, 89, 86, 84],
        borderWidth: 1
      }]
    }
  })


  var ctx = $("#chartTempT2")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Temperatura',
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
        borderColor: 'rgba(255, 99, 132, 1)',
        data: [25, 27, 27, 28, 26],
        borderWidth: 1
      }]
    }
  })
  var ctx = $("#chartUmidT2")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Umidade',
        backgroundColor: 'rgba(110, 97, 255, 0.6)',
        borderColor: 'rgba(110, 97, 255, 1)',
        data: [85, 87, 89, 86, 84],
        borderWidth: 1
      }]
    }
  })


  var ctx = $("#chartTempT3")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Temperatura',
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
        borderColor: 'rgba(255, 99, 132, 1)',
        data: [25, 27, 27, 28, 26],
        borderWidth: 1
      }]
    }
  })
  var ctx = $("#chartUmidT3")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Umidade',
        backgroundColor: 'rgba(110, 97, 255, 0.6)',
        borderColor: 'rgba(110, 97, 255, 1)',
        data: [85, 87, 89, 86, 84],
        borderWidth: 1
      }]
    }
  })


  var ctx = $("#chartTempT4")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Temperatura',
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
        borderColor: 'rgba(255, 99, 132, 1)',
        data: [25, 27, 27, 28, 26],
        borderWidth: 1
      }]
    }
  })
  var ctx = $("#chartUmidT4")[0].getContext('2d');
  var chartTempT1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['07:30', '08:00', '08:30', '09:00', '09:30'],
      datasets: [{
        label: 'Umidade',
        backgroundColor: 'rgba(110, 97, 255, 0.6)',
        borderColor: 'rgba(110, 97, 255, 1)',
        data: [85, 87, 89, 86, 84],
        borderWidth: 1
      }]
    }
  })
})
