using MiRegistro.Views.Main;
using Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Controllers
{
    public class FormulariosController
    {
        Formularios _view { get; set; }

        FormModel _formModel = new FormModel();
        //MainViewModel _model = new MainViewModel();

        public FormulariosController(Formularios view)
        {
            this._view = view;
        }
    }
}
