// .Net
using System;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

// App
using HolaMundoMVC.Models;

namespace HolaMundoMVC.Controllers
{
	public class AsignaturaController : Controller
	{
		public IActionResult Index(){
			var asignatura = new Asignatura{Nombre="Edufisica"};
			ViewBag.Fecha = DateTime.Now;

			return View(asignatura);
		}

		public IActionResult MultiAsignatura(){
			var listaAsignaturas = new List<Asignatura>(){
				new Asignatura{Nombre="Matematicas"},
				new Asignatura{Nombre="Edufisica"},
				new Asignatura{Nombre="Castellano"},
				new Asignatura{Nombre="Naturales"},
			};
			ViewBag.Fecha = DateTime.Now;

			return View("MultiAsignatura", listaAsignaturas);
		}
	}
}
