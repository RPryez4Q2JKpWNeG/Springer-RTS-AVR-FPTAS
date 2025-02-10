#Set Title
set title "Demand Calculation Runtime vs. Acceleration" font "Times, 14"

#Set Axis Markings
set xtics font "Times, 12"
set ytics font "Times, 12"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 12" offset 3,0
set xlabel 'Maximum Acceleraton (rpm/sec^2)' font "Times, 12" offset 0,0.5

set xrange [-20000:1020000]
set yrange [0.001:1500000]

# set format y "%2.0t{/Symbol \264}10^{%L}"

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
# set key at 5.75, 900
set key top left
# set key spacing 1.1
set key width 3
set key reverse
set key Left
set key maxrows 4

set xtics 200000
# set lmargin 8
#l,r,b,t
set margins 7,2,2.5,2
# set logscale x 10
set logscale y 10

#Name PDF
set output "exp3-accel-p5-12-simplify-cangen.pdf"

plot \
    '../../src/exp_data/var_accel-kavr24-p5-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 1 lc rgb "web-green" title "CAN-K-P05",\
    '../../src/exp_data/var_accel-kavr24-p5-gen-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 1 lc rgb "blue" title "GEN-K-P05",\
    '../../src/exp_data/var_accel-kavr24-p12-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 2 lc rgb "web-green" title "CAN-K-P12",\
    '../../src/exp_data/var_accel-kavr24-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 2 lc rgb "blue" title "GEN-K-P12",\
    '../../src/exp_data/var_accel-exact-p12-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 3 lc rgb "web-green" title "CAN-EXACT",\
    '../../src/exp_data/var_accel-exact-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 3 lc rgb "blue" title "GEN-EXACT",\
    '../../src/exp_data/var_accel-apx-p12-can-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 4 lc rgb "web-green" title "CAN-APX",\
    '../../src/exp_data/var_accel-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG.csv' using 8:3 with lines dt 4 lc rgb "blue" title "GEN-APX"