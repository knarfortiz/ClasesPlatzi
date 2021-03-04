using System;
using CoreEscuela.Entidades;
using CoreEscuela.Util;
using CoreEscuela;
using static System.Console;

namespace Etapa1
{
	class Program
	{
		static void Main(string[] args)
		{
			var engine = new EscuelaEngine();
			engine.Inicializar();
			ImprimirCursosEscuela(engine.Escuela);

			// ELiminar delegado
			// escuela.ArregloCursos.RemoveAll( delegate(Curso cur){ return cur.Nombre == "501"; } );

			// Eliminar Lambda
			engine.Escuela.ArregloCursos.RemoveAll( cur => cur.Nombre == "501" );

			WriteLine(engine.Escuela);
			Printer.DibujarLinea();
			ImprimirCursosEscuela(engine.Escuela);
		}

		private static void ImprimirCursosEscuela(Escuela escuela){
			Printer.WriteTitle("Lista de Cursos de la escuela");
			if(escuela?.ArregloCursos != null){	
				foreach (var curso in escuela.ArregloCursos)
					WriteLine($"Nombre: {curso.Nombre}, Id: {curso.UniqueId}");
			}
		}
	}
}
