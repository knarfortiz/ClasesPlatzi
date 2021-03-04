// .Net
using System;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;

// App
using HolaMundoMVC.Models;

namespace HolaMundoMVC.Controllers
{
	public class AlumnoController : Controller
	{
		public IActionResult Index(){
			var alumno = new Alumno{Nombre="Francisco"};
			ViewBag.Fecha = DateTime.Now;

			return View(alumno);
		}

		public IActionResult MultiAlumno(){
			var listaAlumnos = GenerarAlumnosAlAzar();
			ViewBag.Fecha = DateTime.Now;

			return View("MultiAlumno", listaAlumnos);
		}
		
		private List<Alumno> GenerarAlumnosAlAzar(){
			string[] nombre1 = {"Alba", "Felipa", "Juan", "Francisco", "Liz", "Camilo", "Luis"};
			string[] nombre2= {"Pedro", "Maria", "Blanca", "Michael", "Leonardo", "Gabriela", "Marina"};
			string[] apellido = {"Ortiz", "Gonzalez", "Sanabria", "Goyeneche", "Soto", "Cardenas", "Perez"};

			var listaAlumnos = from n1 in nombre1
							   from n2 in nombre2 
							   from a1 in apellido
							   select new Alumno {Nombre = $"{n1} {n2} {a1}"};

			return listaAlumnos.OrderBy( (a1) => a1.UniqueId ).ToList();
		}
	}
}
