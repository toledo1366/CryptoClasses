using BlockchainEx.Core.Services;
using BlockchainEx.Core.ViewModels;
using MvvmCross;
using MvvmCross.Navigation;
using MvvmCross.ViewModels;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace BlockchainEx.Core
{
    public class App:MvxApplication
    {
        public override void Initialize()
        {
            Mvx.IoCProvider.RegisterType<IBlockchainService, BlockchainService>();

            RegisterCustomAppStart<AppStart<MainViewModel>>();
        }
    }

    public class AppStart<TViewModel> : MvxAppStart<TViewModel> where TViewModel : IMvxViewModel
    {
        public AppStart(IMvxApplication app, IMvxNavigationService mvxNavigationService) : base(app, mvxNavigationService)
        {
        }

        protected override Task NavigateToFirstViewModel(object hint = null)
        {
            NavigationService.Navigate<TViewModel>();

            return Task.CompletedTask;
        }
    }
}
