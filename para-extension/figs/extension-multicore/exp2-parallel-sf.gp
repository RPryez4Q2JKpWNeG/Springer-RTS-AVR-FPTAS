
#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"

# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Speedup (factor)' font "Times, 10" offset 3,0
set xlabel 'Demand Interval (us)' font "Times, 10" offset 0,0.5
# set format y "%2.0t{/Symbol \264}10^{%L}"
# set format y '2^{%L}'

set xrange [5000:1500000]
set yrange [-0.45:3.5]
# set logscale y 2

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
set key bottom right
# set key spacing 1.1
# set key width 3
# set key reverse
# set key Left
# set key vertical
# set key maxrows 4

# set xtics 1
# set lmargin 7
set logscale x 
# set logscale y 

set lmargin 4
set rmargin 1
set tmargin 2

#Name PDF
set output "exp2-para-exact-sf.pdf"
set title "EXACT n-Core PBM Speedup vs. Interval Size" font "Times, 12"
set key top left
set key samplen 2 spacing .75 font ",10"
set key maxrows 5
set key box height 1 width 1

plot \
    '../../../src/exp_data/var_duration-exact-p12-can-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "web-green" title "CAN-C01",\
    '../../../src/exp_data/var_duration-exact-p12-can-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "web-green" title "CAN-C02",\
    '../../../src/exp_data/var_duration-exact-p12-can-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_duration-exact-p12-can-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_duration-exact-p12-gen-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "blue" title "GEN-C01",\
    '../../../src/exp_data/var_duration-exact-p12-gen-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "blue" title "GEN-C02",\
    '../../../src/exp_data/var_duration-exact-p12-gen-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "blue" title "GEN-C04",\
    '../../../src/exp_data/var_duration-exact-p12-gen-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "blue" title "GEN-C06"

#Name PDF
set output "exp2-para-apx-sf.pdf"
set title "APX n-Core PBM Speedup vs. Interval Size" font "Times, 12"
set key top right
set key samplen 2 spacing .75 font ",10"
set key maxrows 5
set key box height 1 width 1

plot \
    '../../../src/exp_data/var_duration-apx-p12-can-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "web-green" title "CAN-C01",\
    '../../../src/exp_data/var_duration-apx-p12-can-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "web-green" title "CAN-C02",\
    '../../../src/exp_data/var_duration-apx-p12-can-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_duration-apx-p12-can-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_duration-apx-p12-gen-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "blue" title "GEN-C01",\
    '../../../src/exp_data/var_duration-apx-p12-gen-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "blue" title "GEN-C02",\
    '../../../src/exp_data/var_duration-apx-p12-gen-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "blue" title "GEN-C04",\
    '../../../src/exp_data/var_duration-apx-p12-gen-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "blue" title "GEN-C06"

#Name PDF
set output "exp2-para-kavr24-p05-sf.pdf"
set title "KAVR P05 n-Core PBM Speedup vs. Interval Size" font "Times, 12"
set key top left
set key samplen 2 spacing .75 font ",10"
set key maxrows 5
set key box height 1 width 1

plot \
    '../../../src/exp_data/var_duration-kavr24-p05-can-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "web-green" title "CAN-C01",\
    '../../../src/exp_data/var_duration-kavr24-p05-can-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "web-green" title "CAN-C02",\
    '../../../src/exp_data/var_duration-kavr24-p05-can-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_duration-kavr24-p05-can-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_duration-kavr24-p05-gen-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "blue" title "GEN-C01",\
    '../../../src/exp_data/var_duration-kavr24-p05-gen-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "blue" title "GEN-C02",\
    '../../../src/exp_data/var_duration-kavr24-p05-gen-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "blue" title "GEN-C04",\
    '../../../src/exp_data/var_duration-kavr24-p05-gen-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "blue" title "GEN-C06"

#Name PDF
set output "exp2-para-kavr24-p12-sf.pdf"
set title "KAVR P12 n-Core PBM Speedup vs. Interval Size" font "Times, 12"
set key top left
set key samplen 2 spacing .75 font ",10"
set key maxrows 5
set key box height 1 width 1

plot \
    '../../../src/exp_data/var_duration-kavr24-p12-can-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "web-green" title "CAN-C01",\
    '../../../src/exp_data/var_duration-kavr24-p12-can-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "web-green" title "CAN-C02",\
    '../../../src/exp_data/var_duration-kavr24-p12-can-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_duration-kavr24-p12-can-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_duration-kavr24-p12-gen-1.0e6-set-m1-s0-t0-c01-p0-ES-SF.csv' using 8:3 with linespoints pt 6 ps 0.5 lc rgb "blue" title "GEN-C01",\
    '../../../src/exp_data/var_duration-kavr24-p12-gen-1.0e6-set-m1-s0-t0-c02-p1-ES-SF.csv' using 8:3 with linespoints pt 8 ps 0.5 lc rgb "blue" title "GEN-C02",\
    '../../../src/exp_data/var_duration-kavr24-p12-gen-1.0e6-set-m1-s0-t0-c04-p1-ES-SF.csv' using 8:3 with linespoints pt 4 ps 0.5 lc rgb "blue" title "GEN-C04",\
    '../../../src/exp_data/var_duration-kavr24-p12-gen-1.0e6-set-m1-s0-t0-c08-p1-ES-SF.csv' using 8:3 with linespoints pt 12 ps 0.5 lc rgb "blue" title "GEN-C06"

