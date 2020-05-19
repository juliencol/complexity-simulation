const drawChart = (yData) => {
  const xData = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100];
  const chart = new Chart(xData, yData);
  chart.createGraph();
  console.log(numberOfValues);
};

const submitButton = document.getElementById('submit-button');
submitButton.addEventListener('click', (e) => {
  e.preventDefault();
  drawChart([0.00095367431640625, 0.00095367431640625, 0.0019073486328125, 0.0030994415283203125, 0.0030994415283203125, 0.003814697265625, 0.005245208740234375, 0.0057220458984375, 0.007152557373046875, 0.0069141387939453125, 0.008106231689453125, 0.007867813110351562, 0.0152587890625, 0.009775161743164062, 0.012874603271484375, 0.013828277587890625, 0.014066696166992188, 0.06413459777832031, 0.016689300537109375, 0.018358230590820312, document.getElementById('user-input').value]);
});
