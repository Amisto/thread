//mm sec g

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N_BASIC 5000
#define N_LOGS 5
#define XMIN 0.0
#define XMAX 400.0          // mm
#define RHO 1.43            // g/mm
#define E 125000000000.0    // Pa

int N = 200;

double DX = (XMAX - XMIN)/N;
double DM = RHO * DX; // S = 1 mm^2

double DT = 0.5E-9;
double strength = 1.0425;

int going, step;
double ymax;

FILE* flog = NULL;
char fname_dummy[100] = "chain_serialN_time_tri_%s.csv", fname[100];

double res[100][100];

int min_intact = N, check_intact_counter = 0, check_intact_checker, fnum = 0;

//Pulse properties:
double pulse_width = 50;                //mm
double pulse_amplitude = 5E9;    //Pa, base - 5*10^9 Pa
double pulse_duration = 1e-10;

struct link
{
    double vx, vy, x, y;
    int intact;
} chain[N_BASIC];

int intact[N_BASIC-1];

struct v2
{
    double x, y;
} force[N_BASIC];

void init_chain()
{
    for (int i = 0; i < N; i++)
    {
        chain[i].vx = chain[i].vy = chain[i].y = 0;
        chain[i].x = XMIN + i*DX;
        force[i].x = force[i].y = 0;
    }

    for (int i = 0; i < N-1; i++)
        intact[i] = 1;
    going = 1;
    intact[0] = intact[N-2] = 0;
    ymax = 0.0;
    min_intact = N;
    DX = (XMAX - XMIN)/N;
    DM = RHO * DX;
}

void finalize()
{
    //fprintf(flog[0], "%lf\t%lf\n", strength, (N - 2*min_intact)*DX);

    //for (int i = 1; i < N-1; i++)
    //    fprintf(flog[1], "%lf\t", chain[i].vy);
    //fputc('\n', flog[1]);

    //for (int i = 1; i < min_intact; i++)
    //    if (intact[i-1] && intact[i])
    //        fprintf(flog[2], "%lf\t", chain[i].vy);
    //    else
    //        fprintf(flog[2], "%d\t", 0);
    //fputc('\n', flog[2]);

    //for (int i = 1; i < N-1; i++)
    //    fprintf(flog[3], "%lf\t", chain[i].y);
    //fputc('\n', flog[3]);

    //for (int i = 0; i < N-1; i++)
    //    fprintf(flog[4], "%d\t", intact[i]);
    //fputc('\n', flog[4]);
}

void step_chain()
{
    for (int i = 0; i < N; i++)
    {
        force[i].x = force[i].y = 0;
    }

    if (step*DT < pulse_duration)
    {
        int hw = int(pulse_width/DX/2.0);
        for (int i = 0; i < 2*hw; i++)
            force[N/2-hw+i].y = pulse_amplitude*cos((-hw+i)*M_PI/hw/2.0)*cos((-hw+i)*M_PI/hw/2.0)*(1 - fabs(step*DT - pulse_duration/2.0)/pulse_duration/2.0);
    }

    for (int i = 1; i < N-1; i++)
    {
        double fx, fy;
        fx = force[i].x;
        fy = force[i].y;

        if (intact[i-1])
        {
            double l = sqrt((chain[i].x - chain[i-1].x)*(chain[i].x - chain[i-1].x) + (chain[i].y - chain[i-1].y)*(chain[i].y - chain[i-1].y));
            fx -= E*(l - DX)/DX*(chain[i].x - chain[i-1].x)/l/DX;
            fy -= E*(l - DX)/DX*(chain[i].y - chain[i-1].y)/l/DX;
        }
        if (intact[i])
        {
            double l = sqrt((chain[i].x - chain[i+1].x)*(chain[i].x - chain[i+1].x) + (chain[i].y - chain[i+1].y)*(chain[i].y - chain[i+1].y));
            fx -= E*(l - DX)/DX*(chain[i].x - chain[i+1].x)/l/DX;
            fy -= E*(l - DX)/DX*(chain[i].y - chain[i+1].y)/l/DX;
        }

        chain[i].x += DT*chain[i].vx;
        chain[i].y += DT*chain[i].vy;

        if (fabs(fx) < 0.1) fx = 0;
        if (fabs(fy) < 0.1) fy = 0;

        chain[i].vx += fx*DT/RHO;
        chain[i].vy += fy*DT/RHO;
    }

    for (int i = 0; i < N-1; i++)
        if (sqrt((chain[i].x - chain[i+1].x)*(chain[i].x - chain[i+1].x) + (chain[i].y - chain[i+1].y)*(chain[i].y - chain[i+1].y))/DX > strength)
        {
            intact[i] = 0;
            if (i < min_intact)
                min_intact = i;
        }

    ymax = chain[0].y;
    for (int i = 1; i < N-1; i++)
        if (chain[i].y > ymax) ymax = chain[i].y;
}

int main(int argc, char** argv)
{
    sprintf(fname, fname_dummy, "diameter");
    flog = fopen(fname, "w");
    //sprintf(fname, fname_dummy, "velocity");
    //flog[1] = fopen(fname, "w");
    //sprintf(fname, fname_dummy, "intact_velocity");
    //flog[2] = fopen(fname, "w");
    //sprintf(fname, fname_dummy, "y");
    //flog[3] = fopen(fname, "w");
    //sprintf(fname, fname_dummy, "intact");
    //flog[4] = fopen(fname, "w");
    for(pulse_duration = 0.0006; pulse_duration > 0.00006; pulse_duration *= 0.8)
    //for(pulse_amplitude = 1e9; pulse_amplitude < 1.1e10; pulse_amplitude += 1e9)
        fprintf(flog, "%lf ", pulse_duration);
    fputc('\n', flog);

    for (int i=0; i<10; i++)
    {
        printf("starting with N %d\n", N); 
        fprintf(flog, "%d ", N); 
        for(pulse_duration = 0.0006; pulse_duration > 0.00006; pulse_duration *= 0.8)
        {
            printf("starting with duration %lf\n", pulse_duration);
            init_chain();
            for (step = 0; ymax < 100.0; step++)
                step_chain();
            fprintf(flog, "%lf ", (N - 2*min_intact)*DX);
        }
        fputc('\n', flog);
        N += 100;
        DT *= 0.95;
    }

    //for (int i=0; i<N_LOGS; i++)
    //    if (flog[i]) fclose(flog[i]);
    fclose(flog);

    return 0;
}

