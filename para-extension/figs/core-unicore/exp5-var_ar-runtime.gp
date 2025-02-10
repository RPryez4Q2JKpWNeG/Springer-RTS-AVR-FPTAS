#Set Title
set title "APX Runtime vs. Approximation Parameters" font "Times, 12"

#Set Axis Markings
set xtics font "Times, 10"
set ytics font "Times, 10"
# set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
# set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set ylabel 'Runtime (s)' font "Times, 10" offset 3,0
set xlabel "{/Symbol e} value of varied term" font "Times, 10" offset 0,0.5 enhanced
set xrange [0.0:0.12]
set yrange [0.0:0.14]

#Prepare to handle CSVs
set datafile separator ','

#Configure Global PDF Outputs
set terminal pdf enhanced size 3.44in,2in
set key font "Times, 10"

set key autotitle columnhead

#Set key
# set key at 5.75, 900
# set key at 1.1,5
# set key spacing 2.0
# set key width 4
set key reverse
set key Left

# set xtics 1
# set lmargin 8
#l,r,b,t
set margins 5,2,2.5,2
# set logscale x 10
# set logscale y 10

#Name PDF
# set output "exp6-ar-can-lt.tex"

# plot \
#     '../../src/exp_data/pub_data/var_ar/sxs_tasks-var_ar-can-apx-2023-05-24-15-49-28.csv'\
#         every ::0::0 using 14:5     with points pt 1 lc rgb "web-green" title "$\\epsilon_x = 0.1$",\
#     ''  every ::1::4 using 14:5     with linespoints pt 4 lc rgb "web-green" title "$\\epsilon_r$",\
#     ''  every ::5::8 using 15:5     with linespoints pt 6 lc rgb "web-green" title "$\\epsilon_b$",\
#     ''  every ::9::12 using 16:5    with linespoints pt 8 lc rgb "web-green" title "$\\epsilon_f$"

# set output "exp6-ar-gen-lt.tex"
# plot \
#     '../../src/exp_data/pub_data/var_ar/sxs_tasks-var_ar-gen-apx-2023-05-24-15-50-05.csv'\
#         every ::0::0 using 14:5     with points pt 1 lc rgb "medium-blue" title "e_x = 0.1",\
#     ''  every ::1::4 using 14:5     with linespoints pt 4 lc rgb "medium-blue" title "e_r",\
#     ''  every ::5::8 using 15:5     with linespoints pt 6 lc rgb "medium-blue" title "e_b",\
#     ''  every ::9::12 using 16:5    with linespoints pt 8 lc rgb "medium-blue" title "e_f"

set output "exp5-var_ar-runtime.pdf"
plot \
    '../../src/exp_data/var_ar-runtime-apx-p12-can-1s-memo-1-slnSeq-0-trace-0-AG.csv'\
        every ::0::0 using 12:3     with points pt 1 lc rgb "web-green" title "CAN-APX All {/Symbol e}_x = 0.1",\
    ''  every ::1::4 using 12:3     with linespoints pt 4 lc rgb "web-green" title "CAN-APX {/Symbol e}_r",\
    ''  every ::5::8 using 14:3     with linespoints pt 6 lc rgb "web-green" title "CAN-APX {/Symbol e}_f",\
    ''  every ::9::12 using 13:3    with linespoints pt 8 lc rgb "web-green" title "CAN-APX {/Symbol e}_b",\
    '../../src/exp_data/var_ar-runtime-apx-p12-gen-1s-memo-1-slnSeq-0-trace-0-AG.csv'\
        every ::0::0 using 12:3     with points pt 1 lc rgb "medium-blue" title "GEN-APX All {/Symbol e}_x = 0.1",\
    ''  every ::1::4 using 12:3     with linespoints pt 4 lc rgb "medium-blue" title "GEN-APX {/Symbol e}_r",\
    ''  every ::5::8 using 14:3     with linespoints pt 6 lc rgb "medium-blue" title "GEN-APX {/Symbol e}_f",\
    ''  every ::9::12 using 13:3    with linespoints pt 8 lc rgb "medium-blue" title "GEN-APX {/Symbol e}_b"
