class Chart {
  constructor(xData, yData) {
    this.xData = xData;
    this.yData = yData;
  }

  createGraph() {
    const data = {
      labels: this.xData,
      series: [this.yData]
    }
    const options = {
      width: '600px',
      height: '360px'
    };
    new Chartist.Line('.ct-chart', data, options);
  }
}

