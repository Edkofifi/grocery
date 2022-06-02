var xValues = ["Jan","Feb","Mar","April","Jun","July","Aug","Sept","Oct","Nov","Dec"]; 

new Chart("productmetrix", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{ 
      label: 'orders',
      data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478,3000,3800],
      borderColor: "red",
      fill: false
    }, { 
      label: 'completed',
      data: [1600,1700,1700,1900,2000,2700,3500,4800,6000,7000,800,1000],
      borderColor: "green",
      fill: false
    }, { 
      label: 'pending',
      data: [300,700,2000,5000,6000,4000,2000,1000,200,100,80,60],
      borderColor: "blue",
      fill: false
    }]
  },
  options: {
    legend: {display: true}
  }
});

var xValues = ["Accra", "Central", "Ashanti", "Eastern", "Western"];
var yValues = [55, 49, 44, 24, 15];
var barColors = ["red", "green","blue","orange","brown"];

new Chart("regional_chat", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Distributional Centers"
    }
  }
});

var xValues = ["Total", "Instock", "Out-stock",];
var yValues = [55, 49, 44,];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797"
];

new Chart("stocks", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  }
});

var xValues = ["Total", "Instock", "Out-stock",];
var yValues = [55, 49, 44,];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797"
];

new Chart("stocks_statistics", {
  type: "doughnut",
  data: {
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  }
});

var xValues = ["Total", "Instock", "Out-stock",];
var yValues = [55, 49, 44,];
var barColors = [
  "red",
  "blue",
  "green"
];

new Chart("Orders", {
  type: "doughnut",
  data: {
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  }
});

var xValues = ["Total", "Instock", "Out-stock",];
var yValues = [55, 49, 44,];
var barColors = [
  "red",
  "blue",
  "green"
];

new Chart("Completed", {
  type: "pie",
  data: {
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  }
});

var xValues = ["Total", "Instock", "Out-stock",];
var yValues = [55, 49, 44,];
var barColors = [
  "red",
  "blue",
  "green"
];

new Chart("processing", {
  type: "pie",
  data: {
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  }
});

var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
var yValues = [55, 49, 44, 24, 35];
var barColors = ["red", "green","blue","orange","brown"];

new Chart("visitors", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false}
  }
});