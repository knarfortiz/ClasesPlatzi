using System;
using System.Collections.Generic;
using static System.Console;

namespace CoreEscuela.Entidades
{
	public class Escuela {
		public string UniqueId { get; private set; } = Guid.NewGuid().ToString();
		// Formas de declarar variables y realizar encapsulamiento
		// Forma 1
		private string nombre;
		public string Nombre
		{
			get { return "Copia: "+nombre; }
			set { nombre = value; }
		}

		// Forma 2
		public int AñoDeCreacion { get; set; }
		public string Pais { get; set; }
		public string Ciudad { get; set; }

		public List<Curso> ArregloCursos { get; set; }

		public TiposEscuela TipoEscuela { get; set; }

		// Formas de escribir el contructor
		// Forma 1 clásica
		public Escuela(string nombre, int año, TiposEscuela tipo, string pais="", string ciudad=""){
			(Nombre, AñoDeCreacion) = (nombre, año);
			Pais = pais;
			Ciudad = ciudad;
		}

		// Forma 2 asignacion por tuplas
		public Escuela(string nombre, int año) => (Nombre, AñoDeCreacion) = (nombre, año);

		public override string ToString(){
			WriteLine("------------------------------------------------------");
			WriteLine("Datos escuela");
			WriteLine("------------------------------------------------------");
			return $"Nombre: '{ Nombre }', Tipo: { TipoEscuela } \nPais: { Pais }, Ciudad: { Ciudad }";
		}
	}	
}
