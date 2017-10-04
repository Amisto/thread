echo compiling
g++ thread_single_sq_width.cpp -o thread_single_sq_width
g++ thread_single_tri_width.cpp -o thread_single_tri_width
g++ thread_single_cos_width.cpp -o thread_single_cos_width
g++ thread_single_cos2_width.cpp -o thread_single_cos2_width
g++ thread_single_cos4_width.cpp -o thread_single_cos4_width
echo compiled

echo counting sq
./thread_single_sq_width
echo counting tri
./thread_single_tri_width
echo counting cos
./thread_single_cos_width
echo counting cos2
./thread_single_cos2_width
echo counting 4
./thread_single_cos4_width
echo all counted

echo drawing
./plot.py chain_sq_width_*
./plot.py chain_tri_width_*
./plot.py chain_cos_width_*
./plot.py chain_cos2_width_*
./plot.py chain_cos4_width_*
./plot_diameters.py chain_*_width_diameter.csv
echo drawn

