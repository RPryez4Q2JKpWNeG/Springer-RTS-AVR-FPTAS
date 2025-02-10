#Set Title
set title "Demand Calculation Peak RAM vs. Precision" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Peak RAM Required (MB)' font "Times, 10" offset 3,0
set xlabel 'Precision' font "Times, 10" offset 0,0.5
# set format y "%2.0t{/Symbol \264}10^{%L}"
# set format y '2^{%L}'

set xrange [4.5:12.5]
set yrange [-1:65536]
set logscale y 2

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
set key bottom left
set key spacing 1.1
set key width 3
set key reverse
set key Left
set key vertical
set key maxrows 4

set xtics 1
# set lmargin 7
#l,r,b,t
set margins 6.5,1,2.5,2

#Name PDF
set output "exp2-duration-p5-12-mem-single-line.pdf"

plot \
    '../../src/exp_data/var_duration-kavr24-p5-12-can-2.0e7-memo-1-slnSeq-0-trace-1-AG.csv'  using 10:($11/1048576) with linespoints pt 9 lc rgb "web-green" title "CAN-KAVR",\
    '../../src/exp_data/var_duration-kavr24-p5-12-gen-2.0e7-memo-1-slnSeq-0-trace-1-AG.csv'  using 10:($11/1048576) with linespoints pt 8 lc rgb "blue" title "GEN-KAVR",\
    '../../src/exp_data/var_duration-exact-p12-can-2.0e7-memo-1-slnSeq-0-trace-1-AG.csv'  every ::1::1 using 10:($11/1048576) with linespoints pt 7 lc rgb "web-green" title "CAN-EXACT",\
    '../../src/exp_data/var_duration-exact-p12-gen-2.0e7-memo-1-slnSeq-0-trace-1-AG.csv'  every ::1::1 using 10:($11/1048576) with linespoints pt 6 lc rgb "blue" title "GEN-EXACT",\
    '../../src/exp_data/var_duration-apx-p12-can-2.0e7-memo-1-slnSeq-0-trace-1-AG.csv'  every ::1::1 using 10:($11/1048576) with linespoints pt 5 lc rgb "web-green" title "CAN-APX",\
    '../../src/exp_data/var_duration-apx-p12-gen-2.0e7-memo-1-slnSeq-0-trace-1-AG.csv'  every ::1::1 using 10:($11/1048576) with linespoints pt 4 lc rgb "blue" title "GEN-APX"