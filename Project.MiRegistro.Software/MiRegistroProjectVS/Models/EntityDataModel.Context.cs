//------------------------------------------------------------------------------
// <auto-generated>
//     Este código se generó a partir de una plantilla.
//
//     Los cambios manuales en este archivo pueden causar un comportamiento inesperado de la aplicación.
//     Los cambios manuales en este archivo se sobrescribirán si se regenera el código.
// </auto-generated>
//------------------------------------------------------------------------------

namespace MiRegistro.Models
{
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Infrastructure;
    
    public partial class MiRegistroEntity : DbContext
    {
        public MiRegistroEntity()
            : base("name=miregistroEntity")
        {
        }
    
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            throw new UnintentionalCodeFirstException();
        }
    
        public virtual DbSet<alerta> alerta { get; set; }
        public virtual DbSet<categoriaalerta> categoriaalerta { get; set; }
        public virtual DbSet<categoriaerror> categoriaerror { get; set; }
        public virtual DbSet<categoriaformulario> categoriaformulario { get; set; }
        public virtual DbSet<categoriatramite> categoriatramite { get; set; }
        public virtual DbSet<claseformulario> claseformulario { get; set; }
        public virtual DbSet<direccion> direccion { get; set; }
        public virtual DbSet<direccion_empresa> direccion_empresa { get; set; }
        public virtual DbSet<empleado> empleado { get; set; }
        public virtual DbSet<empresa> empresa { get; set; }
        public virtual DbSet<etapatramite> etapatramite { get; set; }
        public virtual DbSet<formulario> formulario { get; set; }
        public virtual DbSet<formulario_alerta> formulario_alerta { get; set; }
        public virtual DbSet<formulario_parametro> formulario_parametro { get; set; }
        public virtual DbSet<numeracionformulario> numeracionformulario { get; set; }
        public virtual DbSet<pais> pais { get; set; }
        public virtual DbSet<parametro> parametro { get; set; }
        public virtual DbSet<perfil> perfil { get; set; }
        public virtual DbSet<perfil_direccion> perfil_direccion { get; set; }
        public virtual DbSet<preguntaseguridad> preguntaseguridad { get; set; }
        public virtual DbSet<rol> rol { get; set; }
        public virtual DbSet<tipoformulario> tipoformulario { get; set; }
        public virtual DbSet<tramite> tramite { get; set; }
        public virtual DbSet<tramite_error> tramite_error { get; set; }
        public virtual DbSet<tramite_proceso> tramite_proceso { get; set; }
        public virtual DbSet<usuario> usuario { get; set; }
        public virtual DbSet<usuario_rol> usuario_rol { get; set; }
        public virtual DbSet<usuario_seguridad> usuario_seguridad { get; set; }
    }
}
