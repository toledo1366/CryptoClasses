using BlockchainEx.Core.Models;
using BlockchainEx.Core.Services;
using MvvmCross.ViewModels;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Threading.Tasks;

namespace BlockchainEx.Core.ViewModels
{
    public class MainViewModel:MvxViewModel
    {
        readonly IBlockchainService _blockChainService;

        public  MainViewModel(IBlockchainService blockchainService)
        {
            _blockChainService = blockchainService;
            List<Block> blockBufor = _blockChainService.GetBlock();
            Blocks = new MvxObservableCollection<Block>(blockBufor);
        }

        private MvxObservableCollection<Block> _blocks;

        public MvxObservableCollection<Block> Blocks
        {
            get => _blocks;
            set
            {
                _blocks = value;
                RaisePropertyChanged(()=>Blocks);
            }
        }
    }
}
