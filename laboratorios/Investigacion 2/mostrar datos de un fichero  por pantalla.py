#include <stdio.h> //escribe una cadena en un fichero y después lo lee y escribe en pantalla
 
 
struct registro{
   char nombre[50];
};
 
 
int   main ()
   {
      FILE *fich;
      char op;
       
      struct registro datos;
      /* Escritura del float en el fichero */
      if ((fich = fopen ("cadenas.dat", "wb")) == NULL)
         {
         printf ("Error de creación del fichero\n");
         
         }
       else{
          do{
           printf("Introduce una cadena: ");
           scanf("%49s",datos.nombre);
           fwrite (&datos, sizeof (datos), 1, fich);
           printf("¿Otra? (s/n)");
           scanf("%1s",&op); 
          }while((op == 's') || (op == 'S'));
       }
       fclose (fich);
      /* Lectura del float del fichero */
      if ((fich = fopen ("cadenas.dat", "rb")) == NULL)
         {
         printf ("Error de existencia del fichero\n");
         
         }
      else{
          fread (&datos, sizeof(datos), 1, fich);
          while(!feof){
             fread (&datos, sizeof(datos), 1, fich);
          }
      } 
      fclose (fich);
      
      printf ("%s\n", datos.nombre);
   }