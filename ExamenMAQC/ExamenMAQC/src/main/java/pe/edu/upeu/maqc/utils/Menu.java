package pe.edu.upeu.maqc.utils;

import pe.edu.upeu.maqc.examen.ResolucionExamen;

public class Menu {
    public static void MenuOpt(LeerTeclado teclado) {
        int numberOption;
        ResolucionExamen examen = new ResolucionExamen();

        System.out.println(
                "Escoge una opcion :\n[1] Ejercicio 1 MAQC\n[2] Ejercicio 2 MAQC\n[3] Ejercicio 3 MAQC\n[4] Ejercicio 4 MAQC\n[0] Salir\n");
        System.out.print("\n==> ");
        numberOption = teclado.lector(3);

        switch (numberOption) {
            case 1:
                examen.ejercicio1();
                repeatCicle(teclado);
                break;
            case 2:
                examen.ejercicio2();
                repeatCicle(teclado);
                break;
            case 3:
                examen.ejercicio3();
                repeatCicle(teclado);
                break;
            case 4:
                int n, e;
                System.out.println("Dame el numero base: ");
                n = teclado.lector(0);
                System.out.println("Dame un numero exponencial: ");
                e = teclado.lector(0);

                System.out.println(examen.ejercicio4(n, e));
                repeatCicle(teclado);
                break;
            case 0:
                System.out.println("Hasta la proxima");
                break;
            default:
                System.out.println("No existe ese valor....");
                repeatCicle(teclado);

        }
    }

    public static void repeatCicle(LeerTeclado teclado) {
        int numberOption;
        System.out.print("\n\nDeseas volver al Menú: \n[1] SI \n[2] NO \n\n==> ");
        numberOption = teclado.lector(3);

        if (numberOption == 1) {
            MenuOpt(null);
        } else if (numberOption == 2) {
            System.out.println("\nHasta la proxima");
        } else {
            System.out.println("\nNo existen esas Opciones....");
            repeatCicle(null);
        }
    }
}