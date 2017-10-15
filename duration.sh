echo compiling
g++ thread_single_time_sq.cpp -o thread_single_time_sq
g++ thread_single_time_tri.cpp -o thread_single_time_tri
g++ thread_single_time_cos.cpp -o thread_single_time_cos
g++ thread_single_time_cos2.cpp -o thread_single_time_cos2
g++ thread_single_time_cos4.cpp -o thread_single_time_cos4
echo compiled

echo counting sq
./thread_single_time_sq
echo counting tri
./thread_single_time_tri
echo counting cos
./thread_single_time_cos
echo counting cos2
./thread_single_time_cos2
echo counting cos4
./thread_single_time_cos4
echo all counted

echo drawing
./plot_time.py chain_serialN_time_*_diameter.csv
echo drawn


