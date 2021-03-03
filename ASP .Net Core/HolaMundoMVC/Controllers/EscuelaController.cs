// .Net
using System;
using Microsoft.AspNetCore.Mvc;

// App
using HolaMundoMVC.Models;

namespace HolaMundoMVC.Controllers
{
	public class EscuelaController : Controller
	{
		public IActionResult Index(){
			var escuela = new Escuela();
			escuela.AñoFundación = 2005;
			escuela.EscuelaId = Guid.NewGuid().ToString();
			escuela.Nombre = "Divino Salvador";

			return View(escuela);
		}
	}
}
