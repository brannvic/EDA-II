#include <stdio.h>
#include <pthread.h>
#define TAM 10
struct DatosHilo {
    int* A;
    int* B;
    int* C;
    int inicio;
    int fin;
};

void* sumar_paralelo(void* datos_hilo) {
    struct DatosHilo* datos = (struct DatosHilo*)datos_hilo;

    for (int i = datos->inicio; i < datos->fin; i++) {
        datos->C[i] = datos->A[i] + datos->B[i];
    }

    pthread_exit(NULL);
}

int main() {
    int A[TAM] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int B[TAM] = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    int C[TAM];

    int punto_medio = TAM / 2;

    struct DatosHilo datos_hilo0 = {A, B, C, 0, punto_medio};
    struct DatosHilo datos_hilo1 = {A, B, C, punto_medio, TAM};

    pthread_t hilo0, hilo1;

    pthread_create(&hilo0, NULL, sumar_paralelo, (void*)&datos_hilo0);
    pthread_create(&hilo1, NULL, sumar_paralelo, (void*)&datos_hilo1);

    pthread_join(hilo0, NULL);
    pthread_join(hilo1, NULL);

    printf("Resultado de la suma en paralelo: ");
    for (int i = 0; i < TAM; i++) {
        printf("%d ", C[i]);
    }
    printf("\n");

    return 0;
}
