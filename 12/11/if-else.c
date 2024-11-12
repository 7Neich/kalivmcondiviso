#include <stdio.h>

int main()

{
    int primo;
    int secondo;
    int risultato;

    printf("\nInserisci primo numero: ");
    scanf("%d", &primo);

    printf("\nInserisci secondo numero: ");
    scanf("%d", &secondo);
    risultato = primo + secondo;
    if (secondo != 0)
    {
        printf("\n %d / %d = %d\n", primo, secondo, primo / secondo);
        printf("\n %d / %d ha resto %d\n", primo, secondo, primo % secondo);
    }
    else
    {
        printf("\n Hai appena sbloccato una gemma dell'infinito!Ma C è Thanos e ti prende a schiaffi lo stesso");
    }
    
    return 0;
}
