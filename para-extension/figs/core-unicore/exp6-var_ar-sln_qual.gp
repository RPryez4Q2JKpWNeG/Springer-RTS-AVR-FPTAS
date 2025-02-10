#Set Title
set title "Theoretical vs. Observed Approximation Ratio" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10" nomirror
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Approximation Ratio' font "Times, 10" offset 3,0
set xlabel '{/Symbol e}_r={/Symbol e}_f={/Symbol e}_b' font "Times, 10" offset 0,0.5
set xrange [0:0.55]
set yrange [0:10]
set y2label 'Observed / Theoretical Approx. Ratio' font "Times, 10" offset -1.5,0
set y2range [0:1.75]
set y2tics font "Times, 10" offset -0.5,0
set y2tics 1
#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
set key top left
set key spacing 1.1
# set key width 3
set key reverse
set key Left
set key vertical
set key maxrows 4
set key width -10

# set xtics 1
#l,r,b,t
#l,r,b,t
set margins 3.5,4.5,2.5,2

#Name PDF
set output "exp6-var_ar-sln-quality.pdf"

plot \
    '../../src/exp_data/var_ar-sln_qual-apx-p12-can-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-manual-addition.csv' using 12:16 with linespoints pt 7 lc rgb "green" title "CAN-Theoretical" axis x1y1,\
    '../../src/exp_data/var_ar-sln_qual-apx-p12-can-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-manual-addition.csv' using 12:19 with linespoints pt 6 lc rgb "red" title "CAN-Observed" axis x1y1,\
    '../../src/exp_data/var_ar-sln_qual-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-manual-addition.csv' using 12:16 with linespoints pt 9 lc rgb "blue" title "GEN-Theoretical" axis x1y1,\
    '../../src/exp_data/var_ar-sln_qual-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-manual-addition.csv' using 12:19 with linespoints pt 8 lc rgb "red" title "GEN-Observed" axis x1y1,\
    '../../src/exp_data/var_ar-sln_qual-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-manual-addition.csv' using 12:20 with linespoints ps 0.5 pt 4 lc rgb "green" title "CAN-Observed/Theoretical" axis x1y2,\
    '../../src/exp_data/var_ar-sln_qual-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG-KAVR24-manual-addition.csv' using 12:20 with linespoints ps 0.5 pt 2 lc rgb "blue" title "GEN-Observed/Theoretical" axis x1y2,\
    NaN lt -2 ti " "