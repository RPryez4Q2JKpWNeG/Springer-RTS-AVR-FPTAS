#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 12" offset 2,0
set xlabel 'Maximum Acceleraton (rpm/sec^2)' font "Times, 12" offset 0,0.5

# set format y "%2.0t{/Symbol \264}10^{%L}"
set format y '2^{%L}'

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
# set key at 5.75, 900
set key bottom right
# set key spacing 1.1
set key width 3
set key reverse
set key Left
set key maxrows 5
set key box height 1

set xtics 200000
# set lmargin 8
#l,r,b,t
set lmargin 4.5
set rmargin 2
set tmargin 2
set bmargin 3
# set logscale x 10
set logscale y 2
# set yrange [0.001:64]

#Name PDF
set output "exp3-para-exact.pdf"
set title "EXACT n-core PBM Runtime vs. Acceleration" font "Times, 12"

plot \
    '../../../src/exp_data/var_accel-exact-p12-can-1s-m1-s0-t0-c01-p0-ES.csv' every 4 using 5:1 with lines           lc rgb "web-green" title "CAN-C01",\
    '../../../src/exp_data/var_accel-exact-p12-can-1s-m1-s0-t0-c02-p1-ES.csv' every 4 using 5:1 with lines dt "-"    lc rgb "web-green" title "CAN-C02",\
    '../../../src/exp_data/var_accel-exact-p12-can-1s-m1-s0-t0-c04-p1-ES.csv' every 4 using 5:1 with lines dt "-."   lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_accel-exact-p12-can-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_accel-exact-p12-gen-1s-m1-s0-t0-c01-p0-ES.csv' every 4 using 5:1 with lines           lc rgb "blue" title "GEN-C01",\
    '../../../src/exp_data/var_accel-exact-p12-gen-1s-m1-s0-t0-c02-p1-ES.csv' every 4 using 5:1 with lines dt "-"    lc rgb "blue" title "GEN-C02",\
    '../../../src/exp_data/var_accel-exact-p12-gen-1s-m1-s0-t0-c04-p1-ES.csv' every 4 using 5:1 with lines dt "-."   lc rgb "blue" title "GEN-C04",\
    '../../../src/exp_data/var_accel-exact-p12-gen-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "blue" title "GEN-C06"


#Name PDF
set output "exp3-para-apx.pdf"
# set yrange [0.0001:10000]
set title "APX n-core PBM Runtime vs. Acceleration" font "Times, 12"

plot \
    '../../../src/exp_data/var_accel-apx-p12-can-1s-m1-s0-t0-c01-p0-ES.csv' every 4 using 5:1 with lines           lc rgb "web-green" title "CAN-C01",\
    '../../../src/exp_data/var_accel-apx-p12-can-1s-m1-s0-t0-c02-p1-ES.csv' every 4 using 5:1 with lines dt "-"    lc rgb "web-green" title "CAN-C02",\
    '../../../src/exp_data/var_accel-apx-p12-can-1s-m1-s0-t0-c04-p1-ES.csv' every 4 using 5:1 with lines dt "-."   lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_accel-apx-p12-can-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_accel-apx-p12-gen-1s-m1-s0-t0-c01-p0-ES.csv' every 4 using 5:1 with lines           lc rgb "blue" title "GEN-C01",\
    '../../../src/exp_data/var_accel-apx-p12-gen-1s-m1-s0-t0-c02-p1-ES.csv' every 4 using 5:1 with lines dt "-"    lc rgb "blue" title "GEN-C02",\
    '../../../src/exp_data/var_accel-apx-p12-gen-1s-m1-s0-t0-c04-p1-ES.csv' every 4 using 5:1 with lines dt "-."   lc rgb "blue" title "GEN-C04",\
    '../../../src/exp_data/var_accel-apx-p12-gen-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "blue" title "GEN-C06"


#Name PDF
set output "exp3-para-kavr24-p05.pdf"
# set yrange [0.0001:10000]
set title "KAVR P05 n-core PBM Runtime vs. Acceleration" font "Times, 12"

plot \
    '../../../src/exp_data/var_accel-kavr24-p05-can-1s-m1-s0-t0-c01-p0-ES.csv' every 4 using 5:1 with lines           lc rgb "web-green" title "CAN-C01",\
    '../../../src/exp_data/var_accel-kavr24-p05-can-1s-m1-s0-t0-c02-p1-ES.csv' every 4 using 5:1 with lines dt "-"    lc rgb "web-green" title "CAN-C02",\
    '../../../src/exp_data/var_accel-kavr24-p05-can-1s-m1-s0-t0-c04-p1-ES.csv' every 4 using 5:1 with lines dt "-."   lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_accel-kavr24-p05-can-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_accel-kavr24-p05-gen-1s-m1-s0-t0-c01-p0-ES.csv' every 4 using 5:1 with lines           lc rgb "blue" title "GEN-C01",\
    '../../../src/exp_data/var_accel-kavr24-p05-gen-1s-m1-s0-t0-c02-p1-ES.csv' every 4 using 5:1 with lines dt "-"    lc rgb "blue" title "GEN-C02",\
    '../../../src/exp_data/var_accel-kavr24-p05-gen-1s-m1-s0-t0-c04-p1-ES.csv' every 4 using 5:1 with lines dt "-."   lc rgb "blue" title "GEN-C04",\
    '../../../src/exp_data/var_accel-kavr24-p05-gen-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "blue" title "GEN-C06"


#Name PDF
set output "exp3-para-kavr24-p12.pdf"
# set yrange [0.0001:10000]
set title "KAVR P12 n-core PBM Runtime vs. Acceleration" font "Times, 12"

plot \
    '../../../src/exp_data/var_accel-kavr24-p12-can-1s-m1-s0-t0-c04-p1-ES.csv' every 4 using 5:1 with lines dt "-."   lc rgb "web-green" title "CAN-C04",\
    '../../../src/exp_data/var_accel-kavr24-p12-can-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "web-green" title "CAN-C06",\
    '../../../src/exp_data/var_accel-kavr24-p12-gen-1s-m1-s0-t0-c08-p1-ES.csv' every 4 using 5:1 with lines dt "."    lc rgb "blue" title "GEN-C06"