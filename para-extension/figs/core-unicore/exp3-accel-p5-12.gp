#Set Title
set title "Demand Calculation Runtime vs. Acceleration" font "Times, 14"

#Set Axis Markings
set xtics font "Times, 12"
set ytics font "Times, 12"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 12" offset 3,0
set xlabel 'Maximum Acceleraton (rpm/sec^2)' font "Times, 12" offset 0,0.5
# set xrange [5000:25000000]
set xrange [5000:1500000]
# set yrange [0.00001:15000]
set format y "%2.0t{/Symbol \264}10^{%L}"

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 12"

set key autotitle columnhead

#Set key
# set key at 5.75, 900
set key top left
# set key spacing 1.1
# set key width 4
set key reverse
set key Left
set key maxrows 5

# set xtics 1
set lmargin 8
set logscale x 10
set logscale y 10

#Name PDF
set output "exp3-accel-p5-12.pdf"

plot \
    '../../src/exp_data/var_accel-kavr24-p5-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "." lc rgb "web-green" title "K-P05",\
    '../../src/exp_data/var_accel-kavr24-p6-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "-" lc rgb "web-green" title "K-P06",\
    '../../src/exp_data/var_accel-kavr24-p7-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "-." lc rgb "web-green" title "K-P07",\
    '../../src/exp_data/var_accel-kavr24-p9-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "--." lc rgb "web-green" title "K-P09",\
    '../../src/exp_data/var_accel-kavr24-p8-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "---." lc rgb "web-green" title "K-P08",\
    '../../src/exp_data/var_accel-kavr24-p10-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "...-" lc rgb "web-green" title "K-P10",\
    '../../src/exp_data/var_accel-kavr24-p11-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "..-" lc rgb "web-green" title "K-P11",\
    '../../src/exp_data/var_accel-kavr24-p12-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt "  ." lc rgb "web-green" title "K-P12",\
    '../../src/exp_data/var_accel-exact-p12-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt 4 lc rgb "red" title "E-p12",\
    '../../src/exp_data/var_accel-apx-p12-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' every 4 using 8:3 with lines dt 1 lc rgb "red" title "A-p12"