#Set Title
set title "Demand Calculation Peak RAM vs. Accel" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Peak RAM Required (MB)' font "Times, 10" offset 3,0
set xlabel 'Precision' font "Times, 10" offset 0,0.5
# set format y "%2.0t{/Symbol \264}10^{%L}"
# set format y '2^{%L}'

# set xrange [4.5:12.5]
set yrange [-1:262144]
set logscale y 2

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
set output "exp3-accel-p5-12-mem.pdf"

plot \
    '../../src/exp_data/var_accel-kavr24-p5-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "." lc rgb "web-green" title "K-P05",\
    '../../src/exp_data/var_accel-kavr24-p6-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "-" lc rgb "web-green" title "K-P06",\
    '../../src/exp_data/var_accel-kavr24-p7-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "-." lc rgb "web-green" title "K-P07",\
    '../../src/exp_data/var_accel-kavr24-p9-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "--." lc rgb "web-green" title "K-P09",\
    '../../src/exp_data/var_accel-kavr24-p8-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "---." lc rgb "web-green" title "K-P08",\
    '../../src/exp_data/var_accel-kavr24-p10-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "...-" lc rgb "web-green" title "K-P10",\
    '../../src/exp_data/var_accel-kavr24-p11-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "..-" lc rgb "web-green" title "K-P11",\
    '../../src/exp_data/var_accel-kavr24-p12-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt "  ." lc rgb "web-green" title "K-P12",\
    '../../src/exp_data/var_accel-exact-p12-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt 4 lc rgb "red" title "E-p12",\
    '../../src/exp_data/var_accel-apx-p12-can-1s-memo-1-slnSeq-0-trace-1-AG.csv' every 4 using 8:($11/1048576) with lines dt 1 lc rgb "red" title "A-p12"