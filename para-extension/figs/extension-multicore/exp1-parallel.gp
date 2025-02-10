
#Set Title
set title "AVR Demand Runtime vs. Precision" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"

# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 10" offset 3,0
set xlabel 'Precision' font "Times, 10" offset 0,0.5
# set format y "%2.0t{/Symbol \264}10^{%L}"
# set format y '2^{%L}'

set xrange [4.5:12.5]
# set yrange [-1:65536]
set logscale y 2

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
# set key bottom left
# set key spacing 1.1
# set key width 3
# set key reverse
# set key Left
# set key vertical
# set key maxrows 4

# set xtics 1
set lmargin 6
set rmargin 1
set tmargin 2

#Name PDF
# set output "exp1-para-row17.pdf"

# plot \
#     '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 1 lc rgb "web-green" title "ROW-C01",\
#     '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 2 lc rgb "web-green" title "ROW-C02",\
#     '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 12 lc rgb "web-green" title "ROW-C04",\
#     '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 3 lc rgb "web-green" title "ROW-C08"

#Name PDF
set title "n-Core PBI Runtime vs. Precision: CAN Task Set" font "Times, 12"
set output "exp1-para-all-can-p0.pdf"

set xrange [4.5:12.5]
set yrange [0.1:4096]
set key bottom left
set key samplen 0.5 spacing .75 font ",7"
set key maxrows 5
set key box height 1

plot \
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#D81B60" title "ROW-C01",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#D81B60" title "ROW-C02",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#D81B60" title "ROW-C04",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#D81B60" title "ROW-C08",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#D81B60" title "ROW-C16",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#1E88E5" title "KAVR-C01",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#1E88E5" title "KAVR-C02",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#1E88E5" title "KAVR-C04",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#1E88E5" title "KAVR-C08",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#1E88E5" title "KAVR-C16",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#FFC107" title "EXACT-C01",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#FFC107" title "EXACT-C02",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#FFC107" title "EXACT-C04",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#FFC107" title "EXACT-C08",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#FFC107" title "EXACT-C16",\
    '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#004D40" title "APX-C01",\
    '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#004D40" title "APX-C02",\
    '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#004D40" title "APX-C04",\
    '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#004D40" title "APX-C08",\
    '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#004D40" title "APX-C16"

#Name PDF
set title "n-Core PBI Runtime vs. Precision: GEN Task Set" font "Times, 12"
set output "exp1-para-all-gen-p0.pdf"

set xrange [4.5:12.5]
set yrange [0.5:4096]
set key bottom left
set key samplen 0.5 spacing .75 font ",7"
set key maxrows 5
set key box
set key box height 1

plot \
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#D81B60" title "ROW-C01",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#D81B60" title "ROW-C02",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#D81B60" title "ROW-C04",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#D81B60" title "ROW-C08",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#D81B60" title "ROW-C16",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#1E88E5" title "KAVR-C01",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#1E88E5" title "KAVR-C02",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#1E88E5" title "KAVR-C04",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#1E88E5" title "KAVR-C08",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#1E88E5" title "KAVR-C16",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#FFC107" title "EXACT-C01",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#FFC107" title "EXACT-C02",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#FFC107" title "EXACT-C04",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#FFC107" title "EXACT-C08",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#FFC107" title "EXACT-C16",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#004D40" title "APX-C01",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#004D40" title "APX-C02",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#004D40" title "APX-C04",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#004D40" title "APX-C08",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c16-p0.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#004D40" title "APX-C16"

#Name PDF
set title "n-Core PBM Runtime vs. Precision: CAN Task Set" font "Times, 12"
set output "exp1-para-all-can-p1.pdf"

set xrange [4.5:12.5]
set yrange [0.5:4096]
set key bottom left
set key samplen 0.5 spacing .75 font ",7"
set key maxrows 5
set key box
set key box height 1

plot \
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#D81B60" title "ROW-C01",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#D81B60" title "ROW-C02",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#D81B60" title "ROW-C04",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#D81B60" title "ROW-C08",\
    '../../../src/exp_data/v_precision-row17-p05-p12-can-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#D81B60" title "ROW-C16",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#1E88E5" title "KAVR-C01",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#1E88E5" title "KAVR-C02",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#1E88E5" title "KAVR-C04",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#1E88E5" title "KAVR-C08",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#1E88E5" title "KAVR-C16",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#FFC107" title "EXACT-C01",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#FFC107" title "EXACT-C02",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#FFC107" title "EXACT-C04",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#FFC107" title "EXACT-C08",\
    '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#FFC107" title "EXACT-C16",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#004D40" title "APX-C01",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#004D40" title "APX-C02",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#004D40" title "APX-C04",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#004D40" title "APX-C08",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#004D40" title "APX-C16"

