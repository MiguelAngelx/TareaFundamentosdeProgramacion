package pe.edu.upeu.maqc;

import pe.edu.upeu.maqc.utils.LeerTeclado;
import pe.edu.upeu.maqc.utils.Menu;

public class App {


    public static void main(String[] args) {
        LeerTeclado teclado = new LeerTeclado();
        Menu menu = new Menu();

        menu.MenuOpt(teclado);
    }


}
