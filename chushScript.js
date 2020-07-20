// ©Sn.Lionel90, do not share without credit me, thanks!!

//Algoritmo de ligar
let yo = new Persona ("Hombre");
let ella = new Persona("Mujer");

if (yo.novia === null && yo.cruchOn (ella)){
    try{
        if (yo.pedirSalirElla(ella) == "Si"){
            yo.feliz = true;
        } else{
            yo.F_en_el_chat();

        }
    }catch(yaTengoNovioExcetion){
        yo.F_en_el_chat();

    }
}

