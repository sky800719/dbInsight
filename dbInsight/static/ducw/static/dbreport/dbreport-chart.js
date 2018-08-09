/**
 * 记录数少的查询结果表格
 */


/**
 * 初始化页面展现表格
 * @returns
 */
function logSwitchChart() {
  var logswitchDom = document.getElementById(logswitchChartID);
  var logswitchEChart = echarts.init(logswitchDom);
  var logswitchApp = {};
    
  logswitchApp.title = logswitchTitle;

  logswitchData = logswitchData.map(function (item) {
        return [item[1], item[0], item[2] || '-'];
  });

  var logswitchColor = ["#FF0000","#FF8000","#FFFF00","#00CC00","#CCFFCC"];
    
  logswitchOption = {
        tooltip: {
            position: 'top'
        },
        animation: false,
        grid: {
            height: '50%',
            y: '10%'
        },
        xAxis: {
            type: 'category',
            data: logswitchXAxis,
            splitArea: {
                show: true
            }
        },
        yAxis: {
            type: 'category',
            data: logswitchYAxis,
            splitArea: {
                show: true
            }
        },
        visualMap: {
            min: 0,
            max: 200,
            calculable: true,
            orient: 'horizontal',
            left: 'center',
            bottom: '25%',
            color:logswitchColor,
        },
        series: [{
            name: 'Punch Card',
            type: 'heatmap',
            data: logswitchData,
            label: {
                normal: {
                    show: true
                }
            },
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    };

  logswitchEChart.setOption(logswitchOption, true);
}