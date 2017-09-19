var svgWidth=600;
var svgHeight=600;
var dataSet = {{data}};
var pie = d3.pie();
var arc = d3.arc().innerRadius(0).outerRadius(280);

var pieElements = d3.select('#myCircle1')
.selectAll('path')
.data(pie(dataSet))

pieElements.enter()
.append('path')
.attr('class', 'pie')
.attr('d', arc)
.attr('transform', "translate("+svgWidth/2 + "," + svgHeight/2 + ")")
.style('fill', function(d,i){
    return['red', 'orange', 'yellow', 'green', 'blue'][i];
})

