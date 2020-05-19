const drawChart = (yData) => {
  const xData = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100];
  const chart = new Chart(xData, yData);
  chart.createGraph();
  console.log(numberOfValues);
};

const submitButton = document.getElementById('submit-button');
submitButton.addEventListener('click', (e) => {
  e.preventDefault();
  drawChart([0.0011920928955078125, 0.0, 0.0, 0.00095367431640625, 0.00095367431640625, 0.00095367431640625, 0.0, 0.0, 0.0, 0.00095367431640625, 0.0, 0.0, 0.0, 0.00095367431640625, 0.0, 0.0, 0.0, 0.0, 0.00095367431640625, 0.0, document.getElementById('user-input').value]);
});

