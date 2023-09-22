reset
load 'spectral.pal'

set style fill transparent pattern 2
set yrange [0:90]
set xrange [-150:150]
set xlabel '$\gamma_s$ [grad]'
set ylabel '$\alpha$ [grad]'

set label 1 at -125, 7 '5'
set label 2 at -115, 18 '6'
set label 3 at -106, 28 '7'
set label 4 at -95, 39 '8'
set label 5 at -83, 49 '9'
set label 6 at -69, 59 '10'
set label 7 at -45, 66 '11'
#set label 8 at -20, 75 'Mediodía'
set label 9 at 37, 66 '13'
set label 10 at 61, 59 '14'
set label 11 at 75, 49 '15'
set label 12 at 87, 39 '16'
set label 13 at 97, 28 '17'
set label 14 at 107, 18 '18'
set label 15 at 119, 7 '19'

# set label 16 at 0, 22.5 '\scriptsize Dic'
# set label 17 at 0, 26 '\scriptsize Ene'
# set label 18 at 0, 35 '\scriptsize Feb'
# set label 19 at 0, 46 '\scriptsize Mar'
# set label 20 at 0, 58 '\scriptsize Abr'
# set label 21 at 0, 66 '\scriptsize May'
# set label 22 at 0, 70 '\scriptsize Jun'

#set label 23 at -130, 70 '$\phi$ = 45$^\circ$'

plot 'gD.dat' index 0 using 3:4 with line ls 2 title '',\
     '' index 1 using 3:4 with line ls 3 title '',\
     '' index 2 using 3:4 with line ls 4 title '',\
     '' index 3 using 3:4 with line ls 5 title '',\
     '' index 4 using 3:4 with line ls 6 title '',\
     '' index 5 using 3:4 with line ls 7 title '',\
     '' index 11 using 3:4 with line ls 1 title '',\
     'gH.dat' index 0 using 3:4 with line ls 1 title '',\
     '' index 1 using 3:4 with line ls 1 title '',\
     '' index 2 using 3:4 with line ls 2 title '',\
     '' index 3 using 3:4 with line ls 3 title '',\
     '' index 4 using 3:4 with line ls 4 title '',\
     '' index 5 using 3:4 with line ls 5 title '',\
     '' index 6 using 3:4 with line ls 6 title '',\
     '' index 7 using 3:4 with line ls 8 title '',\
     '' index 8 using 3:4 with line ls 6 title '',\
     '' index 9 using 3:4 with line ls 5 title '',\
     '' index 10 using 3:4 with line ls 4 title '',\
     '' index 11 using 3:4 with line ls 3 title '',\
     '' index 12 using 3:4 with line ls 2 title '',\
     '' index 13 using 3:4 with line ls 1 title '',\
     '' index 14 using 3:4 with line ls 1 title ''
