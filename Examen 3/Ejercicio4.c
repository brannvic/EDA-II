#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

#define N 1000
int vector[N];

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n-1; i++)
        for (j = 0; j < n-i-1; j++)
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
}

int main() {
    int i;
    int operaciones[5] = {0};

    #pragma omp parallel private(i)
    {
        srand((unsigned int)time(NULL) ^ omp_get_thread_num());
        #pragma omp for
        for (i = 0; i < N; i++) {
            vector[i] = rand() % 1000;
        }
    }

    printf("Vector original:\n");
    for (i = 0; i < N; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n");

    #pragma omp parallel num_threads(5)
    {
        int id = omp_get_thread_num();
        int num_threads = omp_get_num_threads();
        int chunk_size = N / num_threads;
        int inicio = id * chunk_size;
        int fin = (id == num_threads - 1) ? N : inicio + chunk_size;

        bubbleSort(vector + inicio, fin - inicio);

        #pragma omp barrier

        operaciones[id] += (rand() % 10) + id;
    }

    printf("Vector ordenado:\n");
    for (i = 0; i < N; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n");

    printf("Resumen de operaciones por hilo:\n");
    int totalOperaciones = 0;
    for (i = 0; i < 5; i++) {
        printf("Hilo %d: %d operaciones\n", i, operaciones[i]);
        totalOperaciones += operaciones[i];
    }
    printf("Total de operaciones: %d operaciones\n", totalOperaciones);

    return 0;
}
