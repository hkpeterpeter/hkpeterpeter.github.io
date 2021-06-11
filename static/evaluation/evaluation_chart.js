// Try to port my D3 Observable notebook to a standalone web page
//  https://observablehq.com/@hkpeterpeter/experiment-0001-teaching-evaluation-donut-chart

function evalulation_chart(target, ratingString) {

    function datum(r, c) {
        return {rating: r, count: c};
    }

    var ratings = ["Very Good", "Good", "Average", "Bad", "Very Bad"];
    var data = ratingString.split(",").map( (d, i) => datum( ratings[i], +d)  );
    var totalCount = data.map(d => d.count).reduce( (a,b) => a+b, 0); // sum the count
    var colors = [ 
        '#57e32c', // Very well 
        '#b7dd29', 
        '#ffe234', 
        '#ffa534', 
        '#ff4545'  // Poorly
    ];
    var colorScale = d3.scaleOrdinal( data.map(d => d.rating), colors );
    var width = 550;
    var height = 500;

    var svg = d3.select(target)
    //.attr("width", width)
    //.attr("height", height);
    .attr("viewBox", `0 0 ${width} ${height}`); 

   
    
    var arc = d3.arc()
        .innerRadius( 0.5 * height / 2)
        .outerRadius( 0.85 * height / 2);
    var pie = d3.pie()
        .padAngle(.01)
        .value( d => d.count);
    var labelArcs = d3.arc()
        .innerRadius( 0.95 * height / 2)
        .outerRadius( 0.95 * height / 2);
    var pieArcs = pie(data).filter( d => d.value > 0) // only keep items with value>0

    

   


    svg.append('g')
        .attr('transform', `translate(${width/2},${height/2})`)
        .selectAll('path')
        .data(pieArcs)
        .join('path')
        .style('fill', d => colorScale( d.data.rating ))
        .attr('d', arc);

    var text = svg.append('g')
        .attr('transform', `translate(${width/2},${height/2})`)
        .selectAll('text')
        .data(pieArcs) // fix: only keep labels with +ve count/percentage
        .join('text')
        .attr('transform', d => `translate(${ labelArcs.centroid(d) })`)
        .attr('text-anchor', 'middle');

        text.selectAll('tspan')
            // 1
            .data( d => [ 
            d.data.rating, 
            (d.data.count/totalCount*100).toFixed(0) + "%"
            ])
            // 2
            .join('tspan')
            .attr('x', 0)
            .style('font-family', 'sans-serif')
            .style('font-size', 12)
            .style('font-weight', (d,i) => i ? undefined : 'bold')
            .style('fill', '#222') 
            //3
            .attr('dy', (d,i) => i ? '1.2em' : 0 )
            .text(d => d);

        var bigText = svg.append('text')
        .attr('transform', `translate(${width/2},${height/2})`)
        .attr('text-anchor', 'middle');

        bigText.selectAll('tspan')
            .data( ["Accessed by", d3.format(",")(totalCount), "students"] )
            .join('tspan')
            .attr('x', 0)
            .attr('y', -30)
            .attr('font-size', 20)
            .style('font-weight', (d,i) => i!==1 ? 'lighter' : 'bold')
            .style('font-style', (d,i) => i!==1 ? 'italic': 'normal')
            .attr('dy', (d,i) => i ? (1.5*i) + 'em' : 0)
            .text( d => d );

}