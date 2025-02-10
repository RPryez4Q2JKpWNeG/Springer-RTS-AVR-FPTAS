#Set Title
set title "Theoretical vs. Observed Overestimate" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Overestimate' font "Times, 10" offset 3,0
set xlabel '{/Symbol e}_r={/Symbol e}_f={/Symbol e}_b' font "Times, 10" offset 0,0.5
set xrange [0:0.55]
set yrange [0:10]

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
set key maxrows 3

# set xtics 1
set lmargin 7

#Name PDF
set output "var_ar-sln-quality.pdf"


plot \
    '../../src/exp_data/var_apx_ratio_sln_qual-apx-p12-can-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-man-add.csv' using 14:16 with linespoints pt 7 lc rgb "green" title "CAN-Theoretical",\
    '../../src/exp_data/var_apx_ratio_sln_qual-apx-p12-can-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-man-add.csv' using 14:19 with linespoints pt 6 lc rgb "red" title "CAN-Observed",\
    '../../src/exp_data/var_apx_ratio_sln_qual-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-man-add.csv' using 14:16 with linespoints pt 9 lc rgb "blue" title "GEN-Theoretical",\
    '../../src/exp_data/var_apx_ratio_sln_qual-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-man-add.csv' using 14:19 with linespoints pt 8 lc rgb "red" title "GEN-Observed"