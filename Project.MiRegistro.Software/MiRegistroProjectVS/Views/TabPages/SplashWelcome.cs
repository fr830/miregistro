using Controllers;
using Models;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MiRegistro.Views.Main
{
    public partial class SplashWelcome : Form
    {
        public Login loginParent;
        protected WelcomeController oWelcomeController;
        public SplashWelcome(UserTableViewModel usuario, Login login)
        {
            InitializeComponent();
            oWelcomeController = new WelcomeController(this);
            oWelcomeController.LoadDataUser(usuario);

            loginParent = login;
        }

        public int countTimer = 0;
        public int imageToSplash = 1;
        public int totalImageToSplash = 5;
    }
}
