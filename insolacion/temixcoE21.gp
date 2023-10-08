reset
load 'spectral.pal'
set datafile separator ','

# "time", "Gb", "G", "Gd", "UV", "T", "phi", "v", "p"
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x '%H:%M'
d = 60*60
set xlabel ''
set ylabel 'G [W/m$^2$]'
set xrange ['2019-01-21 06:00:00':'2019-01-21 20:00:00']
set grid

plot 'temixcoEnero2019.csv' using 1:2 with lines ls 1  title 'Directa ($G_b$)',\
     '' using 1:3 with lines ls 2  title 'Global ($G$)',\
     '' using 1:4 with lines ls 8  title 'Difusa ($G_d$)'