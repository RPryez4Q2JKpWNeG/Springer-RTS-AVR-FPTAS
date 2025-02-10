#Set Title
set title "Demand Calculation Runtime vs. Demand Window Size" font "Times, 14"

#Set Axis Markings
set xtics font "Times, 12"
set ytics font "Times, 12"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 12" offset 3,0
set xlabel 'Demand Window Size (us)' font "Times, 12" offset 0,0.5

set xrange [5000:1500000]
# set yrange [0.00001:15000]
set format y "%2.0t{/Symbol \264}10^{%L}"

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
# set key at 5.75, 900
set key top left
set key spacing 1.1
set key width 4
set key reverse
set key Left
set key maxrows 6
# set xtics 1
# set lmargin 8
#l,r,b,t
set margins 7,2,3,2
set logscale x 10
set logscale y 10

#Name PDF
set output "exp2-duration-p5-12.pdf"

plot \
    '../../src/exp_data/var_duration-kavr24-p5-can-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 9 lc rgb "web-green" title "CAN-KAVR-P05",\
    '../../src/exp_data/var_duration-kavr24-p12-can-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 11 lc rgb "web-green" title "CAN-KAVR-P12",\
    '../../src/exp_data/var_duration-exact-p12-can-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 7 lc rgb "web-green" title "CAN-EXACT",\
    '../../src/exp_data/var_duration-apx-p12-can-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 5 lc rgb "web-green" title "CAN-APX",\
    '../../src/exp_data/var_duration-kavr24-p5-gen-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 8 lc rgb "blue" title "GEN-KAVR-P05",\
    '../../src/exp_data/var_duration-kavr24-p12-gen-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 10 lc rgb "blue" title "GEN-KAVR-P12",\
    '../../src/exp_data/var_duration-exact-p12-gen-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 6 lc rgb "blue" title "GEN-EXACT",\
    '../../src/exp_data/var_duration-apx-p12-gen-2.0e7-memo-1-slnSeq-0-trace-0-AG.csv' using 1:3 with linespoints pt 4 lc rgb "blue" title "GEN-APX"
