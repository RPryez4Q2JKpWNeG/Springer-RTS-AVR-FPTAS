#Set Title
set title "RAM Usage vs. Demand Window Size" font "Times, 14"

#Set Axis Markings
set xtics font "Times, 12"
set ytics font "Times, 12"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'RAM (bytes)' font "Times, 12" offset 3,0
set xlabel 'Demand Window Size (us)' font "Times, 12" offset 0,0.5
set xrange [5000:15000000]
set yrange [1000:10000000000]

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 12"

set key autotitle columnhead

#Set key
# set key at 5.75, 900
set key top left
set key spacing 1.1
set key width 4
set key reverse
set key Left

# set xtics 1
set lmargin 8
set logscale x 10
set logscale y 10

#Name PDF
set output "var_duration_mem.pdf"

plot \
    '../../src/exp_data/pub_data/var_dur_mem/raw_data/kavr/sxs_tasks-var_dur-can-kavr-2024-02-26-17-21-52.csv' using 1:21 with linespoints pt 9 lc rgb "web-green" title "CAN-KAVR ",\
    '../../src/exp_data/pub_data/var_dur_mem/raw_data/apx-exact/sxs_tasks-var_dur-can-apx-exact-2024-02-26-23-58-54.csv' using 1:22 with linespoints dt 2 pt 7 ps 0.5 lc rgb "web-green" title "CAN-EXACT",\
    '' using 1:23 with linespoints dt 3 pt 5 ps 0.5 lc rgb "web-green" title "CAN-APX  ",\
    '../../src/exp_data/pub_data/var_dur_mem/raw_data/kavr/sxs_tasks-var_dur-gen-kavr-2024-02-26-21-42-34.csv' using 1:21 with linespoints pt 8 lc rgb "medium-blue" title "GEN-KAVR ",\
    '../../src/exp_data/pub_data/var_dur_mem/raw_data/apx-exact/sxs_tasks-var_dur-gen-apx-exact-2024-02-27-02-25-09.csv' using 1:22 with linespoints dt 4 pt 6 ps 0.5 lc rgb "medium-blue" title "GEN-EXACT",\
    '' using 1:23 with linespoints dt 5 pt 4 ps 0.5 lc rgb "medium-blue" title "GEN-APX  "