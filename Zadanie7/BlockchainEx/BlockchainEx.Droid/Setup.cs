using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using MvvmCross.Platforms.Android.Core;
using MvvmCross.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BlockchainEx.Droid
{
    public class Setup : MvxAndroidSetup
    {
        protected override IMvxApplication CreateApp()
        {
            return new Core.App();
        }
    }
}