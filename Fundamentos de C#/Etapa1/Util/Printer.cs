using static System.Console;

namespace CoreEscuela.Util
{
	public static class Printer
	{
		public static void DibujarLinea(int tm=54){
			var linea = "".PadLeft(tm, '-');
			WriteLine(linea);
		}

		public static void WriteTitle(string title){
			DibujarLinea();
			WriteLine(title);
			DibujarLinea();
		}
	}	
}