#Name PDF
set title "n-Core PBM Runtime vs. Precision: GEN Task Set" font "Times, 12"
set output "exp1-para-all-gen-p1.pdf"

set xrange [4.5:12.5]
set yrange [0.5:4096]
set key bottom left
set key samplen 0.5 spacing .75 font ",7"
set key maxrows 5
set key box
set key box height 1

plot \
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#D81B60" title "ROW-C01",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#D81B60" title "ROW-C02",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#D81B60" title "ROW-C04",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#D81B60" title "ROW-C08",\
    '../../../src/exp_data/v_precision-row17-p05-p12-gen-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#D81B60" title "ROW-C16",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#1E88E5" title "KAVR-C01",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#1E88E5" title "KAVR-C02",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#1E88E5" title "KAVR-C04",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#1E88E5" title "KAVR-C08",\
    '../../../src/exp_data/v_precision-kavr24-p05-p12-gen-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#1E88E5" title "KAVR-C16",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#FFC107" title "EXACT-C01",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#FFC107" title "EXACT-C02",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#FFC107" title "EXACT-C04",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#FFC107" title "EXACT-C08",\
    '../../../src/exp_data/v_precision-exact-p05-p12-gen-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#FFC107" title "EXACT-C16",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c01-p1.csv' using 7:1 with linespoints pt 6 ps 0.5 lc rgb "#004D40" title "APX-C01",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c02-p1.csv' using 7:1 with linespoints pt 8 ps 0.5 lc rgb "#004D40" title "APX-C02",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c04-p1.csv' using 7:1 with linespoints pt 4 ps 0.5 lc rgb "#004D40" title "APX-C04",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c08-p1.csv' using 7:1 with linespoints pt 12 ps 0.5 lc rgb "#004D40" title "APX-C08",\
    '../../../src/exp_data/v_precision-apx-p05-p12-gen-rtss18-m1-s0-t0-c16-p1.csv' using 7:1 with linespoints pt 3 ps 0.5 lc rgb "#004D40" title "APX-C16"


#Name PDF
# set title "EXACT, APX, KAVR Demand Runtime vs. Precision" font "Times, 12"
# set output "exp1-para-exact-apx.pdf"

# set yrange [0.5:4096]
# set key bottom center
# set key maxrows 4

# plot \
#     '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 1 lc rgb "web-green" title "EXACT-C01",\
#     '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 2 lc rgb "web-green" title "EXACT-C02",\
#     '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 12 lc rgb "web-green" title "EXACT-C04",\
#     '../../../src/exp_data/v_precision-exact-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 3 lc rgb "web-green" title "EXACT-C08",\
#     '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 5 lc rgb "web-green" title "APX-C01",\
#     '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 6 lc rgb "web-green" title "APX-C02",\
#     '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 7 lc rgb "web-green" title "APX-C04",\
#     '../../../src/exp_data/v_precision-apx-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 8 lc rgb "web-green" title "APX-C08",\
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 1 lc rgb "web-green" title "KAVR-C01",\
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 2 lc rgb "web-green" title "KAVR-C02",\
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 12 lc rgb "web-green" title "KAVR-C04",\
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 3 lc rgb "web-green" title "KAVR-C08"

# #Name PDF
# set title "KAVR'24 Demand Runtime vs. Precision" font "Times, 12"
# set output "exp1-para-kavr24.pdf"

# set key bottom right

# plot \
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c01-p0.csv' using 7:1 with linespoints pt 1 lc rgb "web-green" title "Unicore",\
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c02-p0.csv' using 7:1 with linespoints pt 2 lc rgb "web-green" title "2-core",\
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c04-p0.csv' using 7:1 with linespoints pt 12 lc rgb "web-green" title "4-core",\
#     '../../../src/exp_data/v_precision-kavr24-p05-p12-can-rtss18-m1-s0-t0-c08-p0.csv' using 7:1 with linespoints pt 3 lc rgb "web-green" title "8-core"