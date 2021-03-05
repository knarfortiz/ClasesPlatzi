// .Net
using System;
using Microsoft.AspNetCore.Mvc;
using System.Linq;

// App
using HolaMundoMVC.Models;

namespace HolaMundoMVC.Controllers
{
	public class EscuelaController : Controller
	{
		private EscuelaContext _context;	

		public IActionResult Index(){
			ViewBag.CosaDinamica = "La monja";
			var escuela = _context.Escuelas.FirstOrDefault();
			return View(escuela);
		}

		public EscuelaController(EscuelaContext context)
		{
			_context = context;	
		}
	}
}
