﻿//------------------------------------------------------------------------------
// <auto-generated>
//     Este código fue generado por una herramienta.
//     Versión de runtime:4.0.30319.42000
//
//     Los cambios en este archivo podrían causar un comportamiento incorrecto y se perderán si
//     se vuelve a generar el código.
// </auto-generated>
//------------------------------------------------------------------------------

namespace LayerData.Properties {
    
    
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGenerator", "16.6.0.0")]
    internal sealed partial class Settings : global::System.Configuration.ApplicationSettingsBase {
        
        private static Settings defaultInstance = ((Settings)(global::System.Configuration.ApplicationSettingsBase.Synchronized(new Settings())));
        
        public static Settings Default {
            get {
                return defaultInstance;
            }
        }
        
        [global::System.Configuration.ApplicationScopedSettingAttribute()]
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [global::System.Configuration.SpecialSettingAttribute(global::System.Configuration.SpecialSetting.ConnectionString)]
        [global::System.Configuration.DefaultSettingValueAttribute("Server=tcp:rna-argentina.database.windows.net,1433;Initial Catalog=MiRegistroCala" +
            "fateSC;Persist Security Info=False;User ID=adminrna;Password=registro998P;Multip" +
            "leActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Ti" +
            "meout=30;")]
        public string connectionStrings {
            get {
                return ((string)(this["connectionStrings"]));
            }
        }
        
        [global::System.Configuration.UserScopedSettingAttribute()]
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [global::System.Configuration.DefaultSettingValueAttribute("Data Source=LAPTOP-NITRO5\\SQLEXPRESS;Initial Catalog=miRegistro;Integrated Securi" +
            "ty=True")]
        public string ConnectionLocal {
            get {
                return ((string)(this["ConnectionLocal"]));
            }
            set {
                this["ConnectionLocal"] = value;
            }
        }
    }
}
