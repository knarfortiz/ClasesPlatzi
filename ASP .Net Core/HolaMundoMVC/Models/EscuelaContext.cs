// .Net
using System;
using System.Collections.Generic;
using System.Linq;
// Entity
using Microsoft.EntityFrameworkCore;
// App

namespace HolaMundoMVC.Models
{
	public class EscuelaContext : DbContext
	{
		public DbSet<Escuela> Escuelas { get; set; }
		public DbSet<Asignatura> Asignaturas { get; set; }
		public DbSet<Alumno> Alumnos { get; set; }
		public DbSet<Curso> Cursos { get; set; }
		public DbSet<Evaluación> Evaluaciones { get; set; }

		public EscuelaContext (DbContextOptions<EscuelaContext> options) : base(options) 
		{
		}

		protected override void OnModelCreating(ModelBuilder modelBuilder){
			base.OnModelCreating(modelBuilder);

			var escuela = new Escuela();
			escuela.AñoDeCreación = 2005;
			escuela.Id = Guid.NewGuid().ToString();
			escuela.Nombre = "Divino Salvador";
			escuela.Dirección = "El centro";
			escuela.Pais = "Colombia";
			escuela.Ciudad = "Altamira";
			escuela.TipoEscuela = TiposEscuela.Secundaria;

			modelBuilder.Entity<Escuela>().HasData(escuela);

			modelBuilder.Entity<Asignatura>().HasData(
				new Asignatura{Nombre="Matematicas"},
				new Asignatura{Nombre="Edufisica"},
				new Asignatura{Nombre="Castellano"},
				new Asignatura{Nombre="Naturales"}
			);

			modelBuilder.Entity<Alumno>().HasData(GenerarAlumnosAlAzar().ToArray());

		}

		private List<Alumno> GenerarAlumnosAlAzar(){
			string[] nombre1 = {"Alba", "Felipa", "Juan", "Francisco", "Liz", "Camilo", "Luis"};
			string[] nombre2= {"Pedro", "Maria", "Alberto", "Michael", "Leonardo", "Gabriela", "Marina"};
			string[] apellido = {"Ortiz", "Gonzalez", "Sanabria", "Goyeneche", "Soto", "Cardenas", "Perez"};

			var listaAlumnos = from n1 in nombre1
							   from n2 in nombre2 
							   from a1 in apellido
							   select new Alumno {Nombre = $"{n1} {n2} {a1}"};

			return listaAlumnos.OrderBy( (a1) => a1.Id ).ToList();
		}
	}
}
