using Android.App;
using Android.Content;
using Android.Content.PM;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using MvvmCross.Platforms.Android.Views;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BlockchainEx.Droid
{
    [Activity(
            MainLauncher = true
            , Label = "BlockchainApp"
            , NoHistory = true
            , ScreenOrientation = ScreenOrientation.Portrait)]
    public class SplashScreen : MvxSplashScreenActivity
    {
        public SplashScreen()
                    : base(Resource.Layout.splash_screen)
        {
        }
    }
}