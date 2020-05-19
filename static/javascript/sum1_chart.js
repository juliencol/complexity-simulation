const drawChart = (yData) => {
  const xData = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60];
  const chart = new Chart(xData, yData);
  chart.createGraph();
  console.log(numberOfValues);
};

const submitButton = document.getElementById('submit-button');
submitButton.addEventListener('click', (e) => {
  e.preventDefault();
  drawChart([5, 10, document.getElementById('user-input').value]);
});