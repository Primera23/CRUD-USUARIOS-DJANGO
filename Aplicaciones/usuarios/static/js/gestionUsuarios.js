(function(){
    console.log("gestionCursos.js cargado");

    const btnEliminacion = document.querySelectorAll('.btnEliminacion');

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('¿Seguro de eliminar el Curso?')
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();