# Set Title
set title "n-core PBM Runtime vs. Mode Count" font "Times, 14"

#Set Axis Markings
set xtics font "Times, 12"
set ytics font "Times, 12"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 12" offset 2,0
set xlabel 'Number of Modes' font "Times, 12" offset 0,0.5
set xrange [1:17]
set yrange [0.001:4194304]
set format y '2^{%L}'

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
set key top left
set key samplen 0.5 spacing 0.8 font ",7"
set key maxrows 5
set key box height 1

# set xtics 1
# set lmargin 7
#l,r,b,t
set margins 6,1,2.5,2
# set logscale x 10
set logscale y 2


#Name PDF
set output "exp4-modes-parallel.pdf"

plot \
    '../../../src/exp_data/var_mode_16-kavr24-p05-m16-750ms-m1-s0-t0-c01-p0-ES.csv' using 2:1 with linespoints pt 6 ps 0.5 lc rgb "#D81B60" title "KAVR-P05-C01",\
    '../../../src/exp_data/var_mode_16-kavr24-p05-m16-750ms-m1-s0-t0-c02-p1-ES.csv' using 2:1 with linespoints pt 8 ps 0.5 lc rgb "#D81B60" title "KAVR-P05-C02",\
    '../../../src/exp_data/var_mode_16-kavr24-p05-m16-750ms-m1-s0-t0-c04-p1-ES.csv' using 2:1 with linespoints pt 4 ps 0.5 lc rgb "#D81B60" title "KAVR-P05-C04",\
    '../../../src/exp_data/var_mode_16-kavr24-p05-m16-750ms-m1-s0-t0-c08-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#D81B60" title "KAVR-P05-C08",\
    '../../../src/exp_data/var_mode_16-kavr24-p05-m16-750ms-m1-s0-t0-c16-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#D81B60" title "KAVR-P05-C16",\
    '../../../src/exp_data/var_mode_16-exact-p12-m16-750ms-m1-s0-t0-c01-p0-ES.csv' using 2:1 with linespoints pt 6 ps 0.5 lc rgb "#FFC107" title "EXACT-C01",\
    '../../../src/exp_data/var_mode_16-exact-p12-m16-750ms-m1-s0-t0-c02-p1-ES.csv' using 2:1 with linespoints pt 8 ps 0.5 lc rgb "#FFC107" title "EXACT-C02",\
    '../../../src/exp_data/var_mode_16-exact-p12-m16-750ms-m1-s0-t0-c04-p1-ES.csv' using 2:1 with linespoints pt 4 ps 0.5 lc rgb "#FFC107" title "EXACT-C04",\
    '../../../src/exp_data/var_mode_16-exact-p12-m16-750ms-m1-s0-t0-c08-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#FFC107" title "EXACT-C08",\
    '../../../src/exp_data/var_mode_16-exact-p12-m16-750ms-m1-s0-t0-c16-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#FFC107" title "EXACT-C16",\
    '../../../src/exp_data/var_mode_16-apx-p12-m16-750ms-m1-s0-t0-c01-p0-ES.csv' using 2:1 with linespoints pt 6 ps 0.5 lc rgb "#004D40" title "APX-C01",\
    '../../../src/exp_data/var_mode_16-apx-p12-m16-750ms-m1-s0-t0-c02-p1-ES.csv' using 2:1 with linespoints pt 8 ps 0.5 lc rgb "#004D40" title "APX-C02",\
    '../../../src/exp_data/var_mode_16-apx-p12-m16-750ms-m1-s0-t0-c04-p1-ES.csv' using 2:1 with linespoints pt 4 ps 0.5 lc rgb "#004D40" title "APX-C04",\
    '../../../src/exp_data/var_mode_16-apx-p12-m16-750ms-m1-s0-t0-c08-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#004D40" title "APX-C08",\
    '../../../src/exp_data/var_mode_16-apx-p12-m16-750ms-m1-s0-t0-c16-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#004D40" title "APX-C16"
    # '../../../src/exp_data/var_mode_16-kavr24-p12-m16-750ms-m1-s0-t0-c01-p0-ES.csv' using 2:1 with linespoints pt 6 ps 0.5 lc rgb "#1E88E5" title "KAVR-P12-C01",\
    # '../../../src/exp_data/var_mode_16-kavr24-p12-m16-750ms-m1-s0-t0-c02-p1-ES.csv' using 2:1 with linespoints pt 8 ps 0.5 lc rgb "#1E88E5" title "KAVR-P12-C02",\
    # '../../../src/exp_data/var_mode_16-kavr24-p12-m16-750ms-m1-s0-t0-c04-p1-ES.csv' using 2:1 with linespoints pt 4 ps 0.5 lc rgb "#1E88E5" title "KAVR-P12-C04",\
    # '../../../src/exp_data/var_mode_16-kavr24-p12-m16-750ms-m1-s0-t0-c08-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#1E88E5" title "KAVR-P12-C08",\
    # '../../../src/exp_data/var_mode_16-kavr24-p12-m16-750ms-m1-s0-t0-c16-p1-ES.csv' using 2:1 with linespoints pt 12 ps 0.5 lc rgb "#1E88E5" title "KAVR-P12-C16",\