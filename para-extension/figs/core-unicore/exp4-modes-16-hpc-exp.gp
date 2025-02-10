#Set Title
set title "Demand Calculation Runtime vs. Mode Count" font "Times, 14"

#Set Axis Markings
set xtics font "Times, 12"
set ytics font "Times, 12"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 12" offset 3,0
set xlabel 'Number of Modes' font "Times, 12" offset 0,0.5
set xrange [1:17]
set yrange [0.001:20000]

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
# set key width 4
set key reverse
set key Left

# set xtics 1
# set lmargin 7
#l,r,b,t
set margins 6,1,2.5,2
# set logscale x 10
set logscale y 10

#Name PDF
set output "exp4-modes-p5-12.pdf"

plot \
    '../../src/exp_data/var_mode_16-kavr24-p5-m16-750ms-memo-1-slnSeq-0-trace-0-AG.csv' using 5:3 with linespoints dt 2 pt 8 lc rgb "orchid" title "KAVR-P05",\
    '../../src/exp_data/var_mode_16-kavr24-p12-m16-750ms-memo-1-slnSeq-0-trace-0-AG.csv' using 5:3 with linespoints dt 3 pt 8 lc rgb "orchid4" title "KAVR-P12",\
    '../../src/exp_data/var_mode_16-exact-p12-m16-750ms-memo-1-slnSeq-0-trace-0-AG.csv' using 5:3 with linespoints dt 4 pt 6 lc rgb "orange" title "EXACT",\
    '../../src/exp_data/var_mode_16-apx-p12-m16-750ms-memo-1-slnSeq-0-trace-0-AG.csv' using 5:3 with linespoints dt 4 pt 4 lc rgb "light-red" title "APX"
#Name PDF
# set output "exp4-modes-p5-12-no-exact.pdf"

# plot \
#     '../../src/exp_data/var_mode_16-kavr24-p5-m16-750ms-memo-1-slnSeq-0-trace-0-AG.csv' using 5:3 with linespoints dt 2 pt 8 lc rgb "orchid" title "KAVR-P05",\
#     '../../src/exp_data/var_mode_16-kavr24-p12-m16-750ms-memo-1-slnSeq-0-trace-0-AG.csv' using 5:3 with linespoints dt 3 pt 8 lc rgb "orchid4" title "KAVR-P12",\
#     '../../src/exp_data/var_mode_16-apx-p12-m16-750ms-memo-1-slnSeq-0-trace-0-AG.csv' using 5:3 with linespoints dt 4 pt 4 lc rgb "light-red" title "APX"