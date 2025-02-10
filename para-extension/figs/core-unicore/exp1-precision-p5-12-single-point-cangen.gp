#Set Title
set title "Demand Calculation Runtime vs. Precision" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 10" offset 4,0
set xlabel 'Precision' font "Times, 10" offset 0,0.5
set format y "%2.0t{/Symbol \264}10^{%L}"

set xrange [4.5:12.5]
set yrange [0.01:10000]
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
set key maxrows 2

# set xtics 200000
# set lmargin 7
#l,r,b,t
set margins 6.5,1,2.5,2

#Name PDF
set output "exp1-precision-p5-12-single-point-cangen.pdf"

plot \
    '../../src/exp_data/var_precision-kavr24-p05-12-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' using 10:3 with linespoints pt 9 lc rgb "web-green" title "CAN-KAVR",\
    '../../src/exp_data/var_precision-kavr24-p05-12-gen-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' using 10:3 with linespoints pt 8 lc rgb "blue" title "GEN-KAVR",\
    '../../src/exp_data/var_precision-exact-p12-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every ::99::100 using 10:3 with linespoints pt 7 lc rgb "web-green" title "CAN-EXACT",\
    '../../src/exp_data/var_precision-exact-p12-gen-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every ::99::100 using 10:3 with linespoints pt 6 lc rgb "blue" title "GEN-EXACT",\
    '../../src/exp_data/var_precision-apx-p12-can-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every ::99::100 using 10:3 with linespoints pt 5 lc rgb "web-green" title "CAN-APX",\
    '../../src/exp_data/var_precision-apx-p12-gen-rtss18-memo-1-slnSeq-0-trace-0-AG.csv' every ::99::100 using 10:3 with linespoints pt 4 lc rgb "blue" title "GEN-APX"
    # 57.7154751150083 with lines dashtype 2 lc rgb "web-green" title "CAN-EXACT",\
    # 6.420810055002221 with lines dashtype 3 lc rgb "web-green" title "CAN-APX",\
    # 57.7154751150083 with lines dashtype 2 lc rgb "blue" title "GEN-EXACT",\
    # 6.420810055002221 with lines dashtype 3 lc rgb "blue" title "GEN-APX",\
