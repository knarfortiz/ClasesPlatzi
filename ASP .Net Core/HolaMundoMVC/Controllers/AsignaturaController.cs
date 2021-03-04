// .Net
using System;
using Microsoft.AspNetCore.Mvc;

// App
using HolaMundoMVC.Models;

namespace HolaMundoMVC.Controllers
{
	public class AsignaturaController : Controller
	{
		public IActionResult Index(){
			var asignatura = new Asignatura{
				UniqueId = Guid.NewGuid().ToString(),
			    Nombre = "Programación"
			};

			ViewBag.Fecha = DateTime.Now;

			return View(asignatura);
		}
	}
}
