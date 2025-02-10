#Set Title
set title "Demand Calculation Runtime vs. KAVR Precision" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 10" offset 3,0
set xlabel 'Interval Size (us)' font "Times, 10" offset 0,0.5
set format y "%2.0t{/Symbol \264}10^{%L}"

set xrange [-20000:1020000]
set yrange [0.00005:500]
set logscale y 10

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
set key top left
set key spacing 1.1
set key width 3
set key reverse
set key Left
set key vertical
set key maxrows 4

set xtics 200000
set lmargin 7

#Name PDF
set output "exp1-precision-p5-12.pdf"

plot \
    '../../src/exp_data/var_precision-kavr24-p5-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 1 lc rgb "web-green" title "K-p5",\
    '../../src/exp_data/var_precision-kavr24-p6-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 2 lc rgb "web-green" title "K-p6",\
    '../../src/exp_data/var_precision-kavr24-p7-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 3 lc rgb "web-green" title "K-p7",\
    '../../src/exp_data/var_precision-kavr24-p8-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 4 lc rgb "web-green" title "K-p8",\
    '../../src/exp_data/var_precision-kavr24-p9-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 6 lc rgb "web-green" title "K-p9",\
    '../../src/exp_data/var_precision-kavr24-p10-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 8 lc rgb "web-green" title "K-p10",\
    '../../src/exp_data/var_precision-kavr24-p11-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 10 lc rgb "web-green" title "K-p11",\
    '../../src/exp_data/var_precision-kavr24-p12-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 12 lc rgb "web-green" title "K-p12",\
    '../../src/exp_data/var_precision-exact-p12-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 12 lc rgb "blue" title "E-p12",\
    '../../src/exp_data/var_precision-apx-p12-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 1:3 with linespoints pt 14 lc rgb "blue" title "A-p12"
