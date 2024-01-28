/*
482.4	0	As	0	125	250	375	500
2400	0.32	Ba	0	625	1250	1875	2500
78.25871581	0	Be	0	25	50	75	100
29.7	0	Cr	0	7.5	15	22.5	30
4700	0	Cu	0	1250	2500	3750	5000
20.68814406	0	Fluoride	0	6.25	12.5	18.75	25
630	0	Hg	0	162.5	325	487.5	650
237.5641798	0	Nitrate	0	62.5	125	187.5	250
9.49	0	Nitrite	0	2.5	5	7.5	10
320	0	Pb	0	87.5	175	262.5	350
110	0	Ra_Total	0	37.5	75	112.5	150
2809.89611	0	Se	0	750	1500	2250	3000
10	0.05	Tl	0	2.5	5	7.5	10
700	0	U	0	175	350	525	700
400	0.3	V	0	100	200	300	400
*/


AsCountChart
.width(250)
.height(250)
.dimension(AsDim)
.group(countPerAs)
.x(d3.scale.linear().domain([0, 500]))
.xUnits(function(){return 10;})
.elasticY(true)
.centerBar(true)
.barPadding(3)
.yAxisLabel('Count')
.margins({ top: 10, right: 20, bottom: 50, left: 50 });

BaCountChart
.width(250)
.height(250)
.dimension(BaDim)
.group(countPerBa)
.x(d3.scale.linear().domain([0, 2500]))
.xUnits(function(){return 10;})
.elasticY(true)
.centerBar(true)
.barPadding(3)
.yAxisLabel('Count')
.margins({ top: 10, right: 20, bottom: 50, left: 50 });

BeCountChart
.width(250)
.height(250)
.dimension(BeDim)
.group(countPerBe)
.x(d3.scale.linear().domain([0, 100]))
.xUnits(function(){return 10;})
.elasticY(true)
.centerBar(true)
.barPadding(3)
.yAxisLabel('Count')
.margins({ top: 10, right: 20, bottom: 50, left: 50 });

CrCountChart
.width(250)
.height(250)
.dimension(BeDim)
.group(countPerBe)
.x(d3.scale.linear().domain([0, 30]))
.xUnits(function(){return 10;})
.elasticY(true)
.centerBar(true)
.barPadding(3)
.yAxisLabel('Count')
.margins({ top: 10, right: 20, bottom: 50, left: 50 });

CuCountChart
.width(250)
.height(250)
.dimension(BeDim)
.group(countPerBe)
.x(d3.scale.linear().domain([0, 5000]))
.xUnits(function(){return 10;})
.elasticY(true)
.centerBar(true)
.barPadding(3)
.yAxisLabel('Count')
.margins({ top: 10, right: 20, bottom: 50, left: 50 });

FlCountChart
.width(250)
.height(250)
.dimension(BeDim)
.group(countPerBe)
.x(d3.scale.linear().domain([0, 25]))
.xUnits(function(){return 10;})
.elasticY(true)
.centerBar(true)
.barPadding(3)
.yAxisLabel('Count')
.margins({ top: 10, right: 20, bottom: 50, left: 50 });