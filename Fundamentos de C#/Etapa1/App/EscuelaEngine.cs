using System;
using System.Collections.Generic;
using System.Linq;
using CoreEscuela.Entidades;

namespace CoreEscuela
{
	public class EscuelaEngine
	{
		public Escuela Escuela { get; set; }	

		public EscuelaEngine()
		{
		}

		public void Inicializar(){
			/*
			 *escuela.ArregloCursos = new Curso[] {
			 *    new Curso(){ Nombre = "101" },  
			 *    new Curso(){ Nombre = "201" },  
			 *    new Curso(){ Nombre = "301" },  
			 *};
			 */
			Escuela = new Escuela("Divino Salvador", 1974, TiposEscuela.Primaria, ciudad:"Bogota", pais:"Colombia");
			 
			CargarCursos();
			CargarAsignaturas();
			CargarEvaluaciones();
		}

		private void CargarAsignaturas(){
			foreach (var curso in Escuela.ArregloCursos)
			{
				List<Asignatura> listaAsignaturas = new List<Asignatura>(){
					new Asignatura{Nombre="Matematicas"},
					new Asignatura{Nombre="Edufisica"},
					new Asignatura{Nombre="Castellano"},
					new Asignatura{Nombre="Naturales"},
				};
				curso.Asignaturas = listaAsignaturas;
			}
		}

		private List<Alumno> GenerarAlumnosAlAzar(int cantidad){
			string[] nombre1 = {"Alba", "Felipa", "Juan", "Francisco", "Liz", "Camilo", "Luis"};
			string[] nombre2= {"Pedro", "Maria", "Blanca", "Michael", "Leonardo", "Gabriela", "Marina"};
			string[] apellido = {"Ortiz", "Gonzalez", "Sanabria", "Goyeneche", "Soto", "Cardenas", "Perez"};

			var listaAlumnos = from n1 in nombre1
							   from n2 in nombre2 
							   from a1 in apellido
							   select new Alumno {Nombre = $"{n1} {n2} {a1}"};

			return listaAlumnos.OrderBy( (a1) => a1.UniqueId ).Take(cantidad).ToList();
		}

		private void CargarEvaluaciones(){
		}

		private void CargarCursos(){
			Escuela.ArregloCursos = new List<Curso>() {
				new Curso(){ Nombre = "101", Jornada=TiposJornada.Mañana },  
				new Curso(){ Nombre = "201", Jornada=TiposJornada.Mañana },  
				new Curso(){ Nombre = "301", Jornada=TiposJornada.Mañana },  
			};
			var nuevaLista =  new List<Curso>() {
				new Curso(){ Nombre = "501", Jornada=TiposJornada.Mañana },  
				new Curso(){ Nombre = "601", Jornada=TiposJornada.Mañana },  
				new Curso(){ Nombre = "701", Jornada=TiposJornada.Mañana },  
			};
			Escuela.ArregloCursos.Add(new Curso{ Nombre="102", Jornada=TiposJornada.Tarde });
			Escuela.ArregloCursos.Add(new Curso{ Nombre="202", Jornada=TiposJornada.Tarde });
			Escuela.ArregloCursos.AddRange(nuevaLista);

			Random rnd = new Random();
			foreach (var curso in Escuela.ArregloCursos)
			{
				int cantidadRandom = rnd.Next(5, 20);
				curso.Alumnos.AddRange(GenerarAlumnosAlAzar(cantidadRandom));
			}

		}
	}	
}
