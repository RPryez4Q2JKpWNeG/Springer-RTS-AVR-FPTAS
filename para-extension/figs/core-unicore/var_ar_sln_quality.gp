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
    '../../src/exp_data/pub_data/var_ar_sln_qual/sxs_comb_run-var_ar-sln-qual-can-apx-0-2024-02-27-16-48-47-agg.csv' using 19:21 with linespoints pt 6 lc rgb "web-green" title "CAN-Theoretical",\
    '../../src/exp_data/pub_data/var_ar_sln_qual/sxs_comb_run-var_ar-sln-qual-can-apx-0-2024-02-27-16-48-47-agg.csv' using 19:15 with linespoints pt 8 lc rgb "web-green" title "CAN-Observed",\
    '../../src/exp_data/pub_data/var_ar_sln_qual/sxs_comb_run-var_ar-sln-qual-gen-apx-0-2024-02-27-16-48-49-agg.csv' using 19:21 with linespoints pt 6 lc rgb "medium-blue" title "GEN-Theoretical",\
    '../../src/exp_data/pub_data/var_ar_sln_qual/sxs_comb_run-var_ar-sln-qual-gen-apx-0-2024-02-27-16-48-49-agg.csv' using 19:15 with linespoints pt 8 lc rgb "medium-blue" title "GEN-Observed"