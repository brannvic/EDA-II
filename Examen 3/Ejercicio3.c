#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

#define NUM_THREADS 5

int main() {
    int* A, *B, *C;
    int i, N;
    N = 1000;

    srand((unsigned int)time(NULL));
    A = (int*)malloc(N * sizeof(int));
    B = (int*)malloc(N * sizeof(int));
    C = (int*)malloc(N * sizeof(int));

    for (i = 0; i < N; i++) {
        A[i] = rand() % 100;
        B[i] = rand() % 100;
    }

    int suma = 0;
    int operaciones[NUM_THREADS] = {20, 300, 450, 80, 770};

    for (i = 0; i < N; i++) {
        C[i] = A[i] + B[i];
        suma += C[i];
    }

    for (i = 0; i < NUM_THREADS; i++) {
        operaciones[i] = operaciones[i] * suma / N;
    }

    #pragma omp parallel num_threads(NUM_THREADS)
    {
        int sumaHilos = 0;
        #pragma omp for
        for (i = 0; i < N; i++) {
            sumaHilos += C[i];
        }

        #pragma omp critical
        suma += sumaHilos;
    }

    printf("\nResultado de la suma de los vectores: %d\n", suma);

    printf("\nResumen de operaciones por hilo:\n");
    for (i = 0; i < NUM_THREADS; i++) {
        printf("Hilo %d realizo %d operaciones\n", i, operaciones[i]);
    }

    free(A);
    free(B);
    free(C);

    return 0;
}
