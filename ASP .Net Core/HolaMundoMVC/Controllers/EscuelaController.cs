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
			escuela.AñoDeCreación = 2005;
			escuela.UniqueId = Guid.NewGuid().ToString();
			escuela.Nombre = "Divino Salvador";
			escuela.Dirección = "El centro";
			escuela.Pais = "Colombia";
			escuela.Ciudad = "Altamira";
			escuela.TipoEscuela = TiposEscuela.Secundaria;

			ViewBag.CosaDinamica = "La monja";

			return View(escuela);
		}
	}
}
